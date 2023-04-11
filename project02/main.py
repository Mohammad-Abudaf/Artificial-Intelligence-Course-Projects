from lib.node import Node


def print_node_state(node: Node):
    i: int = 1
    while i < 10:
        if i % 3 == 0:
            print(node.state[i - 1], end=" ")
            print()
        else:
            print(node.state[i - 1], end=" ")
        i = i + 1


if __name__ == '__main__':
    start_state: list = [2, 3, 5,
                         1, 4, 7,
                         8, 6, 0]

    goal_state: list = [1, 2, 3,
                        4, 5, 6,
                        7, 8, 0]

    node = Node(state=goal_state, action=None, parent=None, path_cost=0)

    print_node_state(node)
    print()


    h = node.m_distance(goal_state)
    print(h)

    # new = node.generate_new_node(node.state, node.parent, action='right', path_cost=1)

    # print_node_state(new)
