# Identificação de cryptojacking: Uma Análise de ferramentas
*This study explores the surge in cryptojacking due to the widespread popularity of cryptocurrencies. 
With a focus on safeguarding users against unauthorized cryptocurrency mining, the article evaluates five browser extension. Moreover, was developed a bot that can analyze infected sites, generating a final list that was then tested with the extensions to compare their performance. Additionally, the study produces an updated list of infected sites by processing URLs from two distinct databases. The bots enable testing with different databases, facilitating the assessment of various protection tools against cryptojacking.*


### Descrição dos arquivos:

**culprits.txt:** Lista de URL's infectadas que foram detectadas pelo Dr.Mine.

**filtro.py:** BOT responsável por filtrar URL's que estão ativas na base de dados.

**limpar.py:** BOT responsável por remover URL's repetidas e atribuir a formatação correta nos dados do arquivo culprits.txt.

**list_browser.txt:** Base de dados original com 3496 URL's.

**sites_acessiveis.txt:** Lista de sites ativos gerados pelo filtro.py.

**sites_infectados.txt:** Lista de sites que foram identificados pela ferramenta Dr.Mine como estando infectados.

**urls_limpos_unicos.txt:** Lista gerada pelo bot limpar.py.

**nomeArquivo.crx:** Identificador da extensão a ser testada.

**sites_bloqueados.txt:** Lista de sites que a extensão identificou como estando infectados por cryptojacking.

**verificarBloqueio.py**: BOT projetado para percorrer cada site da lista utilizando a extensão especificada e verificar se uma mensagem de bloqueio é exibida.

## COPYRIGHT
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

PASSOS, I. B.; SOUZA, G. P. D.; LAZARIN, N. M. __Identificação de cryptojacking: Uma Análise de ferramentas__. Anais do XV Computer on the Beach - COTB’24. Anais... Em: COMPUTER ON THE BEACH. Balneário Camboriú - Santa Catarina - Brasil: Universidade do Vale do Itajaí, 28 maio 2024. DOI: 10.14210/cotb.v15.p312-314 Disponível em: <https://periodicos.univali.br/index.php/acotb/article/view/20378>. Acesso em: 24 nov. 2024


<details>
<summary> Cite using Bibtex </summary>

```
@inproceedings{passos_identificacao_2024,
	address = {Balneário Camboriú - Santa Catarina - Brasil},
	title = {Identificação de cryptojacking: {Uma} {Análise} de ferramentas},
	shorttitle = {Identificação de cryptojacking},
	url = {https://periodicos.univali.br/index.php/acotb/article/view/20378},
	doi = {10.14210/cotb.v15.p312-314},
	abstract = {This study explores the surge in cryptojacking due to the widespreadpopularity of cryptocurrencies. With a focus on safeguardingusers against unauthorized cryptocurrency mining, the articleevaluates five browser extension. Moreover, was developed a botthat can analyze infected sites, generating a final list that was thentested with the extensions to compare their performance. Additionally,the study produces an updated list of infected sites byprocessing URLs from two distinct databases. The bots enable testingwith different databases, facilitating the assessment of variousprotection tools against cryptojacking.},
	language = {pt},
	urldate = {2024-11-24},
	booktitle = {Anais do {XV} {Computer} on the {Beach} - {COTB}'24},
	publisher = {Universidade do Vale do Itajaí},
	author = {Passos, Isadora Barroso and Souza, Gabriel Pinto De and Lazarin, Nilson Mori},
	month = may,
	year = {2024},
	pages = {312--314},
}
```
</details>
