from BinarySearchTreeLib.TreeNode import TreeNode as Node
from AlgorithmLib.AlgorithmBase import AlgorithmBase


class PrintTreeByLevelAlgorithm(AlgorithmBase):

    def submit_algorithm(self, bfs):
        try:
            self.inject_algorithm(bfs)
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
        Test Case 1
             3
            / \
           1  6
             / \
            4  9
        :return: None
        '''
        root = Node(3)
        root.append_left(1)
        root.append_right(6)
        root.right.append_left(4)
        root.right.append_right(9)
        return root

    @staticmethod
    def test2():
        '''
        Test Case 1
             8
           /   \
          5    10
         / \   / \
        4  7  9  13
        :return: None
        '''
        root = Node(8)
        root.append_left(5)
        root.append_right(10)
        root.left.append_left(4)
        root.left.append_right(7)
        root.right.append_left(9)
        root.right.append_right(13)
        return root
