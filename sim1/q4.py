import numpy as np
import matplotlib.pyplot as plt

samples = 2 * (np.random.randn(1, 10000)[0]) + 2

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.hist(
    samples,
    bins="auto",
    density=True,
)

plt.title("Resultados")
plt.xlabel("Valor")
plt.ylabel("Densidade de probabilidade")

plt.show()
