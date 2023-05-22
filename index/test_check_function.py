import glob
import os
from pathlib import Path

def main():
    # setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = str(Path(script_dir).parents[2])
    VULCAN_dir = os.path.join(parent_dir, 'VULCAN')
    output_dir = os.path.join(parent_dir, 'Emulator_VULCAN/data/vulcan_output')
    configs_dir = os.path.join(parent_dir, 'Emulator_VULCAN/data/configs')
    std_output_dir = os.path.join(output_dir, 'std_output')

    # TODO: create option (flag/argument) for clean start (remove outputs from previous runs)
    # Dangerous: risk of removing all output data accidentally if you don't move it first!!!

    # if clean_start:
    #     # remake output directory
    #     if os.path.isdir(output_dir):
    #         shutil.rmtree(output_dir)
    #     os.mkdir(output_dir)

    #     # remake std_output directory
    #     if os.path.isdir(std_output_dir):
    #         shutil.rmtree(std_output_dir)
    #     os.mkdir(std_output_dir)

    # load config files
    config_files = glob.glob(os.path.join(configs_dir, 'vulcan_cfg*.py'))
    print(f'Found {len(config_files)} config files.')

    # Checks for already run:
    # Create list of completed configs
    done_files = glob.glob(os.path.join(output_dir, '*.vul'))
    print(f'Found {len(done_files)} previously run configs. Removing these from queue...')
    
    # Remove completed configs from config_files list
    removed = 0
    for file in done_files:
        file = file.removeprefix("output_")
        file = file.removesuffix(".vul")
    
    print(done_files[0:3])
    print(config_files[0:3])

    for file in config_files:
        filename = file
        unique_name = file.removeprefix("vulcan_cfg_")
        unique_name = unique_name.removesuffix(".py")
        if unique_name in done_files:
            config_files.remove(filename)
            removed +=1
    print(f'   Removed {removed} configs from queue.')

if __name__ == "__main__":
    main()