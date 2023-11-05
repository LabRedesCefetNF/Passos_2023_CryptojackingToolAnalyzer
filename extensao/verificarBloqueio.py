from selenium import webdriver

# Inicialização do contador
sites_bloqueados = 0

# Leitura do arquivo com as URLs
with open('seu_arquivo_de_urls.txt', 'r') as file:
    sites = file.readlines()

# Inicialização do WebDriver do navegador (ex: Chrome)
options = webdriver.ChromeOptions()
options.add_extension('/caminho/para/a/extensao/extension_id.crx')  # Substitua o caminho e a ID da extensão

driver = webdriver.Chrome(options=options)
sites_bloqueados_list = []  # Lista para armazenar os sites bloqueados

for site in sites:
    url = site.strip()  # Remove espaços em branco ou caracteres de nova linha

    try:
        driver.get(url)  # Abre o site no navegador
        # Verifica se a página contém a mensagem de bloqueio por extensão
        if "Esta página foi bloqueada por uma extensão" in driver.page_source:
            sites_bloqueados += 1
            sites_bloqueados_list.append(url)  # Adiciona o site à lista de sites bloqueados
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
