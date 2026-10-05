import pyautogui
import time

pyautogui.PAUSE = 0.5
link='https://dlp.hashtagtreinamentos.com/python/intensivao/tabela'

def enter():
    pyautogui.press('enter')

def openSystem():
    # PASSO 1: ENTRAR NO SISTEMA
    pyautogui.hotkey('command', 'space', interval=0.1)

    pyautogui.write('chrome')

    enter()

    pyautogui.write(link)

    enter()

    # pausa para carregar pagina
    time.sleep(1)

# PASSO 2: REALIZAR O LOGIN

def login():
    pyautogui.hotkey('tab')

    time.sleep(.5)

    pyautogui.write('luiz@gmail.com')

    time.sleep(.5)

    pyautogui.hotkey('tab')

    pyautogui.write('123456')

    time.sleep(.5)

    pyautogui.hotkey('tab')
    enter()

# PASSO 3: ABRIR A BASE DE DADOS

def fillForm():
    import pandas as pd

    dados = pd.read_csv('produtos.csv')

    count = 0

    for linha in dados.index:
        if count == 5:
            break
        
        pyautogui.click(x=615, y=329)

        codigo = str(dados.loc[linha, 'codigo'])
        pyautogui.write(codigo)

        pyautogui.hotkey('tab')

        marca = str(dados.loc[linha, 'marca'])
        pyautogui.write(marca)

        pyautogui.hotkey('tab')

        tipo = str(dados.loc[linha, 'tipo'])
        pyautogui.write(tipo)

        pyautogui.hotkey('tab')

        categoria = str(dados.loc[linha, 'categoria'])
        pyautogui.write(categoria)

        pyautogui.hotkey('tab')

        preco_unitario = str(dados.loc[linha, 'preco_unitario'])
        pyautogui.write(preco_unitario)

        pyautogui.hotkey('tab')

        custo = str(dados.loc[linha, 'custo'])
        pyautogui.write(custo)

        pyautogui.hotkey('tab')

        obs = str(dados.loc[linha, 'obs'])
        
        if obs != 'nan':
            pyautogui.write(obs)
        else:
             pyautogui.write('-')

        pyautogui.hotkey('tab')

        enter()
        enter()

        time.sleep(1)

        # ir para o inicio da tela
        pyautogui.scroll(5000)

        count += 1

openSystem()

fillForm()

