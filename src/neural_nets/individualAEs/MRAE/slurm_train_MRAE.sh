sbatch \
  --job-name=train_MRAE \
  --partition=amd-gpu-long \
  --gres=gpu:1 \
  --mem-per-gpu=20G \
  --ntasks=1 \
  --nodes=1 \
  --time=168:00:00 \
  --mail-user=silk@strw.leidenuniv.nl \
  --mail-type=ALL \
  --output=out_train_MRAE.out \
  $HOME/data1/Emulator_VULCAN/src/neural_nets/individualAEs/MRAE/train_MRAE.sh