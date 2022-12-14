from ortools.algorithms import pywrapknapsack_solver
from problems_set.problem_set1 import problem_set1
from problems_set.problem_set2 import problem_set2
from problems_set.problem_set3 import problem_set3
from problems_set.problem_set4 import problem_set4
from problems_set.problem_set5 import problem_set5
from problems_set.problem_set6 import problem_set6


def main(values, weights, capacities):
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('\tTotal value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('\tTotal weight:', total_weight)
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)

def get_data(proposals):
    proposed_set = proposals.get("PROPOSAL")
    values =[] 
    weights = [[]]
    for item in proposed_set:
        weights[0].append(item.get("cost"))
        values.append(item.get("quality"))
    return values, weights

def helper(p_set):
    problem_data = p_set()
    print(f"Getting the optimal results of: {p_set.__name__}")
    values, weights = get_data(problem_data)
    capacities = [problem_data.get("AVAILABLE_MONEY")]
    main(values, weights, capacities)

if __name__ == '__main__':
    helper(problem_set1)
    helper(problem_set2)
    helper(problem_set3)
    helper(problem_set4)
    helper(problem_set5)
    helper(problem_set6)
    