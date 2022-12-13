import time
import pandas as pd
import matplotlib.pyplot as plt

from greedy_algorithm_approach import money_greedy_solution
from brute_force_approach import money_brute_force_solution
from dynamic_programming_approach import dyanmic_programming_algorithm_approach
from problems_set.problem_set1 import problem_set1


def function_timer(proposals, available_money, func): 
    print(f"\tTaking the time of: {func.__name__}")
    start_time = time.time()
    solution = func(proposals, available_money)
    print(f"\tThe Output Quality is:{solution}")
    print(f"\t--- {time.time() - start_time} seconds ---\n")
    return time.time() - start_time

def helper_func(problem_set, results):
    print(f"Getting Results for: {problem_set.__name__}")
    proposals, available_money, optimal_quality, set_size = problem_set()
    print(f"    The size of the sample is: {set_size}"
          f"\n    The available money is:{available_money}"
          f"\n    The Optimal Quality is:{optimal_quality}")
    results["brute_force_time"].append(function_timer(proposals, available_money, money_brute_force_solution))
    results["greedy_time"].append(function_timer(proposals, available_money, money_greedy_solution))
    results["dynamic_time"].append(function_timer(proposals, available_money, dyanmic_programming_algorithm_approach))
    results["set_size"].append(set_size)
    return results

def plot_results(results):
    dataframe = pd.DataFrame(results)    
    # Giving title to the chart using plt.title
    plt.title('Plot of the Times for the Algorithms')
    # Plotting the time series of given dataframe
    plt.plot(dataframe.set_size, dataframe.greedy_time, label="greedy algorithm time")
    plt.plot(dataframe.set_size, dataframe.brute_force_time, label="brute force algorithm time", linestyle="dotted")
    plt.plot(dataframe.set_size, dataframe.dynamic_time, label="DP algorithm time", linestyle="dashed")    
    plt.legend()
    # Providing x and y label to the chart
    plt.xlabel('set size (n)')
    plt.ylabel('time (sec)')
    plt.savefig("time_results_of_algorithms.jpg")
    

def main():
    results = {"greedy_time":[], "brute_force_time":[], "dynamic_time":[], "set_size":[]}
    # Get the results of set 1
    results = helper_func(problem_set1, results)
    
    # # Get the results of set 2
    # results = helper_func(problem_set1)
    
    # # Get the results of set 3
    # results = helper_func(problem_set1)
    
    # # Get the results of set 4
    # results = helper_func(problem_set1)
    
    # # Get the results of set 5
    # results = helper_func(problem_set1)
    
    # # Get the results of set 6
    # results = helper_func(problem_set1)
    
    plot_results(results)


if __name__ == "__main__":
    main()