#2 Tipos de variáveis:
#Ano: Quantitativa discreta
#Times: Qualitativa ordinal
#Vitórias:Quantitativa discreta
#Derrotas: Quantitativa discreta
#Empates: Quantiativa discreta
#GolsF/S: Quantitativa discreta
#Saldo: Quantitativa discreta
#Qtd_Jogadores: Quantitativa discreta
#Idade_Media: Quantitativa discreta
#Estrangeiros: Quantitativa discreta
#Valor_total: Quantitativa discreta
#Media_Valor: quantitativa discreta

#A coluna Times possue variáveis qualitativas ordinais, pois seus valors são nomes de times e estão
#organizadas em ordem alfabética.
#As outras colunas são quantitativas discretas pois possuem valores contáveis e única que chega a ter casas decimais é a média de idade.


import pandas as pd

dados= pd.read_csv('Tabela_Clubes.csv')

print(dados.head())
print(dados.describe())