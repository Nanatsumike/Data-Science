import matplotlib.pyplot as plt

# Valores dos pares ordenados
x = [1, 3, 7]
y = [1, 2, 5]

# Titulo do grafico
plt.title('My First graph with python')

# Detalhes dos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Criando o grafico
plt.plot(x, y)

# Mostrando o grafico
plt.show()
