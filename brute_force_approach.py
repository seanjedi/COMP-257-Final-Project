
def money_brute_force_solution(Proposals, Money):
    return 0
    subsets = []
    OQuality = 0
    OSubset = []
    if len(Proposals) == 0:
        return OSubset, OQuality
    elif len(Proposals) == 1:
        subsets.append(Proposals[0])
    else:
        for i, _ in enumerate(Proposals):
            # Get a list that is just i by itself
            subsets.append(Proposals[i])
            for j, _ in enumerate(Proposals, start=i+1):
                # Get a list that is evey permutation of i and everything after i
                # IE [1,2,3], [1,3]
                subset = Proposals[i] + Proposals[:j]
                subsets.append(subset)
    
    for i, _ in enumerate(subset):
        sumCost = 0
        quality = 0
        for grants in subset[i]:
            sumCost += grants["cost"]
            quality += grants["quality"] 
        if sumCost <= Money and quality > OQuality:
            OQuality = quality
            OSubset = subset[i]
    return OSubset, OQuality