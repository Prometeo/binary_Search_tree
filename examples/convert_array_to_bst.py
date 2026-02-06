# Convert sorted list into a balanced binary search tree
class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def __insert(self, current_node: Node, value: int) -> Node:
        if not current_node:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insert(current_node.left, value)
        if value > current_node.right:
            current_node.right = self.__insert(current_node.right, value)
        return current_node

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = Node(value)
        self.__insert(self.root, value)

    def __sorted_list_to_bst(self, nums, left: int, right: int) -> Node:
        if left > right:
            return None

        mid: int = (left + right) // 2
        current: Node = Node(nums[mid])
        current.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        current.right = self.__sorted_list_to_bst(nums, mid + 1, right)

        return current

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def BFS(self) -> list[int | str]:
        current_node: Node = self.root
        results = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node: Node | None = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results


def main() -> None:
    bst = BST()
    bst.sorted_list_to_bst([-10, -3, 0, 5, 9])
    result: list[int] = bst.BFS()
    print(result)


if __name__ == "__main__":
    main()
