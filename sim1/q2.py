import numpy as np
import matplotlib.pyplot as plt

DICE_SIDES = np.arange(1, 7, 1).tolist()
probs = [0.15, 0.15, 0.15, 0.15, 0.15, 0.25]
dice_rolls = np.array(list(np.random.choice(DICE_SIDES, p=probs) for _ in range(10000)))

normalized_dice_rolls = []
for counter in range(1, max(dice_rolls) + 1):
    normalized_dice_rolls.append(
        len(dice_rolls[dice_rolls == counter]) / len(dice_rolls)
    )


fig, ax = plt.subplots(1, 1, figsize=(8, 4))
frequency, value = np.unique(dice_rolls, return_counts=True)
ax.bar(DICE_SIDES, normalized_dice_rolls, align="center")
ax.bar(DICE_SIDES, probs, align="center", alpha=0.5)

plt.title("Resultados")
plt.xlabel("Valor da rolagem")
plt.ylabel("Frequência")

plt.show()