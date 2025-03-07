
import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('Tabela_Clubes.csv')

dados= pd.DataFrame(dados)

#print(dados['Clubes'].value_counts())
qnt_participacoes= pd.DataFrame(dados['Clubes'].value_counts())
qnt_participacoes= qnt_participacoes.reset_index()
#qnt_participacoes= qnt_participacoes.sort_values(by='Clubes', ascending= True)

qnt_participacoes.columns=['Clubes', 'Participações']
print(qnt_participacoes)

plt.figure(figsize=(12, 5))
plt.xlabel('Times')
plt.ylabel('Paticipações')
plt.bar(qnt_participacoes['Clubes'], qnt_participacoes['Participações'])
#plt.show()