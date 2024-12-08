# -*- coding: utf-8 -*-
import sys
import os
# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap as Window
import threading
from PIL import Image, ImageTk
from interface_configuracoes import abrir_configuracoes 
from log import *
from scripts.script_criar_enderecos import *


# Janela princippal
def iniciar_interface():
    janela = ttk.Window(themename="darkly")
    janela.title("Criar Endereços")

    largura_janela = 600
    altura_janela = 400

    # Obter largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcular posição X e Y para centralizar a janela
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Configurar tamanho e posição da janela
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    janela.resizable(False, False)
    
    # Adicionar ícone na janela
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_pasta_raiz = os.path.dirname(os.path.dirname(diretorio_atual)) 
    icon_configuracoes_janela = os.path.join(diretorio_pasta_raiz, 'criar_enderecos', 'src', 'icon_32x32.png')
    janela.tk.call('wm', 'iconphoto', janela._w, ImageTk.PhotoImage(Image.open(icon_configuracoes_janela)))


    # Adiciona os botões definidos em buttons.py
    criar_botoes(janela)

    

    # Iniciar o loop da janela
    janela.mainloop()

def icon_config(janela):
  # Caminho do icon config
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_pasta_raiz = os.path.dirname(os.path.dirname(diretorio_atual)) 
    icon_configuracoes = os.path.join(diretorio_pasta_raiz, 'criar_enderecos', 'src', 'gear.png')

    # Redimensionar icon config
    tamanho_novo = (22, 22)  # Ajuste para o tamanho desejado
    imagem_original = Image.open(icon_configuracoes)
    imagem_redimensionada = imagem_original.resize(tamanho_novo, Image.Resampling.LANCZOS)  # Atualização aqui
    icone = ImageTk.PhotoImage(imagem_redimensionada)

    # Criar botão com o ícone no canto superior direito
    btn_engrenagem = ttk.Button(
        janela,
        image=icone,
        bootstyle="dark",
        command=abrir_configuracoes
    )
    btn_engrenagem.image = icone  # Manter referência
    btn_engrenagem.place(x=555)  # Ajuste as coordenadas conforme necessário


# Botoes
def criar_botoes(janela):
    
    # Centralizando os botões 
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(expand=True) 

    # Configurar grid 
    frame_botoes.grid_columnconfigure(0, weight=1)
    frame_botoes.grid_rowconfigure(0, weight=1) 
    frame_botoes.grid_rowconfigure(1, weight=1)  
    frame_botoes.grid_rowconfigure(2, weight=1)  

    icon_config(janela)

    # Botão Criar Endereços
    btn_criar_endereco = ttk.Button(
        frame_botoes, 
        text="Criar Endereços", 
        bootstyle="primary", 
        command=lambda: interface_criar_enderecos(janela)  # Substitua pela função real
    )
    btn_criar_endereco.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10, sticky="ew")

    # Botão Ativar Endereços
    btn_ativar_endereco = ttk.Button(
        frame_botoes, 
        text="Ativar Endereços", 
        bootstyle="info", 
        command=lambda: interface_ativar_enderecos(janela)  # Substitua pela função real
    )
    btn_ativar_endereco.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10, sticky="ew")

    # Botão Excluir Endereços
    btn_excluir_endereco = ttk.Button(
        frame_botoes, 
        text="Excluir Endereços", 
        bootstyle="danger", 
        command=lambda: interface_excluir_enderecos(janela)  # Substitua pela função real
    )
    btn_excluir_endereco.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=10, sticky="ew")

    # Comparar endereços
    btn_comparar_endereco = ttk.Button(
        frame_botoes, 
        text="Comparar Endereços", 
        bootstyle="warning", 
        command=lambda: interface_comparar_enderecos(janela)  # Substitua pela função real
    )
    btn_comparar_endereco.grid(row=3, column=0, padx=10, pady=10, ipadx=20, ipady=10, sticky="ew")



