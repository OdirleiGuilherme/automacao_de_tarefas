import pyautogui
from time import sleep
import pandas as pd
import numpy as np

pyautogui.PAUSE = 1.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'odirlei_007@hotmail.com'
password = '12345678'

pyautogui.press('win')  # Pressiona a tecla Windows
pyautogui.write('edge')  # Digita "Edge" para abrir o navegador
pyautogui.press('enter')  # Pressiona Enter para abrir o Edge

pyautogui.write(link)  # Digita o link do site
pyautogui.press('enter')  # Pressiona Enter para acessar o site

sleep(3)  # Aguarda 3 segundos para o site carregar

table = pd.read_csv('produtos.csv')

for line in table.index:
    pyautogui.click(x= 1751, y =367)  # Clica no campo de login
    pyautogui.write(email)  # Digita o nome de usuário

    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de senha

    pyautogui.write(password)  # Digita a senha
    pyautogui.press('enter')  # Pressiona Enter para fazer login

    pyautogui.click(x=1811, y=249)  # Clica no botão "Cadastrar Produto"
    pyautogui.write("MOLO000251")  # Digita o código do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("Logitech")  # Digita a marca do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("Mouse")  # Digita o tipo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("1")  # Digita a categoria do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("25.95")  # Digita o preço unitário do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("6.5")  # Digita o custo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)

    pyautogui.write("obs")  # Digita a observação do produto (vazio)
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    sleep(2)
    pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto
