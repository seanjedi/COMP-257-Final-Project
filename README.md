# COMP-257-Final-Project - Sean Malloy

This is the final project for COMP-257.
Here I will be implementing the Knapsack Problem solutions using Brute Force, a greedy algorithm, and a Dynamic Programming Algorithm.

## Table of Contents

* [Question](Question)
  * [inputs and outputs](#inputs-and-outputs)
* [Brute Force Approach](#brute-force-approach)
  * [Approach](#approach)
  * [PseudoCode](#pseudocode)
  * [Big Oh Analysis](#big-oh-analysis)
* [Greedy Approach](#greedy-approach)
  * [Approach](#approach-1)
  * [PseudoCode](#pseudocode-1)
  * [Big Oh Analysis](#big-oh-analysis-1)
* [Dynamic Programming Approach](#dynamic-programming-approach)
  * [Approach](#approach-2)
  * [PseudoCode](#pseudocode-2)
  * [Big Oh Analysis](#big-oh-analysis-2)

## Question

We have a knapsack problem in which we want to optimize the quality ratings we have for a list of grants that are requesting X amount of funds. Given a certain amount of money, how would you find the subset of grants that maximize the sum of quality ratings while still being within budget. In this problem, quality can be a negative number.

### inputs and outputs

**Inputs**
*Proposals*: Dictionary of proposals
The dictionary would be structured as the following

``` python
proposals = [
  {"cost": 100, "quality": 2},
  {"cost": 20, "quality": 5},
  {"cost": 10, "quality": 10},
  ...
]
```

cost: The amount of money to fund a certain grant (cost >=0 )
quality: The amount of quality a grant will provide (float)

*Money*: Money available to fund grants (Money >=0 )

**Outputs**
*OSubset*: Subset of grants that maximize the quality rating
*OQuality*: Optimal quality score obtained

## Brute Force Approach

### Approach

The brute force approach to this problem would be one in which you iterate through each grant, and create a list of each permutation of subroups of grants. Afterwards, you would go through each permutation, and check which subgroup would give you the highest quality rating without going over the available money(M).

#### PseudoCode

``` python
def money_brute_force_solution(Proposals, Money):
  subsets = []
  OQuality = 0
  OSubset = []
  if len(Proposals) == 0:
    return OSubset, Quality
  elif len(proposals) == 1:
    subsets.append(proposals[0])
  else:
    for i in range(len(Proposals)):
      # Get a list that is just i by itself
      subsets.append(proposals[i])
      for j in range(i+1, len(Proposals)):
        # Get a list that is evey permutation of i and everything after i
        # IE [1,2,3], [1,3]
        subset = proposals[i] + proposals[:k]
        subsets.append(subset)
  
  for i in range(len(subset)):
    sumCost = 0
    quality
    for grants in subset[i]:
      sumCost += grants["cost"]
      quality += grants["quality"] 
    if sumCost <= Money:
      if quality > OQuality:
        OQuality = quality
        OSubset = subset[i]
  return OSubset, OQuality

```

### Big Oh Analysis

This solution would be O(2<sup>N</sup>) + O(2<sup>N</sup>), where N is len(proposals)

* O(2<sup>N</sup>) coming from creating the subsets (From creating each permutation of subset from the superset, similar as going through the whole binary counting system of 000, 001, 010, etc)
* O(2<sup>N</sup>) coming from going though the final for-loop of all the permutations to get the answer. Being that there are 2<sup>N</sup> subsets created, going through all of them should take O(2<sup>N</sup>) time

So in this example, the Big-Oh of the solution would be O(2 \* 2<sup>N</sup>) since 2 is a constant, we can get rid of it.
Answer: O(2<sup>N</sup>)

### Limitations

This might take up too much memory and/or time, so when I test this, that might become an issue.

## Greedy Approach

### Approach

One greedy Approach would be to assign the largest quality score available for the subset, and go from there
Another Greedy Approach would be to assign the lowest cost grants first to try to maximize the amount of grants we can manage
My proposed Greed Approach would be to sort the array by both costs and quality, and assign the subtasks accordingly to the list. This would be a combination of the two rules above, in which we take in the tasks with the highest quality, and that are lowest cost.
The reason I propose this approach, is if we have multiple grants with the same costs, we would want to take in the ones with the lowest costs first, in case if we can, then keep going down the list until we have no more money to spend

#### PseudoCode

``` python
def money_greedy_solution(Proposals, Money):
  # In the final code, I will implement this by utilizing two mergesorts, hence this would be O(2logN)
  Proposals = sorted(sorted(Proposals, key = lambda x : x["cost"]), key = lambda x : x["quality"], reverse = True)
  i = 0
  OQuality = 0
  OSubset = []
  while(Money > 0 and i < len(Proposals)):
    if(Money > Proposals[i]["cost"]):
      if(Proposals[i]["quality"] > 0):
        OQuality += Proposals[i]["quality"]
        OSubset.append(Proposals[i])
        money -= Proposals[i]["cost"]
    i += 1
  return OSubset, OQuality

```

### Big Oh Analysis

This algorithm would take O(NlogN) time, where N is len(proposals)

* O(NlogN): It would take O(2NlogN) time to sort the Proposal array (Using something similar to Mergesort). Since 2 is a constant, we can shorten it down to O(NlogN).
* O(N): Time to find the OutputSubset would take O(N) time since it searches through the array.
  
Since O(NlogN) is the leading term (O(NlogN) >= O(N)), that is the time for this algorithm

### Limitations

This might not show optimal solutions all the time. Lets say we have the following when we only have 100 dollars [(100,100), (50,75), (50,75)]. In this case, the greedy approach would only take the first option, while the most optimal would be the two 75 options, so this would not be ideal.

## Dynamic Programming Approach

### Approach

After considering some fallacies of this previous approach, and after reading the book, I realized that this approach would not work (or be great to calculate), since it would always choose the largest subset, and does not quite consider the costs for each grant. Instead this is pretty close to what the book considers as the *knapsack problem* in which we are trying to maximize both value (quality) and weight (cost). To do this, we create a matrix of subproblems, in which we can either include a grant or not. So to say, from the book, that an optimal solution O' can be comprised of cases in which a grant is in O'.IE

* if grant NOT ∈ O', then OPT(Proposals, M) = OPT(proposals-1, M)
* if grant ∈ O', then OPT(Proposals, M) = quality<sub>Proposals</sub> + OPT(proposals-1, M-cost)

Using these two subproblems, we can formulate the following occurance:

```If w < wi then OPT(i, w) = OPT(i − 1, w).
Otherwise OPT(i, w) = max(OPT(i − 1, w), vi + OPT(i − 1, w − wi)).
```

#### PseudoCode

``` pseudocode
Subset-Sum(Proposals, Money)
  Array M[0 . . . len(proposals), 0 . . .Money]
  Initialize M[0, Money]= 0 for each w = 0, 1, . . . , W
  For i = 1, 2, . . . , len(proposals)
    For w = 0, . . . , Money
      If w < proposals[cost]:
        M(i, w) = M(i − 1, w). 
      Else:
        M(i, w) = max(M(i − 1, w), proposals["quality"] + M(i − 1, w − proposals[cost"]))
    Endfor
  Endfor
  Return M[n, W]
```

From Book

From here 

``` pseudocode
function prob1Backtrack(DP, Q, F, budget)
    maxFundableSubset = []
    currBudget = budget
    for i in [n - 1, n - 2, ..., 0] do
        if DP[i, currBudget - F[i]] + Q[i] >= DP[i - 1, currBudget] then
            maxFundableSubset.append(i)
            currBudget -= F[i]
            end if
    end for
    return maxFundableSubset
```

### Big Oh Analysis

The Big-Oh for this approach is O(Money\*N), where N is len(proposals) and M being the amount of Money we have
The reason of this Big Oh is because we are going from the length of the list compared to the all capacity amounts of money we have. 
Since we are comparing these two values in two separate for-loops, we have O(Money)\*O(N).
~~ Since N can be a constant C (IE N could be 50, 100, etc), we must write this as O(C\*N). So a shortened version of this Big-Oh is: O(N) ~~
Since N is not a constant, being that we can change N to any number we want (similar to M) we can have situations where C > M, C = M, and C < M. Since we can't definitely say what N is and it's not a constant, we can not rule it out. So the final BIg-Oh for this approach is O(N\*Money)
Answer: O(N\*Money)

### Limitations

This approach seems to utilize a lot of space since it is a 2-D array solution. There might be better solutions out there.

Update:
Checking the knapsack algorithm online, the website GeeksForGeeks has a few alternative solutions available in which Time complexity is still O(Money \*N), but the space complexity is down to O(2\*Money)
