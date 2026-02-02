class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def __insert(self, current_node: Node | None, value: int) -> Node | None:
        if not current_node:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__insert(current_node.right, value)
        return current_node

    def insert(self, value) -> None:
        if not self.root:
            self.root = Node(value)
            return None
        self.__insert(self.root, value)

    def __invert_tree(self, node: Node | None) -> Node | None:
        if node is None:
            return None
        temp: Node = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        return node

    def invert_tree(self) -> None:
        self.__invert_tree(self.root)


def main():
    bst: BST = BST()
    bst.insert(7)
    bst.insert(5)
    bst.insert(9)
    bst.insert(8)
    bst.invert_tree()


if __name__ == "__main__":
    main()
