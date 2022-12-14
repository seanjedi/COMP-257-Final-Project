from ortools.algorithms import pywrapknapsack_solver
from problems_set.problem_set10 import problem_set10
from problems_set.problem_set25 import problem_set25
from problems_set.problem_set50 import problem_set50
from problems_set.problem_set200 import problem_set200
from problems_set.problem_set500 import problem_set500
from problems_set.problem_set1000 import problem_set1000


def main(values, weights, capacities):
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    packed_values = []
    total_weight = 0
    print('\tTotal value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_values.append(values[i])
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('\tTotal weight:', total_weight)
    print('\tPacked items:', packed_items)
    print('\tPacked_weights:', packed_weights)
    print('\tPacked_values:', packed_values)
    print('\n')

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
    helper(problem_set10)
    helper(problem_set25)
    helper(problem_set50)
    helper(problem_set200)
    helper(problem_set500)
    helper(problem_set1000)
    