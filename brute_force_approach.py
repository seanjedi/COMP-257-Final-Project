import os
from itertools import chain, combinations

import psutil


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def money_brute_force_solution(Proposals, Money):
    subsets = []
    output_quality = 0
    subsets = list(powerset(Proposals))
    for i, _ in enumerate(subsets):
        sumCost = 0
        quality = 0
        for grants in subsets[i]:
            sumCost += grants["cost"]
            quality += grants["quality"]
        if sumCost <= Money and quality > output_quality:
            output_quality = quality

    print("\t\tThis is how much MiB Brute Force is taking: ",
          psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    return output_quality
