import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from scipy.stats import chisquare
temp_data = []
with open("data15.txt") as file:
    for data in file:
        x = eval(data)
        temp_data.append(x)

misure = np.array(temp_data)
x_medio = mean(misure)
print("media di x:" + str(x_medio))
x_std = np.std(misure, dtype=np.float64)
print("standard deviation" + str(x_std))

q25, q75 = np.percentile(misure, [25, 75])
bin_width = 2 * (q75 - q25) * len(misure) ** (-1/3)
print("larghezza bin",bin_width)
bins = round((misure.max() - misure.min())  / 0.01)
print("Numero di bin (freedman-diaconis):", bins)

chisquare(f_obs=[], ddof=3)

plt.hist(misure, bins=bins, histtype='bar', ec='black', density=True)

plt.show()
