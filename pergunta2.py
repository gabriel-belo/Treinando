#tivemos times com crescimento nos seus resultados no campeontado no decorrer do tempo
import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('Tabela_Clubes.csv')

dados= pd.DataFrame(dados)

resultados_SaoPaulo= dados.query('Clubes == "Sao Paulo"')


resultados_SaoPaulo= resultados_SaoPaulo.sort_values(by='Ano')
resultados_SaoPaulo= resultados_SaoPaulo.reset_index(drop=True)
print(resultados_SaoPaulo)