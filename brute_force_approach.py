from itertools import chain, combinations


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
    import os
    import psutil
    print("\t\tThis is how much MiB Brute Force is taking: ",
          psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    return output_quality


# Old Code
# def powerset_raw(s):
#     x = len(s)
#     masks = [1 << i for i in range(x)]
#     for i in range(1 << x):
#         yield [ss for mask, ss in zip(masks, s) if i & mask]

# def money_brute_force_solution_first_attempt(Proposals, Money):
#     subsets = []
#     output_quality = 0
#     output_subset = []
#     subsets = subsets[0]
#     if len(Proposals) == 0:
#         return output_subset, output_quality
#     elif len(Proposals) == 1:
#         subsets.append(Proposals[0])
#     else:
#         for i, _ in enumerate(Proposals):
#             # Get a list that is just i by itself
#             subsets.append([Proposals[i]])
#             for j, _ in enumerate(Proposals, start=i+1):
#                 # Get a list that is evey permutation of i and everything after i
#                 # IE [1,2,3], [1,3], [2,3]
#                 subset = [Proposals[i]]
#                 start_j = j
#                 while start_j < len(Proposals):
#                     subset.append(Proposals[start_j])
#                     start_j += 1
#                 subsets.append(subset)
#     for i, _ in enumerate(subsets):
#         sumCost = 0
#         quality = 0
#         for grants in subsets[i]:
#             sumCost += grants["cost"]
#             quality += grants["quality"]
#         if sumCost <= Money and quality > output_quality:
#             output_quality = quality

#     return output_quality
