import pyautogui
from time import sleep
import pandas as pd
import numpy as np

pyautogui.PAUSE = 1.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'odirlei_007@hotmail.com'
password = '987654'

pyautogui.press('win')  # Pressiona a tecla Windows
pyautogui.write('edge')  # Digita "Edge" para abrir o navegador
pyautogui.press('enter')  # Pressiona Enter para abrir o Edge


pyautogui.write(link)  # Digita o link do site
pyautogui.press('enter')  # Pressiona Enter para acessar o site

sleep(3)  # Aguarda 3 segundos para o site carregar


pyautogui.click(x= 1751, y =367)  # Clica no campo de login
pyautogui.write(email)  # Digita o nome de usuário

pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de senha

pyautogui.write(password)  # Digita a senha
pyautogui.press('enter')  # Pressiona Enter para fazer login
    
table = pd.read_csv('produtos.csv')

for line in table.index:

    pyautogui.click(x=1811, y=249)  # Clica no botão "Cadastrar Código"
    # código
    codigo = table.loc[line, 'codigo']
    pyautogui.write(str(codigo))  # Digita o código do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    # marca
    marca = table.loc[line, 'marca']
    pyautogui.write(str(marca))  # Digita a marca do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    # tipo
    tipo = table.loc[line, 'tipo']
    pyautogui.write(str(tipo))  # Digita o tipo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    # categoria
    categoria = table.loc[line, 'categoria']
    pyautogui.write(str(categoria))  # Digita a categoria do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
   # preço
    preco_unitario = table.loc[line, 'preco_unitario']
    pyautogui.write(str(preco_unitario))  # Digita o preço unitário do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    # custo
    custo = table.loc[line, 'custo']
    pyautogui.write(str(custo))  # Digita o custo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    # obs
    obs = table.loc[line, 'obs']
    pyautogui.write(str(obs))  # Digita a observação do produto (vazio)
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    
    pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto
    
    pyautogui.scroll(600)  # Rola a tela para baixo para visualizar o próximo produto
