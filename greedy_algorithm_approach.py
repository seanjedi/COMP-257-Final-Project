
def money_greedy_solution(Proposals, Money):
    return 1
    # In the final code, I will implement this by utilizing two mergesorts, hence this would be O(2logN)
    Proposals = sorted(sorted(
        Proposals, key=lambda x: x["cost"]), key=lambda x: x["quality"], reverse=True)
    i = 0
    OQuality = 0
    OSubset = []
    while (Money > 0 and i < len(Proposals)):
        if (Money > Proposals[i]["cost"]) and (Proposals[i]["quality"] > 0):
            OQuality += Proposals[i]["quality"]
            OSubset.append(Proposals[i])
            Money -= Proposals[i]["cost"]
        i += 1
    return OSubset, OQuality
