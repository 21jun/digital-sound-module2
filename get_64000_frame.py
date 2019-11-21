from pathlib import Path

import numpy as np
import scipy.io.wavfile as wf

def get_64000_frame(data, st):
    return data[st*16000 : st*16000 + 4*16000]

if __name__ == '__main__':

    path = Path("./voice")
    get= path.glob("**/*.wav")
    files = [x for x in get if x.is_file()]

    voices = {}
    for i, file in enumerate(files):
        try:
            rate, data = wf.read(file)
            voices[file.name] = data
        except:
            print(f"can't read {file.name}")

    key = '진수빈.wav'
    
    for i in range(10):
        frame = get_64000_frame(voices[key], i)
        wf.write(f"./target/{key.split('.')[0]}_{i}_{i+4}.wav", rate, frame)