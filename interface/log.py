import tkinter as tk
import ttkbootstrap as ttk


def log(msg, text_log):
    text_log.config(state=tk.NORMAL) 
    text_log.insert(tk.END, f"{msg}\n")
    text_log.yview(tk.END)  
    text_log.config(state=tk.DISABLED) 

janela = ttk.Window

# Área de texto para log
text_log = tk.Text(
    janela,
    height=20, 
    width=90
)
text_log.pack(pady=20)
text_log.config(state=tk.DISABLED)  # Desabilitar edição


