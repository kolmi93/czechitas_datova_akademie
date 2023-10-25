import pandas as pd
import seaborn as sns
from scipy import stats
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

data = pd.read_csv("Student_Marks.csv")

# popis datasetu
print(data.head())
# graf 
# sns.scatterplot(data, x="time_study", y= "Marks")
# plt.show()

# výpočet korelace - ukazuje že korelace mezi časem studia a známkami je silná -> 94.254 %
# print(data.corr())

print(stats.normaltest(data["time_study"]))
# výsledek je: 2.9015838402429474e-06 -> p hodnota je malé číslo - je menší než 0.05 -> zamítáme nulovou hypotézu

sns.histplot(data, x="time_study", kde=True, bins=25)
plt.show()
# rozložení grafu neodpovídá normálnímu rozdělení.

print(stats.normaltest(data["Marks"]))
# výsledek je: 0.003414494382329425 -> p hodnota je opět malé číslo - hypotéza se zamítá