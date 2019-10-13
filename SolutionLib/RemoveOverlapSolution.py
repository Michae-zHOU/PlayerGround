def greedy(intervals):
    intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
    end = -float('inf')
    count = 0
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    print(count)


class RemoveOverlapSolution:
    def __init__(self):
        self.solution = greedy

    def get_solution(self):
        if self.solution is None:
            raise Exception("No Solution Found")
        return self.solution
