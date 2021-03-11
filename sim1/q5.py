import numpy as np
import matplotlib.pyplot as plt
from scipy import special as sp

# https://mail.python.org/pipermail/scipy-dev/2016-February/021252.html
def qfunc(arg):
    return 0.5 - 0.5 * sp.erf(arg / 1.414)


samples = 2 * (np.random.randn(1, 10000)[0]) + 2
mean_samples = np.mean(samples)
std_samples = np.std(samples)
z1 = (2 - mean_samples) / std_samples
z2 = (6 - mean_samples) / std_samples
probability = qfunc(z1) - qfunc(z2)
print(probability)

probability_less_than_a = 1 - qfunc(z1)
print("P(X<a):", probability_less_than_a)

probability_higher_than_b = qfunc(z2)
print("P(X>b):", probability_higher_than_b)


probability_total = probability + probability_higher_than_b + probability_less_than_a
print("P(X<a) + P(a<X<b) + P(X>b):", probability_total)
