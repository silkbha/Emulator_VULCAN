import os
import sys
from pathlib import Path

from tqdm import tqdm
import torch
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import pickle

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[2])
sys.path.append(src_dir)

from src.neural_nets.dataloaders import SingleVulcanDataset
from src.neural_nets.dataset_utils import make_data_loaders
from src.neural_nets.NN_utils import move_to, plot_core_y_mixs, weight_decay

from src.neural_nets.core.ae_params import ae_params
from src.neural_nets.core.gaussian_noise import GaussianNoise


# setup directories
script_dir = os.path.dirname(os.path.abspath(__file__))
MRP_dir = str(Path(script_dir).parents[2])


dataset_dir = os.path.join(MRP_dir, 'data/poly_dataset/dataset')
# get species list
spec_file = os.path.join(dataset_dir, 'species_list.pkl')
with open(spec_file, 'rb') as f:
    spec_list = pickle.load(f)
print("poly:", len(spec_list))

dataset_dir = os.path.join(MRP_dir, 'data/poly_dataset/time_series_dataset')
# get species list
spec_file = os.path.join(dataset_dir, 'species_list.pkl')
with open(spec_file, 'rb') as f:
    spec_list = pickle.load(f)
print("pTS :", len(spec_list))


dataset_dir = os.path.join(MRP_dir, 'data/bday_dataset/dataset')
# get species list
spec_file = os.path.join(dataset_dir, 'species_list.pkl')
with open(spec_file, 'rb') as f:
    spec_list = pickle.load(f)
print("bday:", len(spec_list))

dataset_dir = os.path.join(MRP_dir, 'data/bday_dataset/time_series_dataset')
# get species list
spec_file = os.path.join(dataset_dir, 'species_list.pkl')
with open(spec_file, 'rb') as f:
    spec_list = pickle.load(f)
print("bTS :", len(spec_list))