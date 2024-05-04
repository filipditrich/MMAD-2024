# Mějme stálý migrační proces obyvatel mezi Severem, Jihem, Východem a Západem,
# jehož průběh za 1 rok lze znázornit diagramem níže (desetinná čísla udávají, jaký zlomek populace se za rok přemístí po šipce do jiné oblasti).
# Na počátku je počet obyvatel ve všech oblastech 10 milionů.
# Jak bude situace rozložení populace vypadat za 10 let od počátku?
# Na kterých hodnotách se populace v jednotlivých oblastech ustálí, pokud ji budeme dostatečně dlouho sledovat?
import numpy as np

# matice přechodů
# S -> S: 0.75
# S -> J: 0.25
# J -> J: 0.25
# J -> V: 0.25
# J -> Z: 0.5
# V -> V: 0.75
# V -> J: 0.25
# Z -> Z: 0.75
# Z -> S: 0.25

# matice přechodů
P = np.array([
    # Sever -> S, J, V, Z
    [0.75, 0.25, 0, 0],
    # Jih -> S, J, V, Z
    [0, 0.25, 0.25, 0.5],
    # Východ -> S, J, V, Z
    [0, 0.25, 0.75, 0],
    # Západ -> S, J, V, Z
    [0.25, 0, 0, 0.75]
]).T

# počáteční rozložení populace
x0 = np.array([10, 10, 10, 10])

# výpočet rozložení populace za 10 let
x = x0
for _ in range(10):
    x = np.dot(P, x)  # P * x
# [13.05176735  6.66666985  6.94823265 13.33333015]
print(f"5a) Po 10 letech: {x}")

# vlastní čísla a vektory matice P
w, v = np.linalg.eig(P)
# vlastní čísla: [0.25 0.5 1. 0.75]
# vlastní vektory: [
#   [ 3.16227766e-01 -6.32455532e-01 -6.32455532e-01  7.07106781e-01]
#   [ 6.32455532e-01 -3.16227766e-01 -3.16227766e-01  4.44605073e-17]
#   [-3.16227766e-01  3.16227766e-01 -3.16227766e-01 -7.07106781e-01]
#   [-6.32455532e-01  6.32455532e-01 -6.32455532e-01  2.03628341e-15]
# ]
# print(w)
# print(v)

# vlastní vektor příslušný vlastnímu číslu 1
v1 = v[:, np.isclose(w, 1)]
# [[-0.63245553], [-0.31622777], [-0.31622777], [-0.63245553]]

# normalizace vlastního vektoru
v1 = v1 / np.sum(v1)
# [[0.33333333] [0.16666667], [0.16666667], [0.33333333]]
print(f"5b) Ustálená populace: {v1}")
