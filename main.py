class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def __insert(self, current_node: Node, value: int) -> Node:
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__insert(current_node.right, value)
        return current_node

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        self.__insert(self.root, value)

    def __contains(self, current_node: Node | None, value) -> bool:
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__contains(current_node.left, value)
        if value > current_node.value:
            return self.__contains(current_node.right, value)

    def contains(self, value: int) -> bool:
        return self.__contains(self.root, value)

    def min_value(self, current_node: Node) -> Node:
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node: Node, value: int) -> Node | None:
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min: int = self.min_value(current_node)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value: int) -> Node | None:
        self.__delete_node * self.root, value


def main() -> None:
    bst: BST = BST()
    bst.insert(9)
    bst.insert(20)
    bst.insert(4)
    bst.insert(10)
    bst.insert(7)
    print(bst.contains(4))
    print(bst.contains(5))


if __name__ == "__main__":
    main()
