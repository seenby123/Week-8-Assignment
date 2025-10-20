class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent = self._find_node(self.root, parent_name)
        if not parent:
            print(f"Parent {parent_name} not found")
            return

        child = DoctorNode(child_name)
        if side.lower() == "left":
            if parent.left is None:
                parent.left = child
            else:
                print(f"Left child already exists for {parent_name}")
        elif side.lower() == "right":
            if parent.right is None:
                parent.right = child
            else:
                print(f"Right child already exists for {parent_name}")
        else:
            print(f"Invalid side: {side}")

    def _find_node(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self._find_node(node.left, name)
        if left_search:
            return left_search
        return self._find_node(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# test
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))