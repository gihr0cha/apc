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

  for palavra, significado in lista_palavras:
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

  with open(f"pagina_{letra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
  print(f"Arquivo 'pagina_{letra.lower()}.html' criado com sucesso!")

# essa função vai ser o arquivo csv que a gente vai colocar as palavras e os significados
def ler_palavras(palavras):
    lista = []
    with open(palavras, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        # esse for ta lendo as linhas do e dividindo as palavras e os significados
        for linha in linhas[1:]:
            parte = linha.strip().split(",")
            if len(parte) == 2:
                palavra = parte[0].strip()
                significado = parte[1].strip()
                lista.append((palavra, significado))
    return lista
# isso aqui é para pegar a primeira letra da palavra e deixar maiúscula e tirar os acentos
def primeira_letra(palavra):
    letra = palavra[0].upper()
    if letra == "Á":
        return "A"
    else:
        return letra

palavras = ler_palavras("palavras.csv")

letras = {}  # dicionário simples
for palavra, significado in palavras:
    letra = primeira_letra(palavra)
    if letra in letras:
        letras[letra].append((palavra, significado))
    else:
        letras[letra] = [(palavra, significado)]

# Gera um arquivo HTML para cada letra
for letra in letras:
    criar_html(letra, letras[letra])

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

    with open(f"{palavra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Arquivo '{palavra.lower()}.html' criado com sucesso!")

for palavra, significado in palavras:
    criar_html_significado(palavra, significado)