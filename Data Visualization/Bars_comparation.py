import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [5, 6, 4, 8, 1]

x2 = [2, 4, 6, 8, 10]
y2 = [7, 6, 5, 9, 2]

titulo = "Gráfico de barras 2"
eixoX = "Eixo X"
eixoY = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# Legenda do grafico
plt.bar(x1, y1, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()

plt.show()
