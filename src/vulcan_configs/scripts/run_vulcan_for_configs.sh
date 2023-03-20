#!/bin/bash

source /net/student35/data2/silk/miniconda3/etc/profile.d/conda.sh

conda activate mrp

python /net/student35/data1/silk/Exo_Project/Emulator_VULCAN/src/vulcan_configs/run_vulcan_for_configs.py -w 6
