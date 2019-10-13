from BinarySearchTreeLib.TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_element__(val, self.root)

    def __insert_element__(self, val, curr):
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
            else:
                self.__insert_element__(val, curr.left)
        elif val > curr.val:
            if curr.right is None:
                curr.right = TreeNode(val)
            else:
                self.__insert_element__(val, curr.right)
        else:
            print("Error: Duplicated Value Inserted.")

    def search(self, val):
        curr = self.root
        while curr is not None:
            if curr.val == val:
                return True
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def __str__(self):
        level_list = list()
        queue = list()
        queue.append([self.root, 0])
        while len(queue) > 0:
            [curr, level] = queue[0]
            del queue[0]
            if level == len(level_list):
                level_list.append(list())
            level_list[level].append(curr)
            if curr.left is not None:
                queue.append([curr.left, level+1])
            if curr.right is not None:
                queue.append([curr.right, level+1])
        output = ""
        for row in level_list:
            for col in row:
                output += str(col) + " "
            output += "\n"
        return output

