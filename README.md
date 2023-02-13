# Emulator_VULCAN (working title)
#### Master Research Project 2023
Using deep learning to emulate the VULCAN chemical kinetics code for exoplanet atmospheres. Continuation of [this](https://github.com/JuliusHendrix/MRP) research project by Julius Hendrix.

VULCAN (Tsai et al. [2017](https://arxiv.org/abs/1607.00409), [2021](https://arxiv.org/abs/2108.01790)): [Link to GitHub repository](https://github.com/exoclime/VULCAN).

### Setup / Requirements

Before setting up a Conda virtual environment, download the standard-resolution [petitRADTRANS opacity and input data](https://petitradtrans.readthedocs.io/en/latest/content/installation.html) (beware: this is a ~12 GB file). Rename the folder to `input_data_std` and put it in a directory of choice. Finally, add the following to your shell profile (replace the filepath with the location of `input_data_std`):

```
export prT_input_data_path="absolute/path/of/input_data_std"
```


A Conda environment with all required packages can be created from one of the included yaml files.
- `requirements_cpu.yml` : for PCs without a dedicated GPU
- `requirements_cuda.yml` : for PCs with a CUDA-supported GPU (nVidia) [COMING SOON]

Both are identical save for a different version of the PyTorch machine learning library. Create the environment by running the following in a terminal window (change "xxx" to one of the above):

```
conda env create --file requirements_xxx.yml
```