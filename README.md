# Dicionário de Termos do Meio Ambiente

Este projeto é um dicionário digital elaborado para a disciplina de Algoritmos e Programação de Computadores (APC) do curso de Computação da Universidade de Brasília, que reúne e explica os principais termos relacionados ao meio ambiente, sustentabilidade, ecologia e áreas afins. O objetivo é auxiliar estudantes, professores, pesquisadores e entusiastas a compreender melhor os conceitos fundamentais para a preservação ambiental.

## Funcionalidades

- Página inicial com explicação do objetivo do dicionário.
- Seleção de letras para navegar pelos termos.
- Página para cada letra, listando os termos correspondentes.
- Página individual para cada termo, com divisão silábica, definição e fonte (com link).

## Estrutura do Projeto

```
Projeto - Dicionário/
│
├── estilo.css         # Estilos do site
├── gerar_html.py      # Script Python para gerar as páginas HTML
├── index.html         # Página principal do dicionário (gerada automaticamente)
├── palavras.csv       # Base de dados dos termos, divisões, significados e fontes
```

## Como usar

1. **Adicione ou edite termos em `palavras.csv`**  
   O arquivo deve ter o seguinte formato (com 4 colunas):
   ```
   palavra,divisao,significado,fonte
   Água,Á-gua,"Líquido incolor e inodoro; composto de hidrogênio e oxigênio; H2O.",www.dicio.com.br/agua/
   ```

2. **Gere as páginas HTML**  
   Execute o script Python:
   ```sh
   python gerar_html.py
   ```
   Isso irá criar/atualizar as páginas HTML para cada letra e cada termo, além do `index.html`.

3. **Abra o `index.html` no navegador**  
   Use o botão "Acessar Dicionário" para navegar pelas letras e termos.

## Personalização

- **Cores e estilos:**  
  Edite o arquivo `estilo.css` para alterar a aparência do dicionário.
- **Texto da página inicial:**  
  O texto explicativo pode ser alterado diretamente no `index.html` ou no script Python, conforme sua preferência.

## Observações

- As fontes dos termos são exibidas como links clicáveis.
- O script trata acentos nas letras iniciais para garantir a correta organização dos termos.
- Certifique-se de que cada linha do CSV tenha exatamente 4 colunas.

## Contribuição

Sinta-se à vontade para sugerir melhorias, adicionar novos termos ou aprimorar o código!

---

Projeto desenvolvido para fins educacionais.