import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import threading
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk


# Importações internas
from scripts.criar_c import iniciar_script, parar_script
from interface.log import log

# Variáveis globais
script_rodando = False
text_log = None 

# Função para iniciar o script em uma thread separada
def iniciar_script_thread():
    global script_rodando
    if not script_rodando:
        script_rodando = True
        threading.Thread(target=iniciar_script, daemon=True).start()
        log("Script iniciado.", text_log)
    else:
        log("O script já está em execução.", text_log)

# Função para iniciar a interface
def iniciar_interface():
    global text_log
    janela = ttk.Window(themename="darkly")
    janela.title("Criar Endereços")
    janela.geometry("600x400")
    janela.resizable(False, False)

    # Títulos e informações
    label_titulo = tk.Label(
        janela,
        text="Criar Endereços",
        font=("Helvetica", 16, "bold"),
        fg="white",
        bg="#2c3e50",
    )
    label_titulo.pack(pady=10)

    # Botões
    btn_iniciar = ttk.Button(
        janela, text="Iniciar Script", 
        bootstyle="success", 
        command=lambda: iniciar_script_thread()
    )
    btn_iniciar.pack(pady=10)

    btn_parar = ttk.Button(
        janela, text="Parar Script", 
        bootstyle="danger", 
        command=lambda: parar_script()
    )
    btn_parar.pack(pady=10)

    # Área de texto para log
    text_log = tk.Text(
        janela,
        height=15,
        width=70,
        state=tk.DISABLED  # Desabilitar edição inicialmente
    )
    text_log.pack(pady=10)

    janela.mainloop()

# Executar a interface
if __name__ == "__main__":
    iniciar_interface()
