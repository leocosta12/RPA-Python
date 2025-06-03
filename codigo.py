# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de produtos pra cadastrar
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo de cadastro até o fim


import pyautogui # biblioteca criada para fazer automações com python
import time

'''         pyautogui.write # escrever um texto
            pyautogui.press # apertar 1 tecla
            pyautogui.click # clicar em algum lugar da tela
            pyautogui.hotkey # combinação de teclas # ex: pyautogui.hotkey('ctrl', 'c')
            pyautogui.PAUSE = 0.3''' # define um delay para as ações 

pyautogui.PAUSE = 0.5 # entre todos os comandos do código o programa vai esperar para executar a ação

pyautogui.press("win") # aperta a tecla windows 
pyautogui.write("chrome") # escreve literalmente Chrome
pyautogui.press("enter") # seleciona

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # escre o endereçõ do site
pyautogui.press("enter") # seleciona
time.sleep(3) # espera de 3 segundos para carregar o site

pyautogui.click(x=731, y=413) # seleciona o campo de email
pyautogui.write("pythonimpressionador@gmail.com") # escreve o seu email
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter") # clique no botao de login
time.sleep(3)

#Importar a base de produtos pra cadastrar
import pandas 
  
tabela = pandas.read_csv("produtos.csv")

#Cadastrar os produtos
for linha in tabela.index: # estrutura de repetição para cadastrar todos os produtos

    pyautogui.click(x=778, y=289) # clicar no campo de código
    
    codigo = tabela.loc[linha, "codigo"] # pegar da tabela o valor do campo que a gente quer preencher
    
    pyautogui.write(str(codigo)) # preencher o campo
    
    pyautogui.press("tab") # passar para o proximo campo
    
    pyautogui.write(str(tabela.loc[linha, "marca"])) # preencher o campo
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != 'nan': # condição para que não fique aparacendo a palavra nan que o pandas coloca em valores vazios 
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    
    pyautogui.scroll(5000) # dar scroll de tudo pra cima
    # Passo 5: Repetir o processo de cadastro até o fim