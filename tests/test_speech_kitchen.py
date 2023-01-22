import numpy as np
import soundfile as sf
from src.speech_kitchen import downsampler
import os

def test_downsampler(sr=16000):
    data = np.random.rand(32000)
    sf.write('src.wav', data, 22000)
    process = downsampler('src.wav','dest.wav',16000)
    assert os.path.exists('dest.wav')==True