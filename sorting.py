import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(cisla):
    cisla = cisla.copy()

    for pozice_ukladani in range(len(cisla)):
        min_index = pozice_ukladani
        for pozice_prochazeni in range(pozice_ukladani + 1, len(cisla)):
            if cisla[pozice_prochazeni] < cisla[min_index]:
                min_index = pozice_prochazeni

        cisla[pozice_ukladani], cisla[min_index] = cisla[min_index], cisla[pozice_prochazeni]
    return cisla

import matplotlib.pyplot as plt

# def bubble_sort(cisla):
#     cisla = cisla.copy()
#
#     for serazeno_od_konce in range(len(cisla)):
#         for pozice_porovnani in range(len(cisla) - 1 - serazeno_od_konce):
#             index_highlight1 = j
#             index_highlight2 = j + 1
#             colors = ["steelblue"] * len(values)
#             colors[index_highlight1] = "tomato"
#             colors[index_highlight2] = "tomato"
#             plt.clf()
#             plt.bar(range(len(values)), values, color=colors)
#             plt.title("Bubble Sort")
#             plt.pause(0.1)
#
#             if cisla[pozice_porovnani] > cisla[pozice_porovnani + 1]:
#                 cisla[pozice_porovnani], cisla[pozice_porovnani + 1] = cisla[pozice_porovnani]
#     plt.ion()
#     plt.show()
#     return cisla

def bubble_sort(cisla):
    cisla = cisla.copy()
    for serazeno_od_konce in range(len(cisla)):
        has_changed = False
        print(serazeno_od_konce)
        for pozice_porovnani in range(len(cisla) - 1 - serazeno_od_konce):
            if cisla[pozice_porovnani] > cisla[pozice_porovnani + 1]:
                has_changed = True
                cisla[pozice_porovnani], cisla[pozice_porovnani + 1] = cisla[pozice_porovnani]
        if not has_changed:
            break
    return cisla

