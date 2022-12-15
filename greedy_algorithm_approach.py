import os

import psutil


def money_greedy_solution(proposals, Money):
    # In the final code, I will implement this by utilizing two mergesorts, hence this would be O(2logN)
    proposals = sorted(sorted(
        proposals, key=lambda x: x["cost"]), key=lambda x: x["quality"], reverse=True)
    i = 0
    output_quality = 0
    output_subset = []
    while (Money > 0 and i < len(proposals)):
        if (Money > proposals[i]["cost"]) and (proposals[i]["quality"] > 0):
            output_quality += proposals[i]["quality"]
            output_subset.append(proposals[i])
            Money -= proposals[i]["cost"]
        i += 1
    print("\t\tThis is how much MiB Brute Force is taking: ",
          psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    return output_quality
