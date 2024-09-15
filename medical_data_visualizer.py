# --- Agrupamento de dados por ano, mês e origem, preenchendo meses faltantes com zero ---

import pandas as pd

# Exemplo de dados com valores faltantes
data = {'year': [2020, 2020, 2021, 2021], 'month': [1, 2, 1, 2], 'origin': ['A', 'B', 'A', 'B'], 'value': [10, 20, 15, 25]}
df = pd.DataFrame(data)

# Criando uma série de todas as combinações possíveis de ano, mês e origem
full_index = pd.MultiIndex.from_product([df['year'].unique(), df['month'].unique(), df['origin'].unique()], names=['year', 'month', 'origin'])

# Reindexando o DataFrame para incluir os meses faltantes e preenchendo com 0
df_full = df.set_index(['year', 'month', 'origin']).reindex(full_index, fill_value=0).reset_index()

# Visualizando o resultado
print("Agrupamento de Dados com Meses Faltantes Preenchidos:")
print(df_full)


# --- Gráfico Seaborn sem sombra ao redor das barras de erro (errorbar) ---

import seaborn as sns
import matplotlib.pyplot as plt

# Exemplo de dataset
data = sns.load_dataset("tips")

# Gráfico Seaborn sem sombra ao redor das barras de erro (errorbars)
sns.barplot(x="day", y="total_bill", data=data, errorbar=None)

# Mostrando o gráfico
plt.title("Gráfico de Barras sem Errorbar")
plt.show()


# --- Adicionar variância nas estatísticas descritivas de um DataFrame ---

# Exemplo de DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# Estatísticas descritivas
desc_stats = df.describe()

# Adicionando a variância
desc_stats.loc['variance'] = df.var()

# Exibindo o resultado
print("\nEstatísticas Descritivas com Variância:")
print(desc_stats)


# --- Proposta de Moodboard para Loja de Doces ---

def moodboard_loja_de_doces():
    proposta = """
    # Moodboard - Proposta de Loja de Doces

    ## Conceito
    - Um espaço alegre e vibrante que transmite nostalgia e doçura.
    - Cores pastel como rosa, azul e amarelo predominantes.
    - Decoração inspirada em doces clássicos como pirulitos, cupcakes e algodão-doce.

    ## Paleta de Cores
    - Rosa bebê (#FADADD)
    - Azul céu (#B0E0E6)
    - Amarelo claro (#FFFACD)
    - Branco puro (#FFFFFF)

    ## Elementos Visuais
    - Balões e banners festivos.
    - Prateleiras com embalagens de doces retrô.
    - Luminárias em formato de sorvetes e pirulitos.
    - Uma vitrine colorida cheia de macarons, donuts e cupcakes.

    ## Tipografia
    - Fontes redondas e divertidas.
    - Estilo manuscrito ou com letras grandes e chamativas.

    ## Atmosfera
    - Músicas alegres e infantis ao fundo.
    - Aroma de baunilha e canela no ar.
    - Área interativa para crianças, com jogos e atividades.
    """
    print(proposta)

# Exibir o moodboard
moodboard_loja_de_doces()
