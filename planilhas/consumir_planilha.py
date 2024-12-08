import openpyxl
import os
from tkinter import messagebox
import json


def carregar_caminho_planilha():
    try:
        with open("configuracoes_imagens.json", "r", encoding="utf-8") as file:
            configuracoes = json.load(file)  # Carregar o JSON como dicionário
            caminho_planilha = configuracoes.get("planilhas", {}).get("caminho_planilha", "")
            
            if not caminho_planilha:
                messagebox.showinfo("Error", "Caminho da planilha não encontrado no arquivo JSON.")
            
            # Verificar se o caminho da planilha existe
            if not os.path.exists(caminho_planilha):
                messagebox.showinfo("Error", "A planilha no caminho não foi encontrada.")
            
            return caminho_planilha
    
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Erro ao decodificar o JSON. Verifique o formato do arquivo.")
        return None

# Consumir a planilha usando o caminho do JSON
    return carregar_caminho_planilha()



