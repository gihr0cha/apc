# Função que lerá o arquivo csv onde serão adicionadas as palavras com seus significados
def ler_palavras(palavras):
    listadepalavras = []
    with open(palavras, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        # esse for lê as linhas do CSV e divide as palavras e os significados em tuplas.
        for linha in linhas[1:]: # Começa no 1 e não no 0 porque a primeira linha é o cabeçalho.
            # aqui retira os espaços em branco e divide a linha em quatro partes, a palavra, divisão silábica, significado e fonte.
            parte = linha.strip().split(",")
            if len(parte) == 4:
                palavra = parte[0].strip()
                divisao = parte[1].strip()
                significado = parte[2].strip()
                fonte = parte[3].strip()
                listadepalavras.append((palavra, divisao, significado, fonte))
    return listadepalavras
# Tratamento de strings para retirar acentos e padronizar entradas.
def primeira_letra(palavra):
    letra = palavra[0].upper()
    if letra == "Á":
        return "A"
    elif letra == "À":
        return "A"
    elif letra == "É":
        return "E"
    elif letra == "Í":
        return "I"
    elif letra == "Ó":
        return "O"
    elif letra == "Ú":
        return "U"
    else:
        return letra

listadepalavras = ler_palavras("palavras.csv") # Chamada da função que lê o arquivo csv e coloca as palavras e os significados na listadepalavras

letras = {}  # Criação de um dicionário para armazenar as palavras por letra
# Esse for percorre a listadepalavras, divisão, significados e fontes, atribuindo palavras às letras do dicionário de acordo com a primeira letra e, caso esta ainda não exista, a adiciona.
for palavra, divisao, significado, fonte in listadepalavras:
    letra = primeira_letra(palavra)
    if letra in letras:
        letras[letra].append((palavra, divisao, significado, fonte))
    else:
        letras[letra] = [(palavra, divisao, significado, fonte)]

# Função para criar um arquivo html para cada letra, com as palavras que começam com aquela letra
def criar_html(letra, listadepalavras_palavras):
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

#aqui há a criação de um grid para colocar as palavras, cada palavra torna-se um botão que leva para uma página com seu significado
  # esse for percorre a listadepalavras e cria um botão para cada palavra
  for palavra, divisao, significado, fonte in listadepalavras_palavras:
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
# Criação do arquivo html com o nome da letra, tipo, pagina_a.html, pagina_b.html...
  with open(f"pagina_{letra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
  print(f"Arquivo 'pagina_{letra.lower()}.html' criado com sucesso!")


# Chamada da função que cria o html para cada letra, passando a letra e a listadepalavras daquela letra
for letra in letras:
    criar_html(letra, letras[letra])

# Função que cria um arquivo html para cada palavra junto à sua divisão, significado e fonte.
def criar_html_dicionario(palavra, divisao, significado, fonte):
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
  <p class="ds"> Divisão silábica: {divisao} </p>
  <p class="def"> Definição: {significado}</p>
  </div>
  <footer class="fonte">
  <p>Fonte: <a href="https://{fonte}" target="_blank">{fonte}</a></p>
  </footer>
</body>
</html>
'''
    with open(f"{palavra.lower()}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Arquivo '{palavra.lower()}.html' criado com sucesso!")

# Criação da Homepage do dicionário, com os botões para cada letra que levam aos respectivos significados
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
# Ordenação de letras em ordem alfabética e atribuição das letras às suas variáveis para criação dos botões
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

# Chamada da função que cria o index.html, passando as letras disponíveis ao dicionário letras{} criado anteriormente
for palavra, divisao, significado, fonte in listadepalavras:
    criar_html_dicionario(palavra, divisao, significado, fonte)   
criar_index_html(letras.keys())
