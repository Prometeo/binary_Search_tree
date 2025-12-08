class Node:
    def __init__(self, value: int):
        self.left: Node | None = None
        self.right: Node | None = None
        self.value: int = value


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value) -> bool:
        new_node: Node | None = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def containse(self, value) -> bool:
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
