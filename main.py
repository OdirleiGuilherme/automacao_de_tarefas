import pyautogui
from time import sleep

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

pyautogui.click(1751, 367)  # Clica no campo de login
pyautogui.write(email)  # Digita o nome de usuário

pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de senha

pyautogui.write(password)  # Digita a senha
pyautogui.press('enter')  # Pressiona Enter para fazer login
