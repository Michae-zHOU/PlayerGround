from AlgorithmLib.AlgorithmBase import AlgorithmBase


class TwoSumClosestToTarget(AlgorithmBase):

    def submit_algorithm(self, greedy):
        try:
            self.inject_algorithm(greedy)
        except Exception:
            raise Exception
        self.add_custom_test_case()

        try:
            self.run()
        except Exception:
            raise Exception

    def add_custom_test_case(self):
        case1 = self.test1()
        self.add_test_case(case1)
        case2 = self.test2()
        self.add_test_case(case2)

    @staticmethod
    def test1():
        '''
        maxTravelDist = 7000
        forwardRouteList = [[1,2000],[2,4000],[3,6000]]
        returnRouteList = [[1,2000]]

        :return: None
        '''
        return [10000,
                [[1, 3000], [2, 5000], [3, 7000], [4, 10000]],
                [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
               ]

    @staticmethod
    def test2():
        '''
        maxTravelDist = 10000
        forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
        returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]

        :return:
        '''
        return [7000,
                [[1,2000],[2,4000],[3,6000]],
                [[1,2000]]
               ]