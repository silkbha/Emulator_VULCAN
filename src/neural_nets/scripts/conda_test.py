import os
import sys
from pathlib import Path
from tqdm import tqdm
import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import pickle

print(f"PyTorch {torch.__version__}")

# setup pytorch
device = torch.device(f"cuda:{params['gpu']}" if torch.cuda.is_available() else "cpu")
print(f'Running on {device}')