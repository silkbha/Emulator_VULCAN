#!/bin/bash

conda env create --file requirements_cuda.yml
conda activate mrp

pip install torch==1.12.1+cu113 torchvision torchaudio -f https://download.pytorch.org/whl/cu113/torch_stable.html
