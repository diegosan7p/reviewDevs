import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('developers.csv')
age = data["age"]
avg = age.mean()
print(f"A média de idade dos programadores é de {avg:.0f} anos")

data_grouped = data.groupby("programming language")["programming language"].count().reset_index(name="count")
idMax = data_grouped['count'].idxmax()
idMin = data_grouped['count'].idxmin()
languageMax = data_grouped['programming language'][idMax]
languageMin = data_grouped['programming language'][idMin]

print(f"A linguagem mais utilizada é {languageMax}")
print(f"A linguagem menos utilizada é {languageMin}")

plt.bar(data_grouped["programming language"], data_grouped["count"])
plt.title("programming language")
plt.show()
