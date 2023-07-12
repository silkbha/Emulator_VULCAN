#!/bin/bash

# module load Miniconda3
# conda init bash
# conda activate mrp
nvidia-smi

source /home/s1825216/miniconda3/etc/profile.d/conda.sh
conda activate mrp

python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/scripts/conda_test.py
