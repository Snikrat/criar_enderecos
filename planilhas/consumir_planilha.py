import openpyxl
from tkinter import messagebox

workbook = openpyxl.load_workbook('planilha_para_enderecos.xlsx', data_only=True)
aba_panilha_enderecamento = workbook['Endereçamento']

