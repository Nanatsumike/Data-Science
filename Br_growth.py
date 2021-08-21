# Crescimento da população brasileira desde 1980 até 2016
# DataSus

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title("Crescimento da população Brasileira 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")

plt.plot(x, y)
plt.bar(x, y)

plt.show()
