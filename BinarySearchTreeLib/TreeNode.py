class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return str(self.val)

    def append_left(self, val):
        self.left = TreeNode(val)

    def append_right(self, val):
        self.right = TreeNode(val)

    def print_detail(self):
        str_left = '#'
        if self.left is not None:
            str_left = str(self.left)
        str_right = '#'
        if self.right is not None:
            str_right = str(self.right)
        print(str_left+" "+self.val+" "+str_right)
