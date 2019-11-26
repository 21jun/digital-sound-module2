## 목소리 파일 추가 (최소 13초 이상의 wav 파일들)
```
digitial-sound-module2
    └─voice
        ├─1조 - .wav 파일들 ...
        ├─2조
        ├─3조
        ├─4조
        ├─5조
        └─6조
```

## 테스트할 파일 추가 (4초 / 64000frame wav 파일들)

```
digitial-sound-module2
    └─test
        └─1.wav
        └─2.wav
        └─... 

```


## 파이썬 환경설정

가상환경 설치 후 실행
```cmd
cd digitial-sount-module2
python -m venv venv
venv\Script\activate
```

라이브러리 설치
```
pip install numpy scipy
```

## 프로그램 실행

```
python main.py
```

## 결과
```
(venv) C:\Users\oasis\develop\digital-sound-module2>python main.py
------Prediction------
17김지수 (2).wav 의 최종 예측 Label = 17김지수.wav

2조 이수진 cut.wav 의 최종 예측 Label = 이수진.wav

3조 김기백 cut.wav 의 최종 예측 Label = 김기백.wav

4초 신현욱 cut.wav 의 최종 예측 Label = 신현욱.wav

5조 김규리 cut.wav 의 최종 예측 Label = 김규리.wav

6조 이정민 cut.wav 의 최종 예측 Label = 이정민.wav

cut(5.7-9.7).wav 의 최종 예측 Label = 15김지수.wav

김규리 (2).wav 의 최종 예측 Label = 김규리.wav

김재영 (2).wav 의 최종 예측 Label = 김재영.wav

진수빈4초.wav 의 최종 예측 Label = 진수빈.wav

```