
def dyanmic_programming_algorithm_approach(Proposals, Money):
    return 2


# Subset-Sum(Proposals, Money)
#     Array M[0 . . . len(proposals), 0 . . .Money]
#     Initialize M[0, Money]= 0 for each w = 0, 1, . . . , W
#     For i = 1, 2, . . . , len(proposals)
#         For w = 0, . . . , Money
#         If w < proposals[cost]:
#             M(i, w) = M(i − 1, w).
#         Else:
#             M(i, w) = max(M(i − 1, w), proposals["quality"] + M(i − 1, w − proposals[cost"]))
#         Endfor
#     Endfor
#     Return M[n, W]


# function prob1Backtrack(DP, Q, F, budget)
#     maxFundableSubset = []
#     currBudget = budget
#     for i in [n - 1, n - 2, ..., 0] do
#         if DP[i, currBudget - F[i]] + Q[i] >= DP[i - 1, currBudget] then
#             maxFundableSubset.append(i)
#             currBudget -= F[i]
#             end if
#     end for
#     return maxFundableSubset