# Função para voltar para a interface principal
def voltar_para_principal(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    criar_botoes(janela)
    

def voltar(janela):
    # Caminho do icon config
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_pasta_raiz = os.path.dirname(os.path.dirname(diretorio_atual)) 
        icon_arrow = os.path.join(diretorio_pasta_raiz, 'criar_enderecos', 'src', 'arrow.png')
        # Redimensionar icon config
        tamanho_novo = (22, 22)  # Ajuste para o tamanho desejado
        imagem_original = Image.open(icon_arrow)
        imagem_redimensionada = imagem_original.resize(tamanho_novo, Image.Resampling.LANCZOS)  # Atualização aqui
        icone = ImageTk.PhotoImage(imagem_redimensionada)

    # Criar botão voltar
        btn_voltar = ttk.Button(
            janela,
            image=icone,
            bootstyle="dark",
            command=lambda:voltar_para_principal(janela)
        )
        btn_voltar.image = icone  # Manter referência
        btn_voltar.place(x=0)  # Ajuste as coordenadas conforme necessário
        return


# Janela dos botoes
def interface_criar_enderecos(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    
    label_titulo = tk.Label(
        janela, 
        text="Criando Endereços", 
        font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=10)

    

   # Frame para os botões à direita
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(
        side="left", 
        padx=20, 
        pady=20
        )

    # Botão 1
    iniciar_criar_enderecos = ttk.Button(
        frame_botoes, 
        text="Iniciar Script", 
        bootstyle="success",
        command=lambda: threading.Thread(
        target=iniciar_script_criar_enderecos, 
        args=(text_log,), 
        daemon=True
    ).start()
        )
    iniciar_criar_enderecos.grid(
        row=0, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10)

    # Botão 2
    parar_criar_enderecos = ttk.Button(
        frame_botoes, 
        text="Parar Script", 
        bootstyle="danger"
        )
    parar_criar_enderecos.grid(
        row=1, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10
        )
    
    text_log = criar_log(janela) 
    voltar(janela)
    

# Janela Ativar Enderços
def interface_ativar_enderecos(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    
    label_titulo = tk.Label(
        janela, 
        text="Ativar endereços", 
        font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=10)

   # Frame para os botões à direita
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(
        side="left", 
        padx=20, 
        pady=20
        )

    # Botão 1
    iniciar_ativar_enderecos = ttk.Button(
        frame_botoes, 
        text="Iniciar Script", 
        bootstyle="success"
        )
    iniciar_ativar_enderecos.grid(
        row=0, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10)

    # Botão 2
    parar_ativar_enderecos = ttk.Button(
        frame_botoes, 
        text="Parar Script", 
        bootstyle="danger"
        )
    parar_ativar_enderecos.grid(
        row=1, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10
        )
    
    text_log = criar_log(janela) 
    voltar(janela)


# Janela Excluir Enderços
def interface_excluir_enderecos(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    
    label_titulo = tk.Label(
        janela, 
        text="Excluir endereços", 
        font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=10)

   # Frame para os botões à direita
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(
        side="left", 
        padx=20, 
        pady=20
        )

    # Botão 1
    iniciar_excluir_enderecos = ttk.Button(
        frame_botoes, 
        text="Iniciar Script", 
        bootstyle="success"
        )
    iniciar_excluir_enderecos.grid(
        row=0, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10)

    # Botão 2
    parar_excluir_enderecos = ttk.Button(
        frame_botoes, 
        text="Parar Script", 
        bootstyle="danger"
        )
    parar_excluir_enderecos.grid(
        row=1, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10
        )
    
    text_log = criar_log(janela) 
    voltar(janela)

def interface_comparar_enderecos(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    
    label_titulo = tk.Label(
        janela, 
        text="Comparar endereços", 
        font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=10)
    
   # Frame para os botões à direita
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(
        side="left", 
        padx=20, 
        pady=20
        )

    # Botão 1
    iniciar_comparar_enderecos = ttk.Button(
        frame_botoes, 
        text="Iniciar Script", 
        bootstyle="success"
        )
    iniciar_comparar_enderecos.grid(
        row=0, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10)

    # Botão 2
    parar_comparar_enderecos = ttk.Button(
        frame_botoes, 
        text="Parar Script", 
        bootstyle="danger"
        )
    parar_comparar_enderecos.grid(
        row=1, 
        column=0, 
        padx=10, 
        pady=10, 
        ipadx=20, 
        ipady=10
        )
    
    text_log = criar_log(janela) 
    voltar(janela)

# Função para voltar para a interface principal
def voltar_para_principal(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    criar_botoes(janela)































# Executar a interface
if __name__ == "__main__":
    iniciar_interface()
