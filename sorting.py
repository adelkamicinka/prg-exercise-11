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


cisla = [5, 1, 4, 2, 8]
print("Původní seznam:", cisla)
print("Seřazený seznam:", selection_sort(cisla))