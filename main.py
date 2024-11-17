import pyautogui
import time
import openpyxl
import pyperclip

# Consumir planilha
workbook = openpyxl.load_workbook('planilha_para_enderecos.xlsx')
sheet_enderecamento = workbook['Endereçamento']

def main():

    fluxo()
    teclas()



def fluxo():
    cadastros = pyautogui.locateCenterOnScreen(r'C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\cadastros.png', confidence=0.7)
    time.sleep(1)
    pyautogui.click(cadastros.x, cadastros.y)

    logisticas = pyautogui.locateCenterOnScreen(r'C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\logisticas.png', confidence=0.7)
    time.sleep(1)
    pyautogui.click(logisticas.x, logisticas.y)

    enderecamentos = pyautogui.locateCenterOnScreen(r'C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\enderecamentos.png', confidence=0.7)
    time.sleep(1)
    pyautogui.click(enderecamentos.x, enderecamentos.y)



def teclas():
    # Colocando a Are
    for linha in sheet_enderecamento.iter_rows(min_row=2, min_col=2):
        time.sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(1)
        area_planilha = sheet_enderecamento['A2'].value
        pyperclip.copy(area_planilha)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.hotkey('enter')     
        time.sleep(1)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Fileira
        fileira = linha[0].value
        pyautogui.typewrite(fileira)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Coluna
        coluna = linha[1].value
        pyautogui.typewrite(coluna)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Andar
        andar = linha[2].value
        pyautogui.typewrite(andar)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Posição
        posicao = linha[3].value
        pyautogui.typewrite(posicao)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Tamanho
        tamanho = linha[4].value
        pyautogui.typewrite(tamanho)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Compartilhado
        compartilhado = linha[5].value
        pyautogui.typewrite(compartilhado)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Máximo Produto
        max_produtos = linha[6].value
        max_produtos = str(max_produtos)
        pyautogui.typewrite(max_produtos)
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Class. End.
        pyautogui.typewrite('B')
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Class. Validade
        pyautogui.typewrite('A')
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Temporario
        pyperclip.copy("Não")
        pyautogui.hotkey("ctrl", "v")  
        pyautogui.hotkey('tab')
        time.sleep(1)
         # Protegido
        pyperclip.copy("Não")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey('tab')
        time.sleep(1)
         # Temperatura  
        pyperclip.copy("Não")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey('tab')
        time.sleep(1)
         # Especial
        pyperclip.copy("Não")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey('tab')
        time.sleep(1)
        # Ordenação
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.typewrite('0')
        break


        
        

# Loop principal
procurar = 'sim'

while procurar == 'sim':
    try:
        inicio = pyautogui.locateCenterOnScreen(r'C:\Users\felip\Desktop\scripts-py\Criar-enderecos\img\inicio.png', confidence=0.7)
        print('encontrei!')
        main()
        break

    except:
        time.sleep(1)
        print('não encontrei!')
        break

