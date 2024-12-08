import tkinter as tk


# Função para criar o log
def criar_log(janela):
    text_log = tk.Text(
        janela,
        height=80, 
        width=45
    )
    text_log.pack(pady=20)
    text_log.config(state=tk.DISABLED)
    return text_log


# Função de log (para inserir mensagens)
def log(msg, text_log):
    def atualizar_log():
        text_log.config(state=tk.NORMAL)
        text_log.insert(tk.END, f"{msg}\n")
        text_log.yview(tk.END)
        text_log.config(state=tk.DISABLED)
    text_log.after(0, atualizar_log)


