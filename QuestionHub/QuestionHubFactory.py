from AlgorithmLib.PrintTreeByLevel import PrintTreeByLevelAlgorithm
from AlgorithmLib.RemoveOverlap import RemoveOverlap
from AlgorithmLib.TwoSumClosestToTarget import TwoSumClosestToTarget


def question1():
    algorithm_object = PrintTreeByLevelAlgorithm("Print Tree By Level")
    return algorithm_object


def question2():
    algorithm_object = RemoveOverlap("Remove Overlap Interval")
    return algorithm_object


def question3():
    algorithm_object = TwoSumClosestToTarget("Flight Pair Sum")
    return algorithm_object


algorithm_map = {
    "Linkedin Q1": question1,
    "Linkedin Q2": question2,
    "Amazon Q1":   question3,
}


class QuestionHubFactory:
    @staticmethod
    def get_solution(question):
        return algorithm_map[question]()

    @staticmethod
    def get_question_map():
        return algorithm_map
