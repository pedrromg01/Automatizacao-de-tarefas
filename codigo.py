# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos

# pyautogui #Controla Mouse, teclado e tela através de codigo
# pip install pyautogui

import pyautogui
import time

# Pause
pyautogui.PAUSE = 0.3 # Intervalor entre as transições do pyautogui

# Abrir o chrome
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

# Entrar no Link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('Enter')

# Esperar o site carregar
time.sleep(3) # Executa 1x

# Fazer login
pyautogui.click(x=-810, y=589, clicks=2) # button='right' or 'left'
pyautogui.write('cabralpma@gmail.com.br')

pyautogui.press('tab')# Sua senha
pyautogui.write('pedromartinscabraldealmeida')

pyautogui.press('tab') #Acessar
pyautogui.press('enter')

time.sleep(3)

# Importar a base de dados de produtos
# pandas -> pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index: # Index é o indice, são as linhas da tabela.
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=-845, y=463)

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']

    # Prencher os codigos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')


    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str('obs'))

    # Apertar para enviar
    pyautogui.press('tab')
    pyautogui.press('enter')


    pyautogui.scroll(50000)

    # Como fazer para repitir varias vezes









