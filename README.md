# Master Research Project
Using deep learning to emulate the VULCAN chemical kinetics code for exoplanet atmospheres.

VULCAN: [Tsai et al. 2017](https://arxiv.org/abs/1607.00409), [Tsai et al. 2021](https://arxiv.org/abs/2108.01790)

Link to VULCAN repo: [https://github.com/exoclime/VULCAN](https://github.com/exoclime/VULCAN)

### Requirements
Conda environment with all required packages can be created from one of the included yaml files.
- requirements_cpu.yaml : for PCs without dedicated GPU
- requirements_cuda.yaml : for PCs with CUDA-supported GPU (nVidia) [COMING SOON]
- requirements_amd.yaml : for PCs with AMD GPU [MAYBE: will make if needed]
- requirements_mac.yaml : for Apple Silicon Macs [MAYBE: will make if needed]

Create environment by running the following (change "xxx" to one of the above):

```
conda env create --file requirements_xxx.yml
```

Download the petitRADTRANS opacity and input data (https://petitradtrans.readthedocs.io/en/latest/content/installation.html) and put the folder in: Emulator_VULCAN/src/stellar_spectra/input_data_std. (BEWARE: this is a ~12 GB file!)
