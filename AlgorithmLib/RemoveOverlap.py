from AlgorithmLib.AlgorithmBase import AlgorithmBase


class RemoveOverlap(AlgorithmBase):

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
        [1,2],[2,3],[1,3],[3,4]

        :return: None
        '''
        return [[1,2],[3,4],[1,3],[2,3]]

    @staticmethod
    def test2():
        '''
        [1,2],[1,2],[1,2]

        :return:
        '''
        return [[1,2],[1,2],[1,2]]