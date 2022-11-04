# Master Research Project
Using Neural Networks to predict the output of VULCAN Chemical Kinetics code: applied to atmospheres of giant planets (starting point: hot jupiters)

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

Download the petitRADTRANS opacity and input data (https://petitradtrans.readthedocs.io/en/latest/content/installation.html) and put the folder in: MRP_Exo/src/stellar_spectra/input_data_std. (BEWARE: this data is ~12 GB!)
