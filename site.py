# Importe as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Setando porta
st.set_option('server.port', 3000)

# Crie uma barra lateral para configurações
st.sidebar.title("Configurações")

# Crie um campo de texto para o título
title = st.sidebar.text_input("Título do Gráfico", "Gráfico de Barras")

# Carregue dados de exemplo (um DataFrame)
data = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [10, 25, 5, 30]
})

# Crie um gráfico de barras com base nos dados
fig, ax = plt.subplots()
ax.bar(data['Categoria'], data['Valores'])
plt.xlabel('Categoria')
plt.ylabel('Valores')
plt.title(title)

# Exiba o gráfico no Streamlit
st.pyplot(fig)

# Mostre os dados na tabela
st.write("Dados da Tabela:")
st.write(data)
