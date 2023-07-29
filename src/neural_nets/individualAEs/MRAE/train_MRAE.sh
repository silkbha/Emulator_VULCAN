#!/bin/bash

# Run these two lines before submitting slurm job!
module load Miniconda3
source /home/s1850237/data1/miniconda3/julius_env_new/bin/activate

# cp -r poly_dataset/ /scratchdata/s1850237/1790125/

nvidia-smi

python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/MRAE/train_MRAE.py

# python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/core/train_lstm_core.py

# sh /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/scripts/conda_test.sh

# scp -r alice1:data1/Emulator_VULCAN/src/visualization/plot_AE_performance/performance_dicts/ ./