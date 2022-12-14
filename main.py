import time
import pandas as pd
import matplotlib.pyplot as plt

from greedy_algorithm_approach import money_greedy_solution
from brute_force_approach import money_brute_force_solution
from dynamic_programming_approach import dyanmic_programming_algorithm_approach
from problems_set.problem_set10 import problem_set10
from problems_set.problem_set15 import problem_set15
from problems_set.problem_set20 import problem_set20
from problems_set.problem_set25 import problem_set25
from problems_set.problem_set30 import problem_set30
from problems_set.problem_set50 import problem_set50
from problems_set.problem_set200 import problem_set200
from problems_set.problem_set500 import problem_set500
from problems_set.problem_set1000 import problem_set1000

VALID_CHOICES = ["1", "2", "3", "4", "q", ""]
VALID_ALGORITHMS_BRUTE_FORCE = [problem_set10, problem_set15, problem_set20]
VALID_ALGORITHMS_GREEDY = [problem_set10, problem_set15, problem_set20, problem_set25,
                           problem_set30, problem_set50, problem_set200, problem_set500, problem_set1000]
VALID_ALGORITHMS_DP = [problem_set10]


class Solution:
    results = {}
    problem_data = {}
    set_count = 1
    algorithm_choice = "4"
    running_algorithm = None
    algorithm_choice_name = None
    runs = "1"

    def get_input(self):
        self.algorithm_choice = input("Which Algorithm Do you want to use (default: 4)?"
                                      "\n1) Brute Force Algorithm"
                                      "\n2) Greedy Algorithm"
                                      "\n3) Dynamic Programming Algorithm"
                                      "\n4) All Three"
                                      "\nq) Quit out of the program"
                                      "\nChoice: ")
        while self.algorithm_choice not in VALID_CHOICES:
            self.algorithm_choice = input("Please Make a Valid Choice: ")
        if self.algorithm_choice == "1":
            self.results = {"brute_force_time": [], "set_size": []}
            self.algorithm_choice_name = (
                "money_brute_force_solution", "brute_force_time")
            self.running_algorithm = money_brute_force_solution
        elif self.algorithm_choice == "2":
            self.results = {"greedy_time": [], "set_size": []}
            self.algorithm_choice_name = (
                "money_greedy_solution", "greedy_time")
            self.running_algorithm = money_greedy_solution
        elif self.algorithm_choice == "3":
            self.algorithm_choice_name = (
                "dyanmic_programming_algorithm_approach", "dynamic_time")
            self.results = {"dynamic_time": [], "set_size": []}
            self.running_algorithm = dyanmic_programming_algorithm_approach
        elif self.algorithm_choice == "4" or self.algorithm_choice == "":
            self.algorithm_choice = "4"
            self.results = {"greedy_time": [], "brute_force_time": [
            ], "dynamic_time": [], "set_size": []}
        else:
            exit(0)
        self.runs = input("How many runs do you want (default: 1)?"
                          "\nChoice: ")
        if self.runs == "":
            self.runs = 1

    def test_runner(self):
        self.run_tests(problem_set10)
        self.run_tests(problem_set15)
        self.run_tests(problem_set20)
        self.run_tests(problem_set25)
        self.run_tests(problem_set30)
        self.run_tests(problem_set50)
        self.run_tests(problem_set200)
        self.run_tests(problem_set500)
        self.run_tests(problem_set1000)
        self.plot_results()

    def run_tests(self, problem_set):
        self.problem_data = problem_set()
        self.helper_func(problem_set)
        self.set_count += 1

    def helper_func(self, problem_set):
        print(f"Getting Results for: {problem_set.__name__}")
        print("    The size of the sample is: {}"
              "\n    The available money is:{}"
              "\n    The Optimal Quality is:{}".format(self.problem_data.get('SET_SIZE'), self.problem_data.get("AVAILABLE_MONEY"), self.problem_data.get("OPTIMAL_QUALITY")))
        for i in range(int(self.runs)):
            if self.algorithm_choice == "4":
                self.collect_results_all(problem_set)
            else:
                self.collect_results_one(problem_set)

    def collect_results_all(self, problem_set):
        # Get Brute Force algorithm times
        if problem_set in VALID_ALGORITHMS_BRUTE_FORCE:
            self.results["brute_force_time"].append(
                self.function_timer(money_brute_force_solution))
        else:
            print("\t\tBrute Force did not run for this problem set")
            self.results["brute_force_time"].append(0)
        # Get greedy algorithm times
        if problem_set in VALID_ALGORITHMS_GREEDY:
            self.results["greedy_time"].append(
                self.function_timer(money_greedy_solution))
        else:
            print("\t\tGreedy Algorithm did not run for this problem set")
            self.results["greedy_time"].append(0)
        # Get Dynamic Programming algorithm times
        if problem_set in VALID_ALGORITHMS_DP:
            self.results["dynamic_time"].append(
                self.function_timer(dyanmic_programming_algorithm_approach))
        else:
            print("\t\tDynamic Programming Algorithm did not run for this problem set")
            self.results["dynamic_time"].append(0)
        self.results["set_size"].append(
            self.problem_data.get("SET_SIZE"))

    def collect_results_one(self, problem_set):
        if self.running_algorithm == money_brute_force_solution:
            if problem_set in VALID_ALGORITHMS_BRUTE_FORCE:
                self.results[self.algorithm_choice_name[1]].append(
                    self.function_timer(self.running_algorithm))
                self.results["set_size"].append(
                    self.problem_data.get("SET_SIZE"))
            else:
                print("\t\tBrute Force did not run for this problem set")
        elif self.running_algorithm == money_greedy_solution:
            if problem_set in VALID_ALGORITHMS_GREEDY:
                self.results[self.algorithm_choice_name[1]].append(
                    self.function_timer(self.running_algorithm))
                self.results["set_size"].append(
                    self.problem_data.get("SET_SIZE"))
            else:
                print("\t\tGreedy Algorithm did not run for this problem set")
        elif self.running_algorithm == dyanmic_programming_algorithm_approach:
            if problem_set in VALID_ALGORITHMS_DP:
                self.results[self.algorithm_choice_name[1]].append(
                    self.function_timer(self.running_algorithm))
                self.results["set_size"].append(
                    self.problem_data.get("SET_SIZE"))
            else:
                print("\tDynamic Programming Algorithm did not run for this problem set")

    def function_timer(self, func):
        print(f"\tTaking the time of: {func.__name__}")
        start_time = time.time()
        solution_quality = func(self.problem_data.get(
            "PROPOSAL"), self.problem_data.get("AVAILABLE_MONEY"))
        print(f"\t\tThe Output Quality is:{solution_quality}")
        print(f"\t\t--- {time.time() - start_time} seconds ---\n")
        return time.time() - start_time

    def plot_results(self):
        dataframe = pd.DataFrame(self.results)
        # Giving title to the chart using plt.title
        plt.title('Plot of the Times for the Algorithms')
        # Plotting the time series of given dataframe
        if self.algorithm_choice == "4":
            plt.plot(dataframe.set_size, dataframe.greedy_time,
                     label="greedy algorithm time")
            plt.plot(dataframe.set_size, dataframe.brute_force_time,
                     label="brute force algorithm time", linestyle="dotted")
            plt.plot(dataframe.set_size, dataframe.dynamic_time,
                     label="DP algorithm time", linestyle="dashed")
        else:
            plt.plot(dataframe.set_size, dataframe.get(
                self.algorithm_choice_name[1]), label=f"{self.algorithm_choice_name[0]} time")
        plt.legend()
        # Providing x and y label to the chart
        plt.xlabel('set size (n)')
        plt.ylabel('time (sec)')
        plt.savefig(f"time_results_of_algorithms{self.set_count}.jpg")


def main():
    # Create the test runner class
    runner = Solution()
    # # Get the algorithm that we want to run
    runner.get_input()
    runner.test_runner()


if __name__ == "__main__":
    main()
