from pathlib import Path

import numpy as np
import scipy.io.wavfile as wf
from scipy import spatial

def get_fft_data(data, st):
    d = data[st*16000 : st*16000 + 4*16000]
    ft = np.fft.fft(d)
    return np.sqrt(ft.real**2 + ft.imag**2)[:int(d.shape[0]/2)]

def predict(label, voice, mean_fft_voices):
    
    prediction = {}
    # mean_fft_voices: 12명의 목소리 특징
    # data: 12명의 목소리파일 List
    # voice: 퓨리에 변환된 입력된 4초짜리 파일 
    for name, data in mean_fft_voices.items():
        cos = 1 - spatial.distance.cosine(voice, data)
        prediction[name] = cos

    prediction_desc = sorted(prediction.items(), key=lambda kv: kv[1], reverse=True)
    print(f"{label} 의 최종 예측 Label =", prediction_desc[0][0], end='\n\n')
    for i in range(12):
        print(prediction_desc[i][0], " : " ,prediction_desc[i][1])
    print(end='\n\n')
    # if label.split('_')[0] != prediction_desc[0][0].split('.')[0]:
    #     print("wrong!")

if __name__ == '__main__':


    train_path = Path("./voice")
    get= train_path.glob("**/*.wav")
    files = [x for x in get if x.is_file()]

    # test_path = Path("./target")
    test_path = Path("./test")
    test_files = [x for x in test_path.glob("**/*.wav") if x.is_file()]

    voices = {}
    for i, file in enumerate(files):
        try:
            _, data = wf.read(file)
            voices[file.name] = data
        except:
            print(f"can't read {file.name}")


    fft_voices = {}
    for name, data in voices.items():
        fft_voices[name] = [get_fft_data(data, x) for x in range(13)]
    
    mean_fft_voices = {}
    for name, data in fft_voices.items():
       mean_fft_voices[name] = np.array(data).mean(axis=0)
       # mean_fft_voices[name] = np.array(data[2])

    print("------Prediction------")

    for idx, target in enumerate(test_files):
        # print(idx, target)
        _, target_voice = wf.read(target)
        ft = np.fft.fft(target_voice)
        fft_target_voice = np.sqrt(ft.real**2 + ft.imag**2)[:int(target_voice.shape[0]/2)]
        # print(target.name)
        predict(target.name,fft_target_voice , mean_fft_voices)
        