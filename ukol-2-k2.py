# Realizujte hrubou silou nalezení největší nezávislé množiny daného grafu a následně otestujte, že je množina nezávislá.
# Následně se pokuste vylepšit řešení procházení množinami použitím sousedů vrcholu.
# Kód by měl vypadat následujícím způsobem:
# ```
# import networkx as nx
# import numpy as np
#
# G = nx.generators.small.small.petersen_graph()
#
# # získání největší nezávislé množiny hrubou silou
# max_ind_set = ...
#
# # Vytvořte algoritmus, který mírně podpořený využitím sousedství
# max_ind_set = ...
#
# # vhodně otestujte na knihovní funkci, že velikost vaší množiny odpovídá nezávislosti
# ```
# Některé hinty, které by se při zpracování mohli hodit. Sousedy vrcholu získáváme normálně
# ```
# >>> G = nx.generators.small.petersen_graph()
# >>> list(G.neighbors(0))
# [1, 4, 5]
# ```
# Pokud chceme testovat procházení, nabízí se, ne nutně, řešení pomocí nějakého rekurzivního přístupu.
import networkx as nx
import itertools


def get_max_independent_set(G):
    """
    Funkce pro nalezení největší nezávislé množiny grafu hrubou silou.
    Maximální nezávislá množina je taková množina uzlů, kde žádné dva uzly nejsou spojeny hranou,
    ale nelze přidat další uzel, aby zůstala nezávislá.
    Největší nezávislá množina je taková množina, která má největší počet uzlů.
    :param G: Graf G
    :return: Největší nezávislá množina grafu G
    """
    # inicializace (prázdné) maximální nezávislé množiny
    max_ind_set = set()
    # pro všechny možné velikosti množin
    for i in range(1, len(G.nodes) + 1):
        # pro všechny možné kombinace uzlů
        for ind_set in itertools.combinations(G.nodes, i):
            # pokud je množina nezávislá a má větší počet uzlů než dosavadní maximální množina
            if is_independent_set(G, ind_set) and len(ind_set) > len(max_ind_set):
                # nastavíme novou maximální množinu
                max_ind_set = set(ind_set)
    return max_ind_set


def is_independent_set(G, ind_set):
    """
    Funkce pro testování nezávislosti množiny.
    Množina je nezávislá, pokud žádné dva uzly nejsou spojeny hranou.
    :param G: Graf G
    :param ind_set: Množina uzlů
    :return: True pokud je množina nezávislá, jinak False
    """
    # pro všechny uzly v množině
    for node in ind_set:
        # projdeme všechny sousedy uzlu
        for neighbor in G.neighbors(node):
            # pokud je soused také v množině, množina není nezávislá
            if neighbor in ind_set:
                return False
    return True


def recursive_independent_set(G, current_set, nodes_remaining):
    """
    Funkce pro nalezení největší nezávislé množiny grafu rekurzivním přístupem.
    Algoritmus postupně prochází všechny uzly grafu a pokud je možné uzel přidat do množiny, přidá ho.
    :param G:
    :param current_set:
    :param nodes_remaining:
    :return:
    """
    # pokud již nejsou žádné uzly k procházení, vrátíme aktuální množinu
    if not nodes_remaining:
        return current_set

    # inicializace maximální množiny
    max_set = current_set
    # pro všechny uzly, které ještě nebyly zpracovány
    for node in nodes_remaining:
        # všechny sousedy uzlu
        neighbors = G.neighbors(node)
        # pokud žádný soused není v aktuální množině
        if all(neighbor not in current_set for neighbor in neighbors):
            # vytvoříme novou množinu s uzlem
            new_set = current_set.union({node})
            # rekurzivně zavoláme funkci pro další uzly
            remaining = nodes_remaining.difference(new_set).difference(set(G.neighbors(node)))
            candidate_set = recursive_independent_set(G, new_set, remaining)
            # pokud je nová množina větší než dosavadní maximální množina
            if len(candidate_set) > len(max_set):
                # nastavíme novou maximální množinu
                max_set = candidate_set

    return max_set


def log_perf(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        exec_time = round((time.time() - start) * 1000, 2)
        print(f"[{func.__name__}] took {exec_time} ms")
        return result

    return wrapper


G = nx.generators.small.petersen_graph()
# G = nx.generators.barbell_graph(5, 0)
# G = nx.generators.small.cycle_graph(5)
# brute force
brute_max_ind_set = log_perf(get_max_independent_set)(G)
print(f"[brute] Set: {brute_max_ind_set}, Length: {len(brute_max_ind_set)}, Is independent: {is_independent_set(G, brute_max_ind_set)}")
# confirm via networkx
nx_max_ind_set = log_perf(nx.algorithms.approximation.maximum_independent_set)(G)
print(f"[nx] Set: {nx_max_ind_set}, Length: {len(nx_max_ind_set)}, Is independent: {is_independent_set(G, nx_max_ind_set)}")
# improved with neighbors
recursive_max_ind_set = log_perf(recursive_independent_set)(G, set(), set(G.nodes))
print(f"[recursive] Set: {recursive_max_ind_set}, Length: {len(recursive_max_ind_set)}, Is independent: {is_independent_set(G, recursive_max_ind_set)}")
# assert
assert len(brute_max_ind_set) == len(nx_max_ind_set)
assert len(recursive_max_ind_set) == len(nx_max_ind_set)
