from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_extension('/home/seguranca/trabalho-Seguranca/extensao3/CoinEater 0.1.3.0.crx') 

driver = webdriver.Chrome(options=options)

# Inicialização do contador
sites_bloqueados = 0

# Leitura do arquivo com as URLs
with open('sites_infectados.txt', 'r') as file:
    sites = file.readlines()


sites_bloqueados_list = []  # Lista para armazenar os sites bloqueados

for site in sites:
    url = site.strip()  # Remove espaços em branco ou caracteres de nova linha

    try:
        driver.get(url)  # Abre o site no navegador
        # Espera até que o elemento com a mensagem específica seja visível
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Esta página foi bloqueada por uma extensão")]'))
        )

        # Se a execução chegou até aqui, a mensagem foi encontrada
        sites_bloqueados += 1
        sites_bloqueados_list.append(url)
        print(f'O site {url} exibe a mensagem de bloqueio por extensão.')
    except Exception as e:
        print(f'Erro ao acessar o site {url}: {e}')

# Fechamento do navegador
driver.quit()

# Salva os sites bloqueados em um arquivo separado
with open('sites_bloqueados.txt', 'w') as output_file:
    for site in sites_bloqueados_list:
        output_file.write(site + '\n')

print(f"Total de sites que exibem a mensagem de bloqueio por extensão: {sites_bloqueados}")
print("Lista de sites bloqueados foi salva em sites_bloqueados.txt")
