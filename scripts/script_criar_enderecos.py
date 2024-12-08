#-*- coding: utf-8 -*-
import os
import json
import openpyxl
import time
import cv2
import pyautogui
from tkinter import messagebox
from interface.log import *



def iniciar_script_criar_enderecos(text_log):
    # Função para carregar o caminho da planilha
    def carregar_caminho_planilha():
        try:
            with open("configuracoes_imagens.json", "r", encoding="utf-8") as file:
                configuracoes = json.load(file)
                caminho_planilha = configuracoes.get("planilhas", {}).get("caminho_planilha", "")
                
                if not caminho_planilha:
                    messagebox.showerror("Erro", "Caminho da planilha não encontrado no arquivo JSON.")
                    return None
                
                if not os.path.exists(caminho_planilha):
                    messagebox.showerror("Erro", f"A planilha não foi encontrada: {caminho_planilha}")
                    return None
                
                return caminho_planilha
        
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao decodificar o JSON. Verifique o formato do arquivo.")
            return None
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado ao carregar o caminho da planilha: {str(e)}")
            return None

    # Função para carregar os caminhos das imagens
    def carregar_caminhos_imagens():
        try:
            with open("configuracoes_imagens.json", "r", encoding="utf-8") as file:
                configuracoes = json.load(file)
                imagens = configuracoes.get("imagens", {})
                
                # Dicionário para armazenar os caminhos
                caminhos_imagens = {
                    "img_caminho_inicio": imagens.get("img_caminho_inicio", ""),
                    "img_caminho_cadastro": imagens.get("img_caminho_cadastro", ""),
                    "img_caminho_logistica": imagens.get("img_caminho_logistica", ""),
                    "img_caminho_enderecamentos": imagens.get("img_caminho_enderecamentos", ""),
                    "img_caminho_salvar": imagens.get("img_caminho_salvar", ""),
                    "img_caminho_novo": imagens.get("img_caminho_novo", ""),
                    "img_caminho_confirmacao": imagens.get("img_caminho_confirmacao", "")
                }

                # Validar a existência de cada caminho
                for chave, caminho in caminhos_imagens.items():
                    if not os.path.exists(caminho):
                        messagebox.showerror("Erro", f"Imagem não encontrada para {chave}: {caminho}")

                return caminhos_imagens
        
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao decodificar o JSON. Verifique o formato do arquivo.")
            return {}
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado ao carregar caminhos das imagens: {str(e)}")
            return {}

    # Uso das funções
    caminho_planilha = carregar_caminho_planilha()
    if caminho_planilha:
        try:
            # Abrir a planilha
            planilha_enderecos = openpyxl.load_workbook(caminho_planilha, data_only=True)
            aba_planilha_enderecamento = planilha_enderecos['Endereçamento']
            log("Planilha carregada com sucesso.", text_log)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a planilha: {str(e)}")

    caminhos_imagens = carregar_caminhos_imagens()

    img_caminho_inicio = caminhos_imagens.get("img_caminho_inicio", "") 
    img_caminho_cadastro = caminhos_imagens.get("img_caminho_cadastro", "") 
    img_caminho_logistica= caminhos_imagens.get("img_caminho_logistica", "") 
    img_caminho_enderecamentos= caminhos_imagens.get("img_caminho_enderecamentos", "") 
    img_caminho_salvar= caminhos_imagens.get("img_caminho_salvar", "") 
    img_caminho_novo= caminhos_imagens.get("img_caminho_novo", "") 
    img_caminho_confirmacao= caminhos_imagens.get("img_caminho_confirmacao", "") 


    # Loop para Iniciar o Script
    def executando_loop():
            esperar_wms_carregar = True
            while esperar_wms_carregar:
                try:
                    pyautogui.locateCenterOnScreen((img_caminho_inicio), confidence=0.7)
                    log('O WMS carregou, inicianddo...', text_log)
                    esperar_wms_carregar = False
                except:
                    time.sleep(1)
                    log('Esperando o WMS carregar...', text_log)
    executando_loop()

    # Função para entrar na janela de endereços
    def entrar_na_janela_enderecos():
        # Clicar no Meno Cadastros
        cadastros = pyautogui.locateCenterOnScreen(str(img_caminho_cadastro), confidence=0.7)
        time.sleep(0.3)
        pyautogui.click(cadastros.x, cadastros.y)
        time.sleep(0.3)

        # Clicar no Sub-Menu Logistica
        logisticas = pyautogui.locateCenterOnScreen(str(img_caminho_logistica), confidence=0.7)
        time.sleep(0.3)
        pyautogui.click(logisticas.x, logisticas.y)

        # Clicar no Sub-Menu Endereçamento
        enderecamentos = pyautogui.locateCenterOnScreen(str(img_caminho_enderecamentos), confidence=0.7)
        time.sleep(0.3)
        pyautogui.click(enderecamentos.x, enderecamentos.y)           


        entrar_na_janela_enderecos()
        log('Econtrei a janela com sucesso! \n', text_log)

        def digitar_campos_enderecos():
            log("o Script sera iniciado.\n", text_log)

            # Encontra a última linha com dados na coluna A
            ultima_linha_com_dados = None
            log('Processando total de linhas...', text_log)
            # Itera de baixo para cima na coluna A
            for linha in reversed(list(aba_planilha_enderecamento.iter_rows(min_col=1, max_col=1))):
                 if linha[0].value is not None and str(linha[0].value).strip() != "":  
                    ultima_linha_com_dados = linha[0].row  
                    break  
            
            log(f'{ultima_linha_com_dados} linhas econtradas\n', text_log)
            return
    
        cadastros = pyautogui.locateCenterOnScreen(str(img_caminho_cadastro), confidence=0.7)
        logisticas = pyautogui.locateCenterOnScreen(str(img_caminho_logistica), confidence=0.7)
        enderecamentos = pyautogui.locateCenterOnScreen(str(img_caminho_enderecamentos), confidence=0.7)

        menus = [cadastros, logisticas, enderecamentos]

        for menu in menus:
            time.sleep(0.3)
            pyautogui.click(menu.x, menu.y)
            time.sleep(0.3)

        log('Econtrei a janela com sucesso! \n')
        log("o Script sera iniciado.\n")
        
        return
