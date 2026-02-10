from sys import _current_exceptions


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        def traverse(current_node: Node, value: int) -> Node | None:
            if not current_node:
                return Node(value)
            if value < current_node.value:
                current_node.left = traverse(current_node.left, value)
            if value > current_node.value:
                current_node.right = traverse(current_node.right, value)
            return current_node

        if not self.root:
            self.root = Node(value)
            return
        traverse(self.root, value)

    def dfs_in_order(self, kth: int) -> list[int]:
        results: list[int] = []

        def traverse(current_node: Node | None, kth: int) -> Node | None:
            if len(results) > kth:
                return
            if current_node.left:
                traverse(current_node.left, kth)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right, kth)

        traverse(self.root, kth)
        print(results)
        return results

    def kth_smallest_node(self, kth: int) -> int:
        result: list[int] = self.dfs_in_order(kth)
        return result[kth - 1]


def main():
    bst: BST = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    result = bst.kth_smallest_node(1)
    print(result)


if __name__ == "__main__":
    main()
