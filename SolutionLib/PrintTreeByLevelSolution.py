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


class PrintTreeByLevelSolution:
    def __init__(self):
        self.solution = bfs

    def get_solution(self):
        if self.solution is None:
            raise Exception("No Solution Found")
        return self.solution
