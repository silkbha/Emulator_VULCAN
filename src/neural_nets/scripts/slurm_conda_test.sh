sbatch \
  --job-name=test_conda_env \
  --partition=cpu-short \
  --ntasks=1 \
  --nodes=1 \
  --time=00:00:15 \
  --mail-user=silk@strw.leidenuniv.nl \
  --mail-type=ALL \
  --output=test_conda_env.out \
  $HOME/data1/Emulator_VULCAN/src/neural_nets/scripts/conda_test.sh