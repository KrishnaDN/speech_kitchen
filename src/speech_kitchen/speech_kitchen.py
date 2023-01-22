import os
import sox
from typing import Union
from pathlib import Path
import subprocess

def downsampler(audio_file: Union[Path, str],
                target_audio_file: Union[Path, str],
                target_sr: int, ):
    cmd = ['sox',audio_file,'-r', str(target_sr),target_audio_file]
    process = subprocess.run(cmd)
    return process