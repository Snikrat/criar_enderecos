import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

janela_config = None

def abrir_configuracoes():
    global janela_config  
    if janela_config and janela_config.winfo_exists():
        janela_config.lift()  
        janela_config.focus_force()  
    else:
        janela_config = tk.Toplevel()
        janela_config.title("Configurações")
        janela_config.geometry("700x600")
        janela_config.resizable(False, False)

        # Adicionar ícone na janela
        icon_configuracoes_janela = r"C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\icon_32x32.png"
        janela_config.iconphoto(True, ImageTk.PhotoImage(Image.open(icon_configuracoes_janela)))

        # Título da tela de configurações
        label_titulo = tk.Label(
            janela_config, 
            text="Configurações", 
            font=("Helvetica", 14, "bold"))
        label_titulo.pack(pady=10)

        frame_config = ttk.Frame(janela_config)
        frame_config.pack(padx=20, pady=20, fill="both", expand=True)

        # Função genérica para carregar arquivos
        def carregar_arquivo(caminho_label, tipo):
            janela_config.lift()
            janela_config.focus_force()
            
            if tipo == "imagem":
                filetypes = [("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp")]
                title = "Selecione a Imagem"
            elif tipo == "planilha":
                filetypes = [("Arquivos Excel", "*.xlsx;*.xls"), ("Todos os Arquivos", "*.*")]
                title = "Selecione a Planilha"
            else:
                return
            
            caminho_arquivo = filedialog.askopenfilename(title=title, filetypes=filetypes)
            
            if caminho_arquivo:
                caminho_label.config(state='normal')
                caminho_label.delete(1.0, "end")
                caminho_label.insert("insert", caminho_arquivo)
                caminho_label.config(state='disabled')

        # Função para carregar os caminhos salvos
        def carregar_configuracoes():
            try:
                with open("configuracoes_imagens.txt", "r") as file:
                    linhas = file.readlines()
                    for linha in linhas:
                        linha = linha.strip()
                        if linha:
                            try:
                                chave, caminho = linha.split(":", 1)
                                chave = chave.strip()
                                caminho = caminho.strip()
                                if chave in caminho_campos:
                                    caminho_campos[chave].config(state='normal')
                                    caminho_campos[chave].delete(1.0, "end")
                                    caminho_campos[chave].insert("insert", caminho)
                                    caminho_campos[chave].config(state='disabled')
                            except ValueError:
                                print(f"Erro ao processar linha: {linha}.")
            except FileNotFoundError:
                print("Arquivo de configurações não encontrado. Nenhum caminho carregado.")

        # Labels para os caminhos
        img_labels = [
            "imagem de Início",
            "imagem de Menu-Cadastro",
            "imagem de Menu-Logística",
            "imagem Menu-Enderecamentos",
            "imagem Icone-Salvar",
            "imagem Icone-Novo",
            "imagem Confirmação",
        ]
        planilha_label = "Selecione a planilha"

        caminho_campos = {}

        # Criação dos campos de entrada para imagens
        for i, label_text in enumerate(img_labels):
            label = ttk.Label(frame_config, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            caminho_label = tk.Text(frame_config, height=1, width=50)
            caminho_label.grid(row=i, column=1, padx=10, pady=5)
            caminho_label.config(state='disabled')

            btn_selecionar = ttk.Button(
                frame_config, 
                text="Selecionar", 
                bootstyle="primary", 
                command=lambda cl=caminho_label: carregar_arquivo(cl, "imagem")
            )
            btn_selecionar.grid(row=i, column=2, padx=10, pady=5)

            caminho_campos[label_text] = caminho_label

        # Adicionar campo para planilha
        i = len(img_labels)
        label = ttk.Label(frame_config, text=planilha_label)
        label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

        caminho_label = tk.Text(frame_config, height=1, width=50)
        caminho_label.grid(row=i, column=1, padx=10, pady=10)
        caminho_label.config(state='disabled')

        btn_selecionar_planilha = ttk.Button(
            frame_config, 
            text="Selecionar", 
            bootstyle="primary",
            command=lambda cl=caminho_label: carregar_arquivo(cl, "planilha")
        )
        btn_selecionar_planilha.grid(row=i, column=2, padx=10, pady=10)

        caminho_campos[planilha_label] = caminho_label

        # Botão para salvar as configurações
        btn_salvar = ttk.Button(
            frame_config, 
            text="Salvar Configurações", 
            bootstyle="success", 
            command=lambda: salvar_config(caminho_campos)
        )
        btn_salvar.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=20, ipadx=20, ipady=10)

        # Carregar as configurações salvas, se existirem
        carregar_configuracoes()

        janela_config.mainloop()

# Função para salvar as configurações
def salvar_config(caminho_campos):
    try:
        with open("configuracoes_imagens.txt", "w") as file:
            for label_text, caminho_label in caminho_campos.items():
                caminho = caminho_label.get(1.0, "end-1c")
                file.write(f"{label_text}: {caminho}\n")
        messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
        janela_config.destroy()
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar as configurações: {str(e)}")
