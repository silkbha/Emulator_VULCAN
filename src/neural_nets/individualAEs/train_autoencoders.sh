#!/bin/bash

module load Miniconda3
# conda init bash
# conda activate mrp
source /home/s1850237/data1/miniconda3/julius_env_new/bin/activate

nvidia-smi

# python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/MRAE/train_MRAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/WAE/train_WAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/FAE/train_FAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/HAE/train_PAE.py
