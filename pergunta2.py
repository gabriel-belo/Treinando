#tivemos times com crescimento nos seus resultados no campeontado no decorrer do tempo
import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('Tabela_Clubes.csv')

dados= pd.DataFrame(dados)

dados_SaoPaulo= dados.query('Clubes == "Sao Paulo"')

resultados_SaoPaulo= dados_SaoPaulo



resultados_SaoPaulo= resultados_SaoPaulo.sort_values(by='Ano')
resultados_SaoPaulo= resultados_SaoPaulo.reset_index(drop=True)
print(resultados_SaoPaulo)
plt.figure(figsize= (10, 10))

plt.subplot(1, 2, 1)
plt.title('Posição por ano no Brasileirão')
plt.xlabel('Ano')
plt.ylabel('Posição')
plt.plot(resultados_SaoPaulo['Ano'],resultados_SaoPaulo['Pos.'], marker= 'o')
plt.gca().invert_yaxis() #invertendo os números no eixo Y, fazendo com que apareçam do maior para o menor


plt.subplot(1, 2, 2)
plt.title('Valor do time por Ano')
plt.xlabel('Ano')
plt.ylabel('Valor do time em Reais')
plt.plot(resultados_SaoPaulo['Ano'], resultados_SaoPaulo['Valor_total'], marker= 'o')

plt.show()

print(resultados_SaoPaulo['Valor_total'])