from Helper import *


class AlgorithmBase:
    def __init__(self, name):
        self.name = name
        self.test_cases = []
        self.status = False
        self.algorithm_func = None

    def __str__(self):
        return str(self.name)

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def is_test_avail(self):
        return len(self.test_cases) > 0

    def add_test_case(self, test_case):
        if test_case is None:
            raise Exception("Test case Null is not allowed.")
        self.test_cases.append(test_case)

    def run(self):
        if not self.get_status():
            raise Exception("Algorithm was not injected.")
        if not self.is_test_avail():
            raise Exception("No available test present.")

        print("Algorithm:["+str(self)+"] is running")
        test_idx = 1
        for test_case in self.test_cases:
            print_dash_helper()
            print("Test Case["+str(test_idx)+"]:")
            self.algorithm_func(test_case)
            test_idx += 1
        print_dash_helper()
        print("Algorithm: ["+str(self)+"] is completed")

    def inject_algorithm(self, func):
        self.algorithm_func = func
        self.set_status(True)