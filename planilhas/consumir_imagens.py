import os
from tkinter import messagebox
from planilhas.consumir_planilha import *
from PIL import Image, ImageTk



# Função para carregar os caminhos das imagens do JSON
def carregar_caminhos_imagens():
    try:
        with open("configuracoes_imagens.json", "r", encoding="utf-8") as file:
            configuracoes = json.load(file) 
            imagens = configuracoes.get("imagens", {})
            
            caminhos_imagens = {
                "img_caminho_inicio": imagens.get("img_caminho_inicio", ""),
                "img_caminho_cadastro": imagens.get("img_caminho_cadastro", ""),
                "img_caminho_logistica": imagens.get("img_caminho_logistica", ""),
                "img_caminho_enderecamentos": imagens.get("img_caminho_enderecamentos", ""),
                "img_caminho_salvar": imagens.get("img_caminho_salvar", ""),
                "img_caminho_novo": imagens.get("img_caminho_novo", ""),
                "img_caminho_confirmacao": imagens.get("img_caminho_confirmacao", "")
            }
            
            # Validar se os arquivos existem
            for caminho in caminhos_imagens.items():
                if not os.path.exists(caminho):
                    messagebox.showerror("Error", "Uma das imagens não foi encontrada, verifique os caminhos e tente novamente.")
            
            return caminhos_imagens
        
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Erro ao decodificar o JSON. Verifique o formato do arquivo.")
        return {}

    # Carregar os caminhos das imagens
    return