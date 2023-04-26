from queue import PriorityQueue

class Puzzle:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = []

    def solve(self):
        start_node = Puzzle(self.initial_state, None, None, 0, 0)
        priority_queue = PriorityQueue()
        priority_queue.put(start_node)
        level=0
        while not priority_queue.empty():
            current_node = priority_queue.get()
            if current_node.state == self.goal_state:
                while current_node.parent is not None:
                    self.moves.insert(0, current_node.move)
                    current_node = current_node.parent
                break
            zero_index = current_node.state.index(0)
            print("\nLevel:",level)
            if zero_index not in [0, 1, 2]: self.move(current_node, zero_index, zero_index - 3, 'up', 1,priority_queue,level)
            if zero_index not in [6, 7, 8]: self.move(current_node, zero_index, zero_index + 3, 'down', 1,priority_queue,level)
            if zero_index not in [0, 3, 6]: self.move(current_node, zero_index, zero_index - 1, 'left', 1,priority_queue,level)
            if zero_index not in [2, 5, 8]: self.move(current_node, zero_index, zero_index + 1, 'right', 1,priority_queue,level)
            level=level+1
        return self.moves

    def move(self, current_node, current_index, new_index, move, cost,priority_queue,level):
        new_state = current_node.state[:]
        new_state[current_index], new_state[new_index] = new_state[new_index], new_state[current_index]
        heuristic=self.calculate_heuristic(new_state)
        new_node = Puzzle(new_state, current_node, move, current_node.depth + 1, current_node.depth + cost + heuristic)
        priority_queue.put(new_node)
        print("Move: " + move)
        print("g(x):",level," , h(x):",heuristic," , f(x):",level+heuristic)
        print("Current State: ",new_state,"\n")

    def calculate_heuristic(self, state):
        distance = 0
        for i in range(9):
            if state[i] != 0 and state[i]!=self.goal_state[i]: distance +=1
        return distance

if __name__ == '__main__':
    initial_state = [1,2,3,0,4,6,7,5,8]
    goal_state = [1,2,3,4,5,6,7,8,0]
    solver = Solver(initial_state, goal_state)
    print("Initial state:",initial_state)
    print("Goal state:",goal_state)
    print("Solving...")
    moves = solver.solve()
    if moves: print("Solution found in ",len(moves)," moves: ",moves)
    else: print("\nNo Solution found")

