from selenium import webdriver

# Lista para armazenar sites acessíveis
sites_acessiveis = []

# Leitura do arquivo com os sites
with open('list_browser.txt', 'r') as file:
    sites = file.readlines()

# Inicializar o WebDriver do navegador (ex: Chrome)
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver configurado

for site in sites:
    url = site.strip()  # Remove espaços em branco ou caracteres de nova linha

    try:
        driver.get(url)  # Abre o site no navegador
        # Verifica se a página contém a mensagem de erro
        if "Não é possível acessar esse site" not in driver.page_source:
            sites_acessiveis.append(url)
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} não está acessível ou exibe a mensagem de erro.')
    except Exception as e:
        print(f'O site {url} não está acessível. Erro: {e}')

# Encerra o WebDriver
driver.quit()

# Cria um novo arquivo com os sites acessíveis
with open('sites_acessiveis.txt', 'w') as output_file:
    for site in sites_acessiveis:
        output_file.write(site + '\n')

print("Lista de sites acessíveis salva em sites_acessiveis.txt")
