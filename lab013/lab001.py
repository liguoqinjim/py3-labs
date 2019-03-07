# coding:utf8

from openpyxl import Workbook
from openpyxl import load_workbook


def test():
    # data_only=True的时候，是为了读取cell的值的时候不是公式
    # 有宏的文件打开的时候要加上keep_vba，不然保存之后的新文件打开会报错

    wb = load_workbook('2.xlsm', data_only=True, keep_vba=True)

    sheetsNames = ["1", "2", "3"]

    sheetMerge = wb["test"]
    sheetMergeCells = sheetMerge['E13': 'M22']

    for nameIndex in range(len(sheetsNames)):
        sheetName = sheetsNames[nameIndex]

        sheet = wb[sheetName]

        cells = sheet['E13':'G22']
        for row in range(len(cells)):
            for col in range(len(cells[row])):
                sheetMergeCells[row][col * 3 + nameIndex].value = cells[row][col].value

    wb.save("1.xlsm")
