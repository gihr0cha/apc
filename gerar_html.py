# essa função vai ler o arquivo csv que a gente vai colocar as palavras e os significados

def ler_palavras(palavras):
    lista = []
    with open(palavras, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        # esse for ta lendo as linhas do e dividindo as palavras e os significados em tuplas, sabe aql role das virgulas?
        for linha in linhas[1:]: # ta começando no 1 e não no 0 porque a primeira linha é o cabeçalho
            # aqui ta tirando os espaços em branco e dividindo a linha em duas partes, a palavra e o significado
            parte = linha.strip().split(",")
            if len(parte) == 2:
                palavra = parte[0].strip()
                significado = parte[1].strip()
                lista.append((palavra, significado))
    return lista
# isso aqui é para pegar a primeira letra da palavra e deixar maiúscula e tirar os acentos, quando a gente for add palavras que começam com acento tem que ir adicionando aqui para não criar um arquivo com a letra errada
def primeira_letra(palavra):
    letra = palavra[0].upper()
    if letra == "Á":
        return "A"
    else:
        return letra

palavras = ler_palavras("palavras.csv") # aqui a gente chama a função que leu o arquivo csv e coloca as palavras e os significados na lista

letras = {}  # aqui a gente cria um dicionário para armazenar as palavras por letra
# esse for ta percorrendo a lista de palavras e significados e colocando as palavras no dicionário de acordo com a primeira letra
for palavra, significado in palavras:
    letra = primeira_letra(palavra)
    if letra in letras:
        letras[letra].append((palavra, significado))
    else:
        letras[letra] = [(palavra, significado)]

# essa função vai criar um arquivo html para cada letra, com as palavras que começam com aquela letra
def criar_html(letra, lista_palavras):
  html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="estilo.css">
  <title>Palavras com {letra}</title>
</head>
<body>
  <h1>Palavras com {letra.upper()}</h1>

  <div class="grid">
'''
#aqui a gente ta criando um grid para colocar as palavras, cada palavra vai ser um botão que vai levar para uma página com o significado da palavra
  # esse for ta percorrendo a lista de palavras e criando um botão para cada palavra
  for palavra in lista_palavras:
        html += f'''
  <div class="palavra">
    <a href="{palavra.lower()}.html" class="button">{palavra.capitalize()}</a>
  </div>
'''

  html += '''
  </div>
</body>
</html>
'''
# aqui a gente ta criando o arquivo html com o nome da letra, tipo, pagina_a.html, pagina_b.html...
  with open(f"pagina_{letra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
  print(f"Arquivo 'pagina_{letra.lower()}.html' criado com sucesso!")





# aqui a gente ta chamando a função que cria o html para cada letra, passando a letra e a lista de palavras daquela letra

for letra in letras:
    criar_html(letra, letras[letra])

# essa função vai criar um arquivo html para cada palavra, com o significado da palavra
def criar_html_significado (palavra, significado):
    html = f'''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="estilo.css">
  <title>{palavra.capitalize()}</title>
</head>
<body>
  <div class="significado">
  <h1>{palavra.capitalize()}</h1>
  <p> Definição: {significado}</p>
  </div>
</body>
</html>
'''
# aqui a gente ta criando o arquivo html com o nome da palavra, tipo, agua.html
    with open(f"{palavra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Arquivo '{palavra.lower()}.html' criado com sucesso!")

for palavra, significado in palavras:
    criar_html_significado(palavra, significado)

# aqui a gente ta criando a primeira pagina do dicionário, que vai ser a página inicial com as letras
# e os botões para cada letra, que vão levar para as páginas com as palavras daquela letra
def criar_index_html(letras_disponiveis):
    html = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="estilo.css">
  <title>Dicionário de Palavras</title>
</head>
<body>
  <h1>Dicionário de Palavras</h1>
  <div class="grid"> 
'''
#esse sorted aqui ta ordenando as letras em ordem alfabética e depois ta pasando cada letra para a variável letra, que vai ser usada para criar os botões
    for letra in sorted(letras_disponiveis):
        html += f'''
    <div class="letra">
      <a href="pagina_{letra.lower()}.html" class="button">{letra.upper()}</a>
    </div>  
'''
    html += '''
  </div>
</body>
</html>
'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Arquivo 'index.html' criado com sucesso!")
# aqui a gente ta chamando a função que cria o index.html, passando as letras disponíveis naquele dicionário letras que a gente criou lá em cima
for letra in letras:
    criar_index_html(letras.keys())

criar_index_html(letras.keys())   
