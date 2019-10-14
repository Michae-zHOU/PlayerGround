from SolutionLib.PrintTreeByLevelSolution import PrintTreeByLevelSolution
from SolutionLib.RemoveOverlapSolution import RemoveOverlapSolution
from SolutionLib.TwoSumClosestToTargetSolution import \
    TwoSumClosestToTargetSolution
from SolutionLib.KMPSolution import KMPSolution


def extract_solution(function):
    return function.get_solution()


solution_map = {
    "Linkedin Q1":      extract_solution(PrintTreeByLevelSolution()),
    "Linkedin Q2":      extract_solution(RemoveOverlapSolution()),
    "Amazon Q1":        extract_solution(TwoSumClosestToTargetSolution()),
    "KMP Algorithm":    extract_solution(KMPSolution())
}


class SolutionFactory:
    @staticmethod
    def get_solution(question):
        if solution_map[question] is None:
            raise Exception("Not Solution Found.")
        else:
            return solution_map[question]

