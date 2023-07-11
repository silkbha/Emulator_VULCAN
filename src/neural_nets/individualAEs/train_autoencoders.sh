#!/bin/bash

# module load Miniconda3
# conda init bash
# conda activate mrp

python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/MRAE/train_MRAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/WAE/train_WAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/FAE/train_FAE.py
python /home/s1850237/data1/Emulator_VULCAN/src/neural_nets/individualAEs/HAE/train_PAE.py
