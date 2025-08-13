#AULA 01 - MANIPULANDO DADOS COM PANDAS
import pandas as pd

#Importando a base de dados:
df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')
df.head()

#Visualizando as informações do df
df.info()
df.describe()

#Atributo que exibe uma 'tupla' (Linhas, colunas)
df.shape
linhas, colunas = df.shape[0], df.shape[1]
print('linhas: ', linhas)
print('colunas: ', colunas)

#Visualizando as 'cl' do 'df'
df.columns

# Traduzindo os nomes das colunas:
#Indentar Shift + Alt + F
renomear_colunas = {
    'work_year':'ano',
    'experience_level':'senhoridade',
    'employment_type' : 'contrato',
    'job_title': 'cargo',
    'salary' : 'salario',
    'salary_currency' : 'moeda',
    'salary_in_usd' : 'usd',
    'employee_residence' : 'residencia',
    'remote_ratio' : 'remoto',
    'company_location' : 'empresa',
    'company_size' : 'tamanho_empresa'
}

#Atributo
#inplace=True → altera diretamente o original (não cria cópia, não retorna nada)
df.rename(columns=renomear_colunas, inplace=True)
df.columns

#Renomeando e visualizando as categorias:
senhoridade = {
    'SE' : 'Senior',
    'MI' : 'Pleno',
    'EN' : 'Junior',
    'EX' : 'Executivo'
}

#replace é um método (função) do Pandas que substitui valores por outros
df['senhoridade'] = df['senhoridade'].replace(senhoridade)
df['senhoridade'].value_counts()

contrato = {
    'FT' : 'Periodo_Integral',
    'CT' : 'Contrato_Temporario',
    'Meio_Periodo' : 'Meio_Período',
    'FL' : 'Freelance' 
}

df['contrato'] = df['contrato'].replace(contrato)
df['contrato'].value_counts()

remoto = {
    0 : 'Presencial',
    100 : 'Remoto',
    'Hibrido' : 'Híbrido'
}

df['remoto'] = df['remoto'].replace(remoto)
df['remoto'].value_counts()

tamanho_empresa = {
    'M' : 'Médio',
    'L' : 'Grande',
    'S' : 'Pequeno'
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()

df.head(15)
df.describe(include='object')

#AULA 02 - APRENDA A LIMPAR E PREPARAR OS DADOS
df.isnull()
df.head()

#Comando para somar os valores nulos entre as categorias
df.isnull().sum()

#Verificando os ano que estão presentes no df
df['ano'].unique()

#Verificando quais são os dados: NaN
df[df.isnull().any(axis=1)]

#INFORMAÇÕES ADICIONAIS:
#Chamadas de Função e Operações 'Mat' são utilizados os parentese ()
#Criação de dicionário ou Listas usar chaves []

#Removendo as informações nulas, criando um df 'novo' pra guardar os dados tratados 
df_limpo = df.dropna()
df_limpo


df_limpo.isnull().sum()

df_limpo.info()
#Próximo passo é mudar o tipo de dado de float pra int (ano)

from numpy import astype, int64

#Modificando o tipo de dado da coluna 'ano'
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
df_limpo.head(10)

#Aula 3 - Visualizando os Dados

df_limpo['senhoridade'].value_counts()

#Gráfico
df_limpo['senhoridade'].value_counts().plot(kind='bar',title='distribuicao de senhoridade')

#Importando bibliotecas
!pip install seaborn 
!pip install matplotlib

sns.barplot(data=df_limpo,x='senhoridade',y='usd')

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo,x='senhoridade', y='usd')
plt.title('Salario Medio por Senhoridade')
plt.xlabel('Nivel de Senhoridade')
plt.ylabel('Salario Medio Anual(USD)')
plt.show()

df_limpo.groupby('senhoridade')['usd'].mean().sort_values(ascending=False)

order = df_limpo.groupby('senhoridade')['usd'].mean().sort_values(ascending=False).index
order

#Visualizando o gráficos de barras estatísticos
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo,x='senhoridade', y='usd', order=orden)
plt.title('Salario Medio por Senhoridade')
plt.xlabel('Nivel de Senhoridade')
plt.ylabel('Salario Medio Anual(USD)')
plt.show()

#Visualizando função do Seaborn para criar histogramas e, opcionalmente, gráficos de densidade
#No figsize os parametros passados são 'altura e largura' nessa ordem.
plt.figure(figsize=(10,5))
#bins 'larguras das barras'
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title('Distribuição dos Sálario anuais')
plt.xlabel('Sálario em USD')
plt.ylabel('Frequência')

#Visualizando em formato de Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot Salário')
plt.xlabel('Sálario em USD')
plt.show()

#Gráfico por senhoridade em Boxplot
order_senhoridade = ['Executivo', 'Senior','Pleno','Junior']
plt.figure(figsize=(8,5))
#Inserindo cor nas categorias através do 'pallete' da biblioteca sns
sns.boxplot(x='senhoridade', y='usd', data=df_limpo, order=order_senhoridade, palette='Set2', hue='senhoridade')
plt.title('Boxplot Sálario por Senhoridade')
plt.xlabel('Sálario em USD')
plt.show()


!pip install plotly

import plotly.express as px

!pip install nbformat


# Criando a tabela com a média salarial por senhoridade
senhoridade_media_salario = df_limpo.groupby('senhoridade')['usd'].mean().sort_values(ascending=False).reset_index()

# Criando o gráfico de pizza
fig = px.bar(senhoridade_media_salario,
             x='senhoridade',
             y='usd',
             title='Média Salarial por Senhoridade',
             labels={'senhoridade': 'Nível de Senhoridade', 'usd': 'Média Salarial Anual (USD)'})

#Isso vai abrir o gráfico como página HTML no seu navegador
fig.show()

