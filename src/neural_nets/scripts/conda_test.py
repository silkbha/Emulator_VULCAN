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

print(f'\nCUDA available: {torch.cuda.is_available()}')
print(f"CUDA {torch.version.cuda}")

print(f'\nDevice count: {torch.cuda.device_count()}')

print(torch.zeros(1).cuda())
