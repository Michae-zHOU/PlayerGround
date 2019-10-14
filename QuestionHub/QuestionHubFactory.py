from AlgorithmLib.PrintTreeByLevel import PrintTreeByLevelAlgorithm
from AlgorithmLib.RemoveOverlap import RemoveOverlap
from AlgorithmLib.TwoSumClosestToTarget import TwoSumClosestToTarget
from AlgorithmLib.KMP import KMP

algorithm_map = {
    "Linkedin Q1":      PrintTreeByLevelAlgorithm("Print Tree By Level"),
    "Linkedin Q2":      RemoveOverlap("Remove Overlap Interval"),
    "Amazon Q1":        TwoSumClosestToTarget("Flight Pair Sum"),
    "KMP Algorithm":    KMP("Knuth-Morris-Pratt Algorithm")
}


class QuestionHubFactory:
    @staticmethod
    def get_solution(question):
        return algorithm_map[question]

    @staticmethod
    def get_question_map():
        return algorithm_map
