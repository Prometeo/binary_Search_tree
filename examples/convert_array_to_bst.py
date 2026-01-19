class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> bool:
        new_node: Node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp: Node = self.root
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

    def BFS(self):
        current_node = self.root
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


def create_bst(my_list: list[int]) -> BST:
    bst: BST = BST()
    root_index: int = len(my_list) // 2
    bst.insert(my_list[root_index])
    for i in range(root_index):
        bst.insert(my_list[i])
    for j in my_list[root_index + 1 :]:
        bst.insert(j)
    return bst


def main() -> None:
    input: list[int] = [-10, -3, 0, 5, 9]
    input: list[int] = [1, 3]
    bst: BST = create_bst(input)
    result: list[int] = bst.BFS()
    print(result)


if __name__ == "__main__":
    main()
