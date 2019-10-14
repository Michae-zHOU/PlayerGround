from AlgorithmLib.AlgorithmBase import AlgorithmBase


class KMP(AlgorithmBase):

    def submit_algorithm(self, kmp):
        try:
            self.inject_algorithm(kmp)
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
        txt = "ABABDABACDABABCABAB"
        pat = "ABABCABAB"
        :return: None
        '''
        return [
                "ABABCABAB",
                "ABABDABACDABABCABAB"
                ]

    @staticmethod
    def test2():
        '''
        txt = "aabacaabaa"
        pat = "aabaa"
        :return:
        '''
        return [
                "aabaa",
                "aabacaabaa"
                ]