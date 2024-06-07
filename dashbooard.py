import folium
from folium.plugins import HeatMap
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import plotly.express as px

# Configuração inicial do Streamlit
st.set_page_config(layout="wide")

# Carregar dados (exemplo com dados fictícios)
df = pd.read_excel("data_registros.xlsx")
df["Data"] = pd.to_datetime(df["Data"])
df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Função para obter as coordenadas específicas de cada oceano
def localizacao(local):
    coordenadas = {
        "Pacifico_Sul": [-20.0, -50.0],
        "Atlantico_Norte": [35.0, -45.0],
        "Indico": [-20.0, 70.0],
        "Pacifico_Norte": [15.0, -150.0],
        "Atlantico_Sul": [-10.0, -30.0]
    }
    return coordenadas.get(local, [-20.0, -110.0])

# Sidebar para seleção de filtros
month = st.sidebar.selectbox("Mês", ["Todos"] + df["Month"].unique().tolist())
op_ocean = st.sidebar.selectbox("Oceanos", ["Todos"] + df["Localizacao"].unique().tolist())

# Botão para limpar filtros
if st.sidebar.button("Limpar Filtros"):
    month = "Todos"
    op_ocean = "Todos"

# Filtragem dos dados
if month != "Todos":
    df_filtered_date = df[df["Month"] == month]
else:
    df_filtered_date = df

if op_ocean != "Todos":
    df_filtered_ocean = df[df["Localizacao"] == op_ocean]
else:
    df_filtered_ocean = df

# Determinar a localização do mapa com base no filtro
loc = localizacao(op_ocean) if op_ocean != "Todos" else [-20.0, -110.0]

# Criação do mapa base
baseMap = folium.Map(
    width="100%",  # largura da tela
    height="100%",  # altura da tela
    location=loc,  # localização inicial
    zoom_start=4
)

# Adicionando HeatMap ao mapa
HeatMap(data=df_filtered_date[['Latitude', 'Longitude', 'media_micro_plastico']].values, radius=15).add_to(baseMap)

# Função para adicionar círculos ao mapa
def plotMap(df):
    for i in range(len(df)):
        folium.Circle(
            location=[df.iloc[i]["Latitude"], df.iloc[i]["Longitude"]],
            color="#0000000",
            fill=True,
            fill_color="#00A1B3",
            tooltip=(
                f"<li><bold> Localização: {df.iloc[i]['Localizacao']}"
                f"<li><bold> Condicao: {df.iloc[i]['Condicao']}"
                f"<li><bold> Nivel Do PH: {df.iloc[i]['Nivel_de_pH']}"
                f"<li><bold> Qtd Kg coletados: {df.iloc[i]['media_micro_plastico']}"
            )
        ).add_to(baseMap)
    return baseMap


st.subheader(f'Analisando {op_ocean if op_ocean != "Todos" else "Todos"}')
# Cards com informações gerais
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Nível Médio de pH", value=f"{df_filtered_ocean['Nivel_de_pH'].mean():.2f}")

with col2:
    st.metric(label="Total de Microplásticos Coletados", value=df_filtered_ocean['media_micro_plastico'].sum())

with col3:
    st.metric(label="Quantidade de Registros", value=len(df_filtered_ocean))

# Plotando o mapa e gráfico de pizza lado a lado
col5, col6  = st.columns(2)
with col5:
    st.subheader('Mapa de Calor')
    folium_static(plotMap(df_filtered_date))

with col6:
    st.subheader('Distribuição das Condições por Localização')
    condicao_counts = df_filtered_ocean['Condicao'].value_counts().reset_index()
    condicao_counts.columns = ['Condicao', 'counts']
    fig4 = px.pie(condicao_counts, names='Condicao', values='counts', title='Distribuição das Condições por Localização')
    st.plotly_chart(fig4)

# Gráfico de evolução mensal em uma única coluna
col7 = st.columns(1)
with col7[0]:
    st.subheader('Evolução Mensal da Coleta de Microplásticos')
    df_filtered_ocean['YearMonth'] = df_filtered_ocean['Data'].dt.to_period('M')
    monthly_data = df_filtered_ocean.groupby('YearMonth').agg({'media_micro_plastico': 'mean'}).reset_index()
    monthly_data['YearMonth'] = monthly_data['YearMonth'].astype(str)
    fig3 = px.line(monthly_data, x='YearMonth', y='media_micro_plastico', title=f'Evolução Mensal da Coleta de Microplásticos - {op_ocean if op_ocean != "Todos" else "Todos"}', labels={'media_micro_plastico': 'Média de Microplásticos', 'YearMonth': 'Mês'})
    st.plotly_chart(fig3)

# Gráficos de barra e scatter lado a lado
col7, col8 = st.columns(2)

with col7:
    st.subheader('Média de Microplásticos por Localização')
    fig1 = px.bar(df_filtered_ocean, x="Localizacao", y="media_micro_plastico", color="Localizacao", title="Média de Microplásticos por Localização")
    st.plotly_chart(fig1)

with col8:
    st.subheader('Nível de pH por Localização')
    fig2 = px.scatter(df_filtered_ocean, x="Nivel_de_pH", y="Localizacao", size="media_micro_plastico", color="Condicao", title="Nível de pH por Localização")
    st.plotly_chart(fig2)
