import requests

# Lista para armazenar sites acessíveis
sites_acessiveis = []

# Leitura do arquivo com os sites
with open('list_browser.txt', 'r') as file:
    sites = file.readlines()

# Iterar sobre cada site na lista
for site in sites:
    url = site.strip()  # Remove espaços em branco ou caracteres de nova linha

    try:
        response = requests.get(url)
        # Verifica se o status do código é 200 (OK) e se não contém a mensagem de erro
        if response.status_code == 200 and "Não é possível acessar esse site" not in response.text:
            sites_acessiveis.append(url)
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} não está acessível ou exibe a mensagem de erro.')
    except requests.RequestException as e:
        print(f'O site {url} não está acessível. Erro: {e}')

# Criar um novo arquivo com os sites acessíveis
with open('sites_acessiveis.txt', 'w') as output_file:
    for site in sites_acessiveis:
        output_file.write(site + '\n')

print("Lista de sites acessíveis salva em sites_acessiveis.txt")
