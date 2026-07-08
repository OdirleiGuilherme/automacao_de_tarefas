import pyautogui
from time import sleep

pyautogui.PAUSE = 1.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')  # Pressiona a tecla Windows
pyautogui.write('edge')  # Digita "Edge" para abrir o navegador
pyautogui.press('enter')  # Pressiona Enter para abrir o Edge

pyautogui.write(link)  # Digita o link do site
pyautogui.press('enter')  # Pressiona Enter para acessar o site

sleep(3)  # Aguarda 3 segundos para o site carregar

pyautogui.click()
