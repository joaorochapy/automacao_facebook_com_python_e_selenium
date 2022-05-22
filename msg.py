from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

def login(url, usuario, senha):
    # Acessa o login e maximiza a janela
    navegador.get(url)
    # navegador.maximize_window()
    sleep(3)

    # Digita email
    navegador.find_element(By.XPATH, campos['email']).send_keys(usuario)
    sleep(3)

    # Digita senha
    navegador.find_element(By.XPATH, campos['senha']).send_keys(senha)
    sleep(3)

    # Clica em entrar
    navegador.find_element(By.XPATH, campos['entrar']).click()
    sleep(10)


def pesquisar_grupo(indice):
    # Digita o nome do grupo no campo de pesquisa
    navegador.find_element(By.XPATH, campos['campo_pesquisa']).send_keys(
        grupos[indice]
    )
    sleep(3)

    # Pressiona Enter
    acao.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(12)


def publicar_materia():
    # Seleciona campo de mensagem
    # navegador.find_element(By.XPATH, campos['campo_mensagem']).click()
    # sleep(3)

    # Escreve mensagem
    navegador.find_element(By.XPATH, campos['caixa_postagem']).send_keys(
        mensagem
    )
    sleep(5)

    # Clica no botao publicar
    navegador.find_element(By.XPATH, campos['botao_publicar']).click()
    sleep(3)


def arquivo(grupo):
    # Cria um arquivo md com os nomes dos grupos nos quais foi compartilhada a
    # mensagem
    with open('lista_de_cidades.md', 'a+') as file:
        file.write(grupo)
        file.write('\n')


# Programa principal
navegador = webdriver.Chrome()
# acao = ActionChains(navegador)

# Campos e botoes
campos = {
    'email': '//*[@id="email"]',
    'senha': '//*[@id="pass"]',
    'entrar': '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button',
    'campo_pesquisa': '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input',
    'campo_mensagem': '//*[@id="mount_0_0_WC"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span',
    'caixa_postagem': '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div',
    'botao_publicar': '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div'
}

# Nomes dos grupos
grupos = [
    'grupo 1',
    'grupo 2',
    'grupo 3',
]

# Link da materia
mensagem = 'Algum link ou mensagem que deve ser compartilhada.'

login(url='https://facebook.com/', usuario='teste@email.com', senha='senha123')

pesquisar_grupo(indice=0)

publicar_materia()

arquivo(grupo=grupos[0])
