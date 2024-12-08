import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import json

janela_config = None

def abrir_configuracoes():
    global janela_config, caminho_campos 
    if janela_config and janela_config.winfo_exists():
        janela_config.lift()  
        janela_config.focus_force()  
    else:
        janela_config = tk.Toplevel()
        janela_config.title("Configurações")
        janela_config.resizable(False, False)

        largura_janela = 700
        altura_janela = 600

        largura_tela = janela_config.winfo_screenwidth()
        altura_tela = janela_config.winfo_screenheight()

        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        janela_config.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Adicionar ícone na janela
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_pasta_raiz = os.path.dirname(os.path.dirname(diretorio_atual)) 
        icon_configuracoes_janela = os.path.join(diretorio_pasta_raiz, 'criar_enderecos', 'src', 'icon_32x32.png')
        janela_config.tk.call('wm', 'iconphoto', janela_config._w, ImageTk.PhotoImage(Image.open(icon_configuracoes_janela)))

        janela_config.grab_set() 


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
        def carregar_configuracoes_json():
            try:
                with open("configuracoes_imagens.json", "r", encoding="utf-8") as file:
                    configuracoes = json.load(file)  
                    imagens = configuracoes.get("imagens", {})
                    planilhas = configuracoes.get("planilhas", {})

                    # Atualizar campos das imagens
                    for chave, caminho in imagens.items():
                        if chave in caminho_campos:
                            caminho_campos[chave].config(state='normal')
                            caminho_campos[chave].delete(1.0, "end")
                            caminho_campos[chave].insert("insert", caminho)
                            caminho_campos[chave].config(state='disabled')

                    # Atualizar campos das planilhas
                    for chave, caminho in planilhas.items():
                        if chave in caminho_campos:
                            caminho_campos[chave].config(state='normal')
                            caminho_campos[chave].delete(1.0, "end")
                            caminho_campos[chave].insert("insert", caminho)
                            caminho_campos[chave].config(state='disabled')

            except FileNotFoundError:
                messagebox.showinfo("Arquivo JSON de configurações não encontrado. Nenhum caminho carregado.")
            except json.JSONDecodeError:
                messagebox.showerror("Erro ao decodificar o JSON. Verifique o formato do arquivo.")


        # Labels para os caminhos
        img_labels = {
            "img_caminho_inicio": "imagem de Início",
            "img_caminho_cadastro": "imagem de Menu-Cadastro",
            "img_caminho_logistica": "imagem de Menu-Logística",
            "img_caminho_enderecamentos": "imagem Menu-Enderecamentos",
            "img_caminho_salvar": "imagem Icone-Salvar",
            "img_caminho_novo": "imagem Icone-Novo",
            "img_caminho_confirmacao": "imagem Confirmação",
        }
        planilha_label = "caminho_planilha"

        caminho_campos = {}

        # Criação dos campos de entrada para imagens
        i = 0
        for chave, label_text in img_labels.items():
            label = ttk.Label(frame_config, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            caminho_label = tk.Text(frame_config, height=1, width=50)
            caminho_label.grid(row=i, column=1, padx=10, pady=5)
            caminho_label.config(state='disabled')

            btn_selecionar = ttk.Button(
                frame_config, 
                text="Selecionar", 
                command=lambda cl=caminho_label: carregar_arquivo(cl, "imagem")
            )
            btn_selecionar.grid(row=i, column=2, padx=10, pady=5)

            caminho_campos[chave] = caminho_label
            i += 1

        # Adicionar campo para planilha
        label = ttk.Label(frame_config, text="Selecione a planilha")
        label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

        caminho_label = tk.Text(frame_config, height=1, width=50)
        caminho_label.grid(row=i, column=1, padx=10, pady=10)
        caminho_label.config(state='disabled')

        btn_selecionar_planilha = ttk.Button(
            frame_config, 
            text="Selecionar", 
            command=lambda cl=caminho_label: carregar_arquivo(cl, "planilha")
        )
        btn_selecionar_planilha.grid(row=i, column=2, padx=10, pady=10)

        caminho_campos[planilha_label] = caminho_label

        # Botão para salvar as configurações
        btn_salvar = ttk.Button(
        frame_config, 
        text="Salvar Configurações", 
        command= salvar_configuracoes_json
        )
        btn_salvar.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=20, ipadx=20, ipady=10)


        # Carregar as configurações salvas, se existirem
    carregar_configuracoes_json()

    janela_config.mainloop()

def salvar_configuracoes_json():
    imagens = {}
    planilhas = {}

    for chave, campo in caminho_campos.items():
        caminho = campo.get(1.0, "end-1c").strip()

        # Organizar caminhos conforme as categorias
        if chave.startswith("img_"):  
            if caminho:  
                imagens[chave] = caminho
            else:
                print(f"Caminho vazio para a chave {chave}")
        elif chave.startswith("caminho_"):  
            if caminho:  
                planilhas[chave] = caminho
            else:
                print(f"Caminho vazio para a chave {chave}")

    configuracoes = {
        "imagens": imagens,
        "planilhas": planilhas
    }

    try:
        with open("configuracoes_imagens.json", "w", encoding="utf-8") as file:
            json.dump(configuracoes, file, ensure_ascii=False, indent=4)
        print("Configurações salvas com sucesso.")
        messagebox.showinfo("Sucesso", "As configurações foram salvas!")
        janela_config.destroy()

    except Exception:
        messagebox.showwarning("Erro", "Não foi possível salvar as configurações, contate o administrador ddo sistema!")


