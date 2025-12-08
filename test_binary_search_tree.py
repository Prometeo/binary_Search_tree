import pytest
from main import BinarySearchTree


# ~> Fixtures
@pytest.fixture
def base_binary_search_tree():
    return BinarySearchTree()


def test_append_item_to_empy_bs_tree(base_binary_search_tree: BinarySearchTree):
    result = base_binary_search_tree.insert(9)
    assert result
    assert base_binary_search_tree.root.value == 9


def test_append_items_to_bs_tree(base_binary_search_tree: BinarySearchTree):
    base_binary_search_tree.insert(9)
    base_binary_search_tree.insert(15)
    base_binary_search_tree.insert(7)
    assert base_binary_search_tree.root.value == 9
    assert base_binary_search_tree.root.left.value == 7
    assert base_binary_search_tree.root.right.value == 15


def test_append_repeated_items_to_bs_tree(base_binary_search_tree: BinarySearchTree):
    result_1 = base_binary_search_tree.insert(9)
    result_2 = base_binary_search_tree.insert(15)
    result_3 = base_binary_search_tree.insert(7)
    result_4 = base_binary_search_tree.insert(15)
    assert result_1
    assert result_2
    assert result_3
    assert not result_4


def test_find_item_on_bs_tree(base_binary_search_tree: BinarySearchTree):
    base_binary_search_tree.insert(6)
    base_binary_search_tree.insert(8)
    base_binary_search_tree.insert(20)
    base_binary_search_tree.insert(16)
    result = base_binary_search_tree.containse(20)
    assert result


def test_not_find_item_on_bs_tree(base_binary_search_tree: BinarySearchTree):
    base_binary_search_tree.insert(6)
    base_binary_search_tree.insert(8)
    base_binary_search_tree.insert(20)
    base_binary_search_tree.insert(16)
    result = base_binary_search_tree.containse(25)
    assert not result
