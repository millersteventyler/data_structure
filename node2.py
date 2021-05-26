
class Node2:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert_node(self, root, key):
        if root is None:
            return Node2(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = root.insert_node(root.right, key)
            else:
                root.left = root.insert_node(root.left, key)
            return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def search_for_node(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search_for_node(root.right, key)
        return self.search_for_node(root.left, key)
