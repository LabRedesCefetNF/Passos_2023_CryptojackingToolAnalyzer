# Trabalho Seguranca e Auditoria
*Arquivos e links usados no desenvolvimento do trabalho: Análise de ferramentas para a identificação de Cryptojacking me páginas web.*

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
