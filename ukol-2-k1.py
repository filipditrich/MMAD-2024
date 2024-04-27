# Naprogramujte algoritmus pro testování isomorfismu grafů hrubou silou a otestujte to na páru příkladech
# grafů s využitím knihovní funkce pro testování isomorfismu. K tomu několik hintů. Nejprve schéma programu.
# To by mělo bez problémů otestovat následující:
# ```
# import networkx as nx
# import numpy as np
# G = nx.generators.small.cycle_graph(5)
# H = nx.complement(nx.generators.small.cycle_graph(5))
# # your code returning 'my_isom' boolean
# my_isom = ...
# # testing library
# nx_isom = nx.is_isomorphic(G, nx.complement(H))
# # check my code
# nx_isom == my_isom
# ```

# Lze předpokládat, že vrcholy grafu jsou reprezentovány jako pole čísel [0, 1, 2, . . . , n], což lze získat následujícím voláním:
# ```
# G.nodes()
# >>> list(G.nodes)
# [0, 1, 2, 3, 4]
# ```

# Navíc pomohou různé funkce pythonu na generování permutací a množin, viz:
# ```
# >>> import itertools
# >>> A = [0, 1, 2, 3, 4]
# >>> list(itertools.permutations(A)) # vˇsechny permutace
# [(0, 1, 2, 3, 4),
# (0, 1, 2, 4, 3),
# (0, 1, 3, 2, 4),
# ...
# (4, 3, 2, 0, 1),
# (4, 3, 2, 1, 0)]
# >>> list(itertools.combinations(A,2)) # vˇsechny p´ary
# [(0, 1),
# (0, 2),
# (0, 3),
# ...
# (2, 4),
# (3, 4)]
# ```
import networkx as nx
import itertools

import numpy as np

def isomorphism(G, H):
    """
    Funkce pro testování isomorfismu grafů hrubou silou.
    Funguje na principech hrubé síly, kde se všechny možné permutace uzlů grafu G porovnají s uzly grafu H.
    :param G: Graf G
    :param H: Graf H
    :return: True pokud jsou grafy isomorfní, jinak False
    """
    if len(G.nodes) != len(H.nodes):
        return False

    # získání všech permutací uzlů grafu G
    perms = itertools.permutations(list(G.nodes))
    for perm in perms:
        # vytvoření mapování uzlů grafu G na uzly grafu H
        # pokud všechny uzly grafu G mají svůj ekvivalent v grafu H a všechny hrany zůstanou zachovány, vrátí True
        mapping = dict(zip(G.nodes, perm))
        has_all_nodes = all([mapping[u] in H.nodes for u in G.nodes])
        has_all_edges = all([mapping[u] in H.nodes for u in G.nodes])
        if has_all_nodes and has_all_edges:
            return True
    return False


 # generate random graphs and test isomorphism
for i in range(10):
    test_n = np.random.randint(3, 10)
    test_b = np.random.randint(0, 2) == 1
    test_G = nx.generators.small.cycle_graph(test_b + test_n)
    test_H = nx.complement(nx.generators.small.cycle_graph(test_n))
    my_isom = isomorphism(test_G, nx.complement(test_H))
    nx_isom = nx.is_isomorphic(test_G, nx.complement(test_H))
    print(f"Test {i+1}: G: {test_G.nodes}, H: {test_H.nodes}")
    print(f"Vlastní: {my_isom}\nNetworkX: {nx_isom}\nÚspěch: {'Ano' if my_isom == nx_isom else 'Ne'}")
    assert my_isom == nx_isom
