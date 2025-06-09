def criar_html(letra, lista_palavras):
  html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Palavras com {letra}</title>
  <style>
    body {{ background-color: #57a1f8; font-family: Arial, sans-serif; padding: 30px; }}
    h1 {{ text-align: center; color: #333; }}
    .palavra {{ background: #fbb6c2; margin: 15px 0; padding: 15px; border-radius: 10px; }}
    .palavra:hover {{ background: #f8c3d4;}}
    .palavra strong {{ font-size: 20px; color: #000; }}
    .palavra p {{ margin: 5px 0 0; color: #333; }}
  </style>
</head>
<body>
  <h1>Palavras com {letra.upper()}</h1>
'''

  for palavra, significado in lista_palavras:
        html += f'''
  <div class="palavra">
    <strong>{palavra}</strong>
    <p>{significado}</p>
  </div>
'''

  html += '''
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

