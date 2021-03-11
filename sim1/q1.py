import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(0)
DICE_SIDES = np.arange(1, 7, 1).tolist()

dice_rolls = np.array(list(np.random.randint(1, 7) for _ in range(10)))
print(dice_rolls)

normalized_dice_rolls = []
for counter in range(1, max(dice_rolls) + 1):
    normalized_dice_rolls.append(
        len(dice_rolls[dice_rolls == counter]) / len(dice_rolls)
    )

ideal_pdf_values = np.full((1, 6), 1 / 6)[0]

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
frequency, value = np.unique(dice_rolls, return_counts=True)
# ax.bar(frequency, value, align="center")
ax.bar(DICE_SIDES, normalized_dice_rolls, align="center")
ax.bar(DICE_SIDES, ideal_pdf_values, align="center", alpha=0.7)

plt.title("Resultados")
plt.xlabel("Valor da rolagem")
plt.ylabel("Frequência")


plt.show()
