# Função para remover a parte "=> Found using url_diferente" de cada linha
def clean_url(line):
    return line.split('=> Found using')[0].strip()

# Ler o arquivo e criar uma lista de URLs limpas
cleaned_urls = []
unique_urls = set()

with open('seu_arquivo_de_urls.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    url = clean_url(line)
    cleaned_urls.append(url)
    unique_urls.add(url)

# Remover linhas duplicadas
cleaned_unique_urls = list(unique_urls)

# Escrever os URLs limpos e únicos em um novo arquivo
with open('urls_limpos_unicos.txt', 'w') as output_file:
    for url in cleaned_unique_urls:
        output_file.write(url + '\n')

print("URLs limpos e únicos foram salvos no arquivo urls_limpos_unicos.txt")
