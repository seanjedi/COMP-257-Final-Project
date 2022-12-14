import os

import psutil


def dyanmic_programming_algorithm_approach(Proposals, Money):
    # This is the dynamic programming algorithm approach
    prop_length = len(Proposals)
    m_array = [[0 for _ in range(Money + 1)] for _ in range(prop_length + 1)]
    for i in range(prop_length+1):
        proposal = Proposals[i-1]
        for w in range(Money+1):
            if i == 0 or w == 0:
                m_array[i][w] = 0
            elif w >= proposal["cost"]:
                m_array[i][w] = max(m_array[i - 1][w], proposal["quality"] +
                                    m_array[i - 1][w - proposal["cost"]])
            else:
                m_array[i][w] = m_array[i-1][w]
    print("\t\tThis is how much MiB Dynamic Programming Approach is taking: ",
          psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    return m_array[prop_length][Money]
