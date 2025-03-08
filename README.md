## Sprint de Python -  Global Solution

    Guilherme Oliveira da silva - rm558797
    Rafael Panhoca - rm555014

### Dashboard de Monitoramento de Microplásticos -

Este projeto utiliza a biblioteca Streamlit para criar um dashboard interativo que exibe dados sobre a coleta de microplásticos em diferentes oceanos. A visualização inclui um mapa de calor, gráficos interativos e informações gerais sobre os dados coletados.

## REQUISITOS - INSTRUÇÕES

Bibliotecas Python Necessárias
pandas
streamlit
folium
streamlit_folium
plotly
openpyxl (para leitura de arquivos Excel)
Instalação das Dependências

Certifique-se de ter o Python e o pip instalados. Em seguida, instale as bibliotecas necessárias utilizando o comando abaixo no terminal ou prompt de comando:

# Criando Ambiente Virtual pelo Terminal do VSCode

Neste guia, vamos mostrar como criar um ambiente virtual usando o terminal do VSCode.

## Passos para Rodar o Código

Siga os passos abaixo para rodar o dashboard em outra máquina:

1. **Abra o VSCode:**

   Abra o Visual Studio Code.

Clonar ou Baixar o Projeto
Baixe o código do projeto ou clone o repositório do GitHub (se aplicável).

Estrutura dos Arquivos
Certifique-se de que os arquivos do projeto estejam organizados da seguinte forma:

    - data_registros.xlsx -------   # Arquivo de dados em Excel
    - dashboard.py      ---------     # Código do dashboard

2. **Abra o Terminal:**

   Abra o terminal do VSCode. Você pode fazer isso indo para o menu superior e selecionando `Terminal` -> `Novo Terminal`.
3. **Crie o Ambiente Virtual:**
   1°

```
pip install virtualenv
```

Use o comando python -m venv para criar o ambiente virtual.
Você pode substituir nome_do_ambiente pelo nome que desejar para o seu ambiente virtual.

**RECOMENDADO - (nome_do_ambiente) = .venv**
2°

```
python -m venv nome_do_ambiente
```

4. **Ative o Ambiente Virtual:**
   caso esteja no prompt do powershell mude para o cmd (Command Prompt)
   que pode ser alterado pelo terminal
   cliclando na seta ao lado do (+) e selecionando (Command Prompt)

No Windows, utilize o comando:

```
nome_do_ambiente\Scripts\activate
```

# !Para saber se esta no ambiente virtual, note a diferença no caminho do arquivo no terminal

**Desativado:**

```
C:\Users\Usuário\Desktop\dash_python>
```

**Ativo:**

```
(venv) C:\Users\Usuário\Desktop\dash_python>
```

# IMPORTANTE: execute todos os comandos apartir deste ponto dentro do ambiente virtual

5.**Instale Dependências:**

```
pip install pandas streamlit folium streamlit_folium plotly openpyxl
```

6. Executar o Código
   Abra um terminal ou prompt de comando na pasta onde o arquivo dashboard.py está localizado e execute o seguinte comando:

```
streamlit run dashboard.py
```

Isso iniciará o Streamlit e abrirá o dashboard no seu navegador padrão.
Possivelmente solicitara um email de acesso é necessario que seja preenchido.

7. Desativar o Ambiente Virtual:

Quando terminar e quiser desativar o ambiente virtual, basta digitar:

```
deactivate
```

---

---

## Funcionalidades

Filtros Interativos: Permite filtrar os dados por mês e por oceano.
Mapa de Calor: Mostra a concentração de microplásticos em diferentes localizações.
Gráficos: Inclui gráficos de barra, scatter, linha e pizza para diferentes análises dos dados.

Informações Gerais: Exibe métricas como nível médio de pH, total de microplásticos coletados e quantidade de registros.

Insights Técnicos
Mapa de Calor: Visualiza a densidade de microplásticos nas diferentes localizações. As áreas com mais concentração de microplásticos são destacadas, ajudando a identificar hotspots de poluição.

Gráficos de Barra e Scatter: Fornecem comparações visuais das quantidades de microplásticos e níveis de pH entre diferentes localizações. Esses gráficos ajudam a entender a relação entre a poluição por microplásticos e as condições ambientais.

Gráfico de Pizza: Mostra a distribuição das condições ambientais por localização, permitindo uma análise rápida das situações mais frequentes em cada oceano.

Gráfico de Linha: Apresenta a evolução temporal da quantidade média de microplásticos coletados, facilitando a análise de tendências ao longo do tempo.

Métricas Gerais: Os cards fornecem uma visão geral rápida e agregada dos principais indicadores, facilitando a tomada de decisões e a interpretação dos dados filtrados.

Este dashboard oferece uma plataforma abrangente para monitoramento e análise da poluição por microplásticos nos oceanos, suportando decisões baseadas em dados para iniciativas de conservação ambiental.
