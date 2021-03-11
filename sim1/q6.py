import numpy as np
import matplotlib.pyplot as plt

z = []
for counter in range(10000):
    z.append(np.random.randint(1, 7) + np.random.randint(1, 7))

print(np.mean(z))

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.hist(z, bins=11, density=True)

plt.title("Resultados")
plt.xlabel("Valor")
plt.ylabel("Densidade de probabilidade")

plt.show()
