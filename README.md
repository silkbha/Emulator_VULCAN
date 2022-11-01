# Master Research Project
Using Neural Networks to predict the output of VULCAN Chemical Kinetics code: applied to atmospheres of giant planets (starting point: hot jupiters)

### Requirements
Conda environment with all required packages can be created from one of the included yaml files.
- requirements_cpu.yaml : for computer with iGPU (no CUDA)
- requirements_gpu.yaml : for computer with CUDA-supported nVidia GPU [COMING SOON]

Download the petitRADTRANS opacity and input data (https://petitradtrans.readthedocs.io/en/latest/content/installation.html) and put the folder in: MRP_Exo/src/stellar_spectra/input_data_std.
BEWARE: this data is ~12 GB!
