import matplotlib.pyplot as plt
import random as rd

vetor = []

for i in range(100):
    vetor.append(rd.randint(0, 50))

plt.boxplot(vetor)
plt.title('BoxPlot')
plt.show()
