def naive(max_distance, forward_flights, return_flights):
    result = list()
    min_sum = 0
    for forward_flight in forward_flights:
        for return_flight in return_flights:
            curr_sum = forward_flight[1] + return_flight[1]
            if max_distance < curr_sum:
                continue
            if (max_distance - curr_sum) == (max_distance - min_sum):
                result.append([forward_flight[0], return_flight[0]])
            elif (max_distance - curr_sum) < (max_distance - min_sum):
                result.clear()
                result.append([forward_flight[0], return_flight[0]])
                min_sum = curr_sum
    print(result)


def greedy(input_test):
    max_distance = input_test[0]
    forward_flights = input_test[1]
    return_flights = input_test[2]
    naive(max_distance, forward_flights, return_flights)


class TwoSumClosestToTargetSolution:
    def __init__(self):
        self.solution = greedy

    def get_solution(self):
        if self.solution is None:
            raise Exception("No Solution Found")
        return self.solution
