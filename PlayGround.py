from AlgorithmLib.PrintTreeByLevel import PrintTreeByLevelAlgorithm


class PlayGround:
    def __init__(self):
        self.algorithm = None

    def build(self, question):
        self.algorithm = algorithm_map.get(question)()

    def run(self, callback):
        self.algorithm.submit_algorithm(callback)


def question1():
    algorithm_object = PrintTreeByLevelAlgorithm("Print Tree By Level")
    return algorithm_object


algorithm_map = {
    "Linkedin Q1": question1
}


def bfs(root):
    q = list()
    q.append(root)
    while len(q) > 0:
        curr = q[0]
        del q[0]
        print(curr)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)


if __name__ == "__main__":
    play_ground = PlayGround()
    play_ground.build("Linkedin Q1")
    play_ground.run(bfs)