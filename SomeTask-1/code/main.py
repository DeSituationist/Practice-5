class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


def get_height(node):
    if not node:
        return 0
    return node.height


def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1


def balance_factor(node):
    return get_height(node.left) - get_height(node.right)


def small_right(node_b):
    node_a = node_b.left
    Ra = node_a.right
    node_b.left = Ra
    node_a.right = node_b

    update_height(node_b)
    update_height(node_a)

    return node_a


def small_left(node_a):
    node_b = node_a.right
    Lb = node_b.left
    node_a.right = Lb
    node_b.left = node_a

    update_height(node_a)
    update_height(node_b)

    return node_b


def big_right(node_b):
    node_a = node_b.left
    node_b.left = small_left(node_a)
    return small_right(node_b)


def big_left(node_a):
    node_b = node_a.right
    node_a.right = small_right(node_b)
    return small_left(node_a)


def insert(key, root):
    if not root:
        return Node(key)

    if key < root.val:
        root.left = insert(key, root.left)
    elif key > root.val:
        root.right = insert(key, root.right)
    else:
        return root

    update_height(root)
    balance = balance_factor(root)

    if balance > 1 and key < root.left.val:
        return small_right(root)
    if balance < -1 and key > root.right.val:
        return small_left(root)
    if balance > 1 and key > root.left.val:
        return big_right(root)
    if balance < -1 and key < root.right.val:
        return big_left(root)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def delete_min(root):
    if root is None:
        return None
    if root.left is None:
        return root.right
    root.left = delete_min(root.left)
    update_height(root)
    return rebalance(root)


def delete_max(root):
    if root is None:
        return None
    if root.right is None:
        return root.left
    root.right = delete_max(root.right)
    update_height(root)
    return rebalance(root)


def delete(key, root):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(key, root.left)
    elif key > root.val:
        root.right = delete(key, root.right)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(temp.val, root.right)

    update_height(root)
    return rebalance(root)


def rebalance(node):
    balance = balance_factor(node)

    if balance > 1:
        if balance_factor(node.left) < 0:
            node.left = small_left(node.left)
        return small_right(node)

    if balance < -1:
        if balance_factor(node.right) > 0:
            node.right = small_right(node.right)
        return small_left(node)

    return node
