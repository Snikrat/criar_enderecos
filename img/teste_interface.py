import os
import tkinter as tk
from tkinter import PhotoImage
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from interface_configuracoes import abrir_configuracoes 
from log import criar_log


# Janela princippal
def iniciar_interface():
    janela = ttk.Window(themename="darkly")
    janela.title("Criar Endereços")
    janela.geometry("600x400")
    janela.resizable(False, False)

    # Caminho do ícone da janela
    icon_configuracoes_janela = r"C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\icon_32x32.png"  
    icone_janela = PhotoImage(file=icon_configuracoes_janela)
    janela.iconphoto(True, icone_janela)
    
    icon_config(janela)

    # Adiciona os botões definidos em buttons.py
    criar_botoes(janela)

    # Iniciar o loop da janela
    janela.mainloop()

def icon_config(janela):
  # Caminho do icon config
    icon_configuracoes = r"C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\gear.png"  

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
    # Centralizando os botões na janela com uma largura fixa
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(expand=True)  # 'expand=True' centraliza o frame na janela

    # Configura a grid para garantir que todas as colunas e linhas tenham o mesmo tamanho
    frame_botoes.grid_columnconfigure(0, weight=1)  # Aumenta a largura da coluna
    frame_botoes.grid_rowconfigure(0, weight=1)  # Aumenta a altura da linha
    frame_botoes.grid_rowconfigure(1, weight=1)  # Aumenta a altura da linha
    frame_botoes.grid_rowconfigure(2, weight=1)  # Aumenta a altura da linha

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
        icon_arrow = r"C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\arrow.png"  # Substitua pelo caminho correto do arquivo de imagem

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
        bootstyle="success"
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
    
    criar_log(janela) 
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
    
    criar_log(janela)
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
    
    criar_log(janela)
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
    
    criar_log(janela)

# Função para voltar para a interface principal
def voltar_para_principal(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    criar_botoes(janela)































# Executar a interface
if __name__ == "__main__":
    iniciar_interface()
