import os
import sys
from pathlib import Path

# own modules
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = str(Path(script_dir).parents[2])
sys.path.append(src_dir)

from src.neural_nets.individualAEs.MRAE.MixingRatioAE import MixingRatioAE
from src.neural_nets.individualAEs.FAE.FluxAE import FluxAE
from src.neural_nets.individualAEs.CopyAE.CopyAE import CopyAE

ae_params = dict(
    models={
        'mrae': MixingRatioAE,
        'fae': FluxAE,
    },

    state_dicts={
        'mrae': "MRAE,hparams={'latent_dim': 30, 'layer_size': 256, 'activation_function': 'tanh', 'lr': 1e-05}_state_dict",
        'fae': "FAE,hparams={'latent_dim': 256, 'layer_size': 1024, 'activation_function': 'tanh', 'lr': 1e-05}_state_dict",
    },

    model_params={
        'mrae': {
            'latent_dim': 30,
            'layer_size': 256,
            'activation_function': 'tanh',
        },
        'fae': {
            'latent_dim': 256,
            'layer_size': 1024,
            'activation_function': 'tanh',
        },
    },
)
