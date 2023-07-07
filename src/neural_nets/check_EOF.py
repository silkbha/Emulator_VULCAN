import os
import glob
import sys
from pathlib import Path
import multiprocessing as mp
from multiprocessing.managers import BaseManager
import shutil
import psutil
from tqdm import tqdm
import numpy as np
import torch
from torch.utils.data import DataLoader
import pickle
import importlib
import argparse

# import public modules
import matplotlib.pyplot as plt
import matplotlib.legend as lg
import scipy
from scipy.interpolate import interp1d
import scipy.optimize as sop
import time, timeit, os, sys
import ast

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[1])
sys.path.append(src_dir)

from src.vulcan_configs.vulcan_config_utils import CopyManager
from src.neural_nets.dataset_utils import unscale_example, create_scaling_dict, scale_dataset
from src.neural_nets.dataloaders import SingleVulcanDataset
from src.neural_nets.interpolate_dataset import interpolate_dataset

def check_EOF(vul_file,vul_name):
    try:
        with open(vul_file, 'rb') as handle:
            data = pickle.load(handle)
        return False
    except EOFError:
        print(
            f"\n################## EOFError! ##################"
            f"\n{vul_name}")
        return True

def generate_input_output_pair(params):
    """
    Generate simulation input and output pair.
    """

    # extract params
    (i, config_file, copy_manager, output_dir, dataset_dir, mode, time_series) = params

    # make std_output redirect file
    cf_name = os.path.basename(config_file)
    vul_file = os.path.join(output_dir, f'output_{cf_name[11:-3]}.vul')
    vul_name = os.path.basename(vul_file)
    
    # print info
    print(
        f'\n{mp.current_process()}'
        f'\non cpu {psutil.Process().cpu_num()}'
        f'\nin {os.getcwd()}'
        f'\nwith {cf_name}\n'
    )
    
    EOF = check_EOF(vul_file,vul_name)
    
    # make dict entry
    entry = {
        vul_name: EOF
    }
    
    # print info
    print(
        f'exiting'
        f'\n{mp.current_process()}\n'
    )
    
    return entry


def main(num_workers, generate=True):
    # setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    git_dir = str(Path(script_dir).parents[2])
    data_maindir = os.path.join(git_dir, 'Emulator_VULCAN/data/poly_dataset')
    output_dir = os.path.join(data_maindir, 'vulcan_output')
    config_dir = os.path.join(data_maindir, 'configs')
    VULCAN_dir = os.path.join(git_dir, 'VULCAN')
    dataset_dir = os.path.join(data_maindir, 'test_loader')
    
    mode = ""
    time_series = True
    
    # create dataset dir
    if os.path.isdir(dataset_dir):
        shutil.rmtree(dataset_dir)
    os.mkdir(dataset_dir)

    # extract saved config files, but in .txt format for some reason?
    config_files = glob.glob(os.path.join(config_dir, '*.py'))

    # setup copy manager
    BaseManager.register('CopyManager', CopyManager)
    manager = BaseManager()
    manager.start()
    mp_copy_manager = manager.CopyManager(num_workers, VULCAN_dir)

    # setup_mp_params
    mp_params = [(i, config_file, mp_copy_manager, output_dir, dataset_dir, mode, time_series)
                 for i, config_file in enumerate(config_files)]

    # run parallel
    print(f'running with {num_workers} workers...')
    with mp.get_context("spawn").Pool(processes=num_workers) as pool:
        entries = list(tqdm(pool.imap(generate_input_output_pair, mp_params),  # return results otherwise it doesn't work properly
                            total=len(mp_params)))

    # save index dict
    index_dict = {}
    for entry in entries:
        index_dict.update(entry)
    
    res = sum(x == True for x in index_dict.values())
    print(f"Number of vul files with EOFError: {res}")
    
    index_dict_file = os.path.join(dataset_dir, 'EOF_dict.pkl')
    with open(index_dict_file, 'wb') as f:
        pickle.dump(index_dict, f)

if __name__ == "__main__":
    # run main
    main(num_workers=mp.cpu_count() - 1, generate=True)


