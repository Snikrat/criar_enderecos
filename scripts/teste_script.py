import sys
import os
import pyautogui
# Diretório raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from planilhas.consumir_planilha import aba_panilha_enderecamento
from interface.log import *
from interface.teste_interface import *


def executar_script_criar_enderecos(text_log):
    log("Iniciando Script...\n", text_log)
    log("Validando planilha de endereços...\n", text_log)

    # Variáveis globais
    script_rodando = False

    # Função para carregar caminhos das imagens a partir de um arquivo
    def carregar_caminhos_arquivo(caminho_arquivo):
        try:
            caminhos = {}
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    if ':' in linha:
                        chave, valor = linha.split(':', 1)
                        caminhos[chave.strip()] = valor.strip()
            return {
                "img_caminho_inicio": caminhos.get("imagem de Início", ""),
                "img_caminho_cadastro": caminhos.get("imagem de Menu-Cadastro", ""),
                "img_caminho_logistica": caminhos.get("imagem de Menu-Logística", ""),
                "img_caminho_enderecamentos": caminhos.get("imagem Menu-Enderecamentos", ""),
                "img_caminho_salvar": caminhos.get("imagem Icone-Salvar", ""),
                "img_caminho_novo": caminhos.get("imagem Icone-Novo", ""),
                "img_caminho_confirmacao": caminhos.get("imagem Confirmação", ""),
            }
        except FileNotFoundError:
            raise FileNotFoundError(log("Arquivo de configurações {caminho_arquivo} não encontrado!"))
        except Exception as e:
            raise ValueError(f"Erro ao carregar configurações do arquivo: {str(e)}")

    # Função para verificar se as imagens existem
    def verificar_imagens(caminho_imagens):
        imagens = [
            caminho_imagens.get("img_caminho_inicio"),
            caminho_imagens.get("img_caminho_cadastro"),
            caminho_imagens.get("img_caminho_logistica"),
            caminho_imagens.get("img_caminho_enderecamentos"),
            caminho_imagens.get("img_caminho_salvar"),
            caminho_imagens.get("img_caminho_novo"),
            caminho_imagens.get("img_caminho_confirmacao"),
        ]
        for img in imagens:
            if not img or not os.path.exists(img):
                raise FileNotFoundError(f"A imagem {img} não foi encontrada ou o caminho está vazio!")

    # Caminho do arquivo de configurações
    caminho_arquivo_configuracoes = "configuracoes_imagens.txt"

    # Carregar e validar as imagens
    log("Carregando caminhos das imagens...\n", text_log)
    caminhos_imagens = carregar_caminhos_arquivo(caminho_arquivo_configuracoes)
    log("Verificando existência das imagens...\n", text_log)
    verificar_imagens(caminhos_imagens)

    log("Configurações validadas com sucesso!\n", text_log)