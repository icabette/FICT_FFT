## 입력 받은 데이터를 FFT 진행 후, 원본 결과와 결과 값을 엑셀 형태로 출력하는 프로그램

import random
from scipy.fftpack import fft  
#import numpy as np

def dataCreation():
    data = []
    for i in range (0,256):
        data.append(float(format(random.uniform(0,6),".2f")))
    return data

def main():
    input = dataCreation()
    y = fft(input)
    for i in y:
        print (i)

main()