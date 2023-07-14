sbatch \
  --job-name=remote_gpu \
  --partition=amd-gpu-long \
  --gres=gpu:1 \
  --mem-per-gpu=80GB \
  --ntasks=1 \
  --nodes=1 \
  --time=168:00:00 \
  $HOME/data1/Emulator_VULCAN/src/neural_nets/sleep_forever.sh
