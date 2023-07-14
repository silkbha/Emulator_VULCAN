sbatch \
  --job-name=train_AEs_gpu \
  --partition=amd-gpu-long \
  --gres=gpu:1 \
  --mem-per-gpu=24G \
  --ntasks=1 \
  --nodes=1 \
  --time=24:00:00 \
  --mail-user=silk@strw.leidenuniv.nl \
  --mail-type=ALL \
  --output=out_train_AEs_gpu.out \
  $HOME/data1/Emulator_VULCAN/src/neural_nets/individualAEs/train_autoencoders.sh
