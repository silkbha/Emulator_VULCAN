import numpy as np
import glob
import os
import shutil
from sklearn.model_selection import ParameterGrid
from pathlib import Path
from tqdm import tqdm
import multiprocessing as mp
from astropy import units as u

from vulcan_config_utils import make_valid_parameter_grid


def make_config(mp_params):
    """
    Make and save a config file for a given set of parameters. Copies and appends to the "vulcan_cfg_template.py" file
    which should be in the same directory as this script.

    Args:
        mp_params: (tuple) (params, configs_dir, output_dir)
data
    Returns:

    """
    (params, configs_dir, output_dir, script_dir, runs_index) = mp_params

    # extract parameters
    orbit_radius = params['orbit_radius']
    r_star = params['r_star']
    sflux_file = params['sflux_file']
    T_eff = params["T_eff"] # not used (?)
    T_irr = params["T_irr"]
    Rp = params["Rp"]
    gs = params["gs"]
    planet_mass = params["planet_mass"]
    Z = params['Z']
    He_H = params['He_H']

    # give unique name
    dec = 3
    config_name = f'{round(orbit_radius,dec)}_{round(r_star,dec)}_{round(planet_mass,dec)}_{Z}'

    # check if config has already been run
    # (uses rounded values for check!)
    with open(runs_index) as file:
        contents=file.read()
        if config_name in contents:
            return 0
        else:
            pass

    config_filename = f'{configs_dir}/vulcan_cfg_{config_name}.py'
    output_name = f'output_{config_name}.vul'

    # copy template file
    shutil.copyfile(os.path.join(script_dir, 'vulcan_cfg_template.py'), config_filename)

    # append to template file
    with open(config_filename, 'a') as file:
        text_to_append = f"output_dir = '{output_dir}'\n" \
                         "plot_dir = 'plot/'\n" \
                         "movie_dir = 'plot/movie/'\n" \
                         f"out_name = '{output_name}'\n" \
                         f"O_H = {Z} * 6.0618E-4\n" \
                         f"C_H = {Z} * 2.7761E-4\n" \
                         f"N_H = {Z} * 8.1853E-5\n" \
                         f"S_H = {Z} * 1.3183E-5\n" \
                         f"He_H = {He_H} * 0.09692\n" \
                         f"para_warm = [120., {T_irr}, 0.1, 0.02, 1., 1.]\n" \
                         "para_anaTP = para_warm\n" \
                         f"sflux_file = '{sflux_file}'\n" \
                         f"r_star = {r_star}\n" \
                         f"Rp = {Rp}\n" \
                         f"orbit_radius = {orbit_radius}\n" \
                         f"gs = {gs}\n" \
                         f"planet_mass = {planet_mass}"

        file.write(text_to_append)
    
    # append filename to index file
    with open(runs_index, "a") as file:
        file.write("\n"+config_name)

    return 0


def main():
    # setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    git_dir = str(Path(script_dir).parents[1])
    configs_dir = os.path.join(git_dir, 'data/configs')
    output_dir_vulcan = '../../Emulator_VULCAN/data/vulcan_output/'  # vulcan needs a relative dir...
    sflux_dir = os.path.join(git_dir,'src/stellar_spectra/output')

    # index_dir : location of index of completed runs (for checking redundancies)
    #     for local runs: os.path.join(git_dir, 'index')
    #     on goot/sloe/ALICE: 'net/student35/data1/silk/Exo_Project/Emulator_VULCAN/index/'
    index_dir = os.path.join(git_dir, 'index')
    runs_index = os.path.join(index_dir, 'runs_index.txt')

    num_workers = mp.cpu_count() - 1

    # remake the config directory
    if os.path.isdir(configs_dir):
        shutil.rmtree(configs_dir)
    os.mkdir(configs_dir)

    # remake the sflux directory
    if os.path.isdir(sflux_dir):
        shutil.rmtree(sflux_dir)
    os.mkdir(sflux_dir)

    ############################################################################
    # Set up parameter ranges and intervals                                    #
    ############################################################################

    zrange = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]
    
    parameter_ranges = dict(
        orbit_radius = np.linspace(0.01, 0.5, 10) * u.AU,    # AU (circular orbit)
        planet_mass = np.linspace(0.05, 5, 20) * u.Mjup,     # Mjup
        r_star = np.linspace(0.5, 1.5, 11) * u.Rsun,         # Rsun (same as fit)
        Z = np.array(zrange),                                # Solar abundance
        He_H = np.linspace(1, 1, 1),    # Leave unchanged    # Solar abundance
    )

    # Total number of runs: 10 * 20 * 11 * 8 = 17600 runs
    # 8112 runs after skipping duplicates

    ############################################################################
    #                                                                          #
    ############################################################################

    # create parameter grid of valid configurations
    parameter_grid = ParameterGrid(parameter_ranges)
    valid_parameter_grid = make_valid_parameter_grid(parameter_grid, num_workers, sflux_dir)

    # make the mp parameters
    mp_params = [(params, configs_dir, output_dir_vulcan, script_dir, runs_index) for params in valid_parameter_grid]

    # run mp Pool
    print('Generating vulcan_cfg files...')
    with mp.Pool(num_workers) as p:
        results = list(tqdm(p.imap(make_config, mp_params),    # return results otherwise it doesn't work properly
                            total=len(mp_params)))


if __name__ == "__main__":
    main()

