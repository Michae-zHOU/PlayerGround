from SolutionLib.SolutionFactory import SolutionFactory
from QuestionHub.QuestionHubFactory import QuestionHubFactory


class PlayGround:
    def __init__(self):
        self.algorithm = None
        self.algorithm_map = QuestionHubFactory().get_question_map()

    def build(self, question):
        self.algorithm = self.algorithm_map.get(question)

    def run(self, callback):
        self.algorithm.submit_algorithm(callback)


if __name__ == "__main__":
    pg = PlayGround()
    sf = SolutionFactory()
    for key in pg.algorithm_map:
        pg.build(key)
        pg.run(sf.get_solution(key))

