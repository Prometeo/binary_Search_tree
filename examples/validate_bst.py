class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = Node(value)
            return

        def traverse(current_node: Node | None, value: int) -> Node | None:
            if not current_node:
                return Node(value)
            if value < current_node.value:
                current_node.left = traverse(current_node.left, value)
            if value > current_node.value:
                current_node.right = traverse(current_node.right, value)
            return current_node

        traverse(self.root, value)

    def dfs_in_order(self) -> list[int]:
        results: list[int] = []

        def traverse(current_node: Node) -> list[int]:
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results


def is_valid_bst(bst: BST):
    bst_list: list[int] = bst.dfs_in_order()
    is_ordered = bst_list == sorted(bst_list)
    print(is_ordered)
    print(bst_list)


def main():
    my_tree = BST()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    is_valid_bst(my_tree)


if __name__ == "__main__":
    main()
