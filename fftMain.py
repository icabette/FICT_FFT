## 입력 받은 데이터를 FFT 진행 후, 원본 결과와 결과 값을 엑셀 형태로 출력하는 프로그램

import random
from scipy.fftpack import fft  
import openpyxl

def dataCreation():
    data = []
    for i in range (0,512):
        data.append(float(format(random.uniform(0,6),".2f")))
    return data

def excelExport(base, result):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'FFT'
    sheet['A1'] = '원본데이터'
    sheet['B1'] = 'FFT변환데이터'
    
    cellCount = 2
    for i in base:
        sheetNum = 'A' + str(cellCount)
        sheet[sheetNum] = str(i)
        cellCount = cellCount + 1
    
    cellCount = 2
    lresult = result.tolist() # np.ndarray to list
    for i in lresult:
        sheetNum = 'B' + str(cellCount)
        # 괄호 제거
        sheet[sheetNum] = str(i).replace("(","").replace(")","")
        cellCount = cellCount + 1
    wb.save('FFT_Result.xlsx')

def main():
    input = dataCreation()
    y = fft(input)
    excelExport(input, y)

    """
    for i in y:
        print (str(i).replace("(","").replace(")",""))
    """
   
main()