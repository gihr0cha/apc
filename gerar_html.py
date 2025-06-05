palavras = [
    ("Água", "Substância líquida essencial para a vida e presente em rios lagos e oceanos"),
    ("Ar", "Bem natural indispensável para a respiração dos seres vivos"),
    ("Amazônia", "Floresta tropical considerada o pulmão do mundo devido à sua biodiversidade"),
    ("Aquecimento Global", "Aumento da temperatura média do planeta devido à ação humana"),
    ("Agroecologia", "Ciência que estuda formas sustentáveis de cultivo e produção agrícola"),
    ("Avaliação Ambiental", "Processo de análise dos impactos ambientais de um projeto ou atividade"),
    ("Área de Preservação", "Espaço natural protegido para conservação da biodiversidade"),
    ("Aterro Sanitário", "Local destinado ao descarte controlado de resíduos sólidos"),
    ("Atmosfera", "Camada de gases que envolve a Terra essencial para a regulação climática"),
]

html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Palavras de A a C</title>
  <style>
    body {
      background-color: #f0f8ff;
      font-family: Arial, sans-serif;
      padding: 30px;
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .palavra {
      background: #fbb6c2;
      margin: 15px 0;
      padding: 15px 20px;
      border-radius: 10px;
    }
    .palavra strong {
      font-size: 20px;
      color: #000;
    }
    .palavra p {
      margin: 5px 0 0;
      color: #333;
    }
  </style>
</head>
<body>
  <div id="lista-palavras">
'''

for palavra, significado in palavras:
    html += f'''
    <div class="palavra">
      <strong>{palavra}</strong>
      <p>{significado}</p>
    </div>
    '''

html += '''
  </div>
</body>
</html>
'''

with open("pagina_a-c.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Arquivo 'pagina_a-c.html' criado com sucesso!")
