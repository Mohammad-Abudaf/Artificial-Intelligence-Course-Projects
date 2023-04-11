class Node:

    def __init__(self, state, parent, action, path_cost):
        self.state: list = state
        self.parent: Node = parent
        self.action = action
        self.path_cost: float = path_cost

    def find_index(self, number: int):
        return self.state.index(number)

    def move_left(self):
        zero_index: int = self.find_index(0)
        number_of_steps: int = 1
        temp_index: int = self.find_index(self.state[zero_index - number_of_steps])
        temp_value: int = self.state[temp_index]
        self.state[temp_index] = 0
        self.state[zero_index] = temp_value

    def move_right(self):
        zero_index: int = self.find_index(0)
        number_of_steps: int = 1
        temp_index: int = self.find_index(self.state[zero_index + number_of_steps])
        temp_value: int = self.state[temp_index]
        self.state[temp_index] = 0
        self.state[zero_index] = temp_value

    def move_up(self):
        zero_index: int = self.find_index(0)
        number_of_steps: int = 3
        temp_index: int = self.find_index(self.state[zero_index - number_of_steps])
        temp_value: int = self.state[temp_index]
        self.state[temp_index] = 0
        self.state[zero_index] = temp_value

    def move_down(self):
        zero_index: int = self.find_index(0)
        number_of_steps: int = 3
        temp_index: int = self.find_index(self.state[zero_index + number_of_steps])
        temp_value: int = self.state[temp_index]
        self.state[temp_index] = 0
        self.state[zero_index] = temp_value
        pass

    def check_goal_state(self, goal: list):
        return self.state == goal

    def generate_new_node(self, state: list, parent, action: str, path_cost: int):
        new_node: Node = Node(self.state, self.parent, self.action, self.path_cost)

        if action == 'up':
            new_node.move_up()
        elif action == 'down':
            new_node.move_down()
        elif action == 'right':
            new_node.move_right()
        else:
            new_node.move_left()
        return new_node

    def find_coordinates(self, state: list, number: int):
        index: int = state.index(number)
        i = index // 3
        j = index - i * 3
        return i, j

    def m_distance(self, goal_state: list):
        h_point: int = 0

        for num in range(9):
            i, j = self.find_coordinates(self.state, num)
            x, y = self.find_coordinates(goal_state, num)
            h = abs(i - x) + abs(j - y)
            h_point = h_point + h

        return h_point