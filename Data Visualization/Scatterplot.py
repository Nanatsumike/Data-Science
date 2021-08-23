import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 6, 4, 8, 1]

# Scatterplot - Grafico de dispersão
titulo = "Gráfico de dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.scatter(x, y, label="Meus pontos", color='red')
plt.plot(x, y)
plt.legend()

#plt.savefig('Figura001.png', dpi=300)
plt.show()
