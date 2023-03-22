import sympy as smp
from scipy.integrate import quad
import matplotlib.pyplot as pl
import numpy as np

z = np.linspace(0.0001, 2, 100)

def f(z, om_m, om_r, om_l, om_k):
    return 1 / (-(om_k) * (1 + z) ** 2 + om_m * (1 + z) ** 3 + om_r * (1 + z) ** 4 + om_l) ** smp.Rational(1, 2)


def p(z):
    integral = quad(f, 0, z, args=(0.303, 8.8443*10**-5, 0.6969, 0))
    l_m = float(2.99 * 10 ** 8) * float(3.24 * 10 ** -23) * (1 + z) * integral[0] / float(2.2197 * 10 ** -18)
    lm_1 = float(5 * smp.log(l_m, 10) + 25)
    return lm_1

luminosity_distance = list(map(p, z))
print(luminosity_distance)
print(len(luminosity_distance))
x = np.linspace(0.0001, 2, 100)
y = luminosity_distance
pl.plot(x, y, c="black", linewidth=2)
pl.xlabel('redshift')
pl.ylabel('distance modulus')
pl.title('distance modulus versus redshift')
pl.show()
