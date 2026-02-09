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
                sub_tree_min: int = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value: int) -> Node | None:
        self.__delete_node(self.root, value)

    def BFS(self) -> list[int]:
        # Breadth nfirst search
        current_node: Node | None = self.root
        results: list[int] = []
        queue: list[Node] = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self) -> list[int]:
        # Depth first pre order
        results: list[int] = []

        def traverse(current_node: Node) -> None:
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self) -> list[int]:
        # Depth first post order
        results: list[int] = []

        def traverse(current_node: Node) -> None:
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self) -> list[int]:
        # Depth first in order
        results: list[int] = []

        def traverse(current_node: Node) -> None:
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results


def main() -> None:
    bst: BST = BST()
    bst.insert(47)
    bst.insert(21)
    bst.insert(76)
    bst.insert(18)
    bst.insert(27)
    bst.insert(52)
    bst.insert(82)
    print(bst.contains(47))
    print(bst.contains(52))
    print(bst.contains(27))
    bst.delete_node(27)
    print(bst.contains(27))
    print(bst.root.left.value)
    print(bst.dfs_pre_order())
    print(bst.dfs_post_order())
    print(bst.dfs_in_order())


if __name__ == "__main__":
    main()
