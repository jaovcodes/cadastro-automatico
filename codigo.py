# 1 passo: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/tabela
# 2 passo: fazer loguin
# 3 passo: importar a base de dados
# 4 passo: cadastrar um produto
# 5 passo: repetir para todos os produtos

import pyautogui
import time
pyautogui.PAUSE = 0.5

# entrar no navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# fazer login

pyautogui.click(x=923, y=468)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")
pyautogui.press("enter")

time.sleep(3)

# importar base de dados

import pandas as pd

pyautogui.FAILSAFE = True  # deixe True por segurança

tabela = pd.read_csv("produtos.csv")

# cadastar produtos

for linha in tabela.index:  # repetir o processo
    
    pyautogui.click(x=613, y=328)
    time.sleep(0.5)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    if not pd.isna(preco):
        pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    if not pd.isna(custo):
        pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000) # scroll para cima