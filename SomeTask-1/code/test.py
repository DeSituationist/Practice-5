from main import Node, insert, find_max, find_min, delete, delete_max, delete_min
def find_min_and_find_max():
    root = Node(20)
    insert(10, root)
    insert(30, root)
    assert find_min(root).val == 10
    assert find_max(root).val == 30

def test_delete():
    root = Node(20)
    root = insert(10, root)
    root = insert(30, root)
    root = insert(40, root)
    root = delete(10, root)
    assert root.left is None
    assert find_min(root).val == 20
    root = delete(30, root)
    assert root.right.val == 40
    root = delete(20, root)
    assert root.val == 40

def test_insert_and_balancing():
    root = Node(10)
    root = insert(20, root)
    root = insert(30, root)
    assert root.val == 20
    assert root.right.val == 30
    assert root.left.val == 10
    assert root.height == 2
    assert root.left.height == 1
    assert root.right.height == 1

def test_delete_min_and_delete_max():
    root = Node(40)
    root = insert(50, root)
    root = insert(60, root)
    root = delete_min(root)
    assert root.val == 40
    root = delete_max(root)
    assert find_max(root).val == 50

find_min_and_find_max()
test_delete()
test_delete_min_and_delete_max()

print("All tests passed.")
