from SolutionLib.PrintTreeByLevelSolution import PrintTreeByLevelSolution
from SolutionLib.RemoveOverlapSolution import RemoveOverlapSolution
from SolutionLib.TwoSumClosestToTargetSolution import \
    TwoSumClosestToTargetSolution


def solution1():
    solution_object = PrintTreeByLevelSolution().get_solution()
    return solution_object


def solution2():
    solution_object = RemoveOverlapSolution().get_solution()
    return solution_object


def solution3():
    solution_object = TwoSumClosestToTargetSolution().get_solution()
    return solution_object


solution_map = {
    "Linkedin Q1": solution1,
    "Linkedin Q2": solution2,
    "Amazon Q1": solution3
}


class SolutionFactory:
    @staticmethod
    def get_solution(question):
        if solution_map[question] is None:
            raise Exception("Not Solution Found.")
        else:
            return solution_map[question]()

