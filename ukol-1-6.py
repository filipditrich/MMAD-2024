# === Úkol 1, úloha 6 ===
# Jedná se o simulovaná data měření teploty v místnosti. Data jsou v .csv formátu.
# Obsahují hlavičku a pět sloupců. V prvním sloupci je datum, v následujících čtyřech sloupcích jsou teploty měření v jednotlivých čtyřech rozích místnosti.
# Celkem je v souboru 144 záznamů měření.
# Pokud bychom chtěli s takovými daty dále pracovat, kolik hlavních komponent (a jaké) je vhodné zvolit a proč?
# Využijte SVD rozkladu a libovolného počítačového nástroje a své argumenty podpořte výstupy těchto nástrojů.
# Nezapomeňte na úvodní transformaci dat.
import pandas as pd
import numpy as np

# načtení dat
data = pd.read_csv('room-temperature.csv')
# zahození sloupce s datem (nepotřebné pro analýzu)
data = data.drop(columns=['Date'])
# normalizace dat (odstranění průměru)
data = data - data.mean()

# SVD rozklad
U, s, V = np.linalg.svd(data, full_matrices=False)
# s = [34.54408633 16.15976563  7.69262365  6.51293724]

# výpočet vysvětlené variance
explained_variance = np.square(s) / np.sum(np.square(s))
# explained_variance = [0.76688522 0.16782361 0.03803049 0.02726068]

# zjištění počtu komponent pro 95% vysvětlené variance
components = np.argmax(np.cumsum(explained_variance) > 0.95) + 1
print(f"6) Počet komponent pro 95% vysvětlené variance: {components}")
