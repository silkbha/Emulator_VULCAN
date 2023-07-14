#!/bin/bash

# module load ALICE
# module load Miniconda3
# . /cm/shared/easybuild/GenuineIntel/software/Miniconda3/23.3.1-0/etc/profile.d/conda.sh
# conda activate mrp

# julius_env
module load ALICE
module load Miniconda3
source /home/s1850237/data1/miniconda3/julius_env_new/bin/activate

nvidia-smi

# source /home/s1825216/miniconda3/etc/profile.d/conda.sh
# conda activate mrp

python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/scripts/conda_test.py
