#!/bin/bash

# Run these two lines before submitting slurm job!
module load Miniconda3
source /home/s1850237/data1/miniconda3/julius_env_new/bin/activate

nvidia-smi

python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/MRAE/train_MRAE.py
