def find_internal_nodes_num(tree):

    parent_nodes = set(tree)
    internal_nodes_num = max(0, len(parent_nodes) - 1)

    return internal_nodes_num

# Test Cases
trees = [
            (0,[]),
            (0,[-1]),
            (1,[-1,0]),
            (1,[-1,0,0]),
            (2,[-1,0,1]),
            (3,[-1,0,1,2]),
            (3,[4, 4, 1, 5, -1, 4, 5])
        ]

for tree in trees:
    assert find_internal_nodes_num(tree[1]) == tree[0], tree
