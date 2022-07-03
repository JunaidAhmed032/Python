from collections import deque


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.State = state
        self.Parent = parent
        self.Action = action
        self.Path_cost = path_cost

    def __repr__(self):
        return "Node : {0} {1} ".format(self.State, self.Path_cost)

    def _eq_(self, node):
        return isinstance(node, Node) and self.State == node.State

    def _lt_(self, node):
        return isinstance(node, Node) and self.Path_cost < node.Path_cost



         n1 = Node("Arad","sibu","right", 30)
         n1 = Node(state="Arid", path_cost=30)
         n2 = Node(state="Arid", path_cost=40)
         n3 = Node(state="sibiu", path_cost=40)
         print(n1)
         print(n1 == n2)
         print(n1._eq_(n2))
         print(n1 == n3)
         print(n1 < n2)
         print(n1._lt_(n2))


class Problem:
    def __init__(self, initial_state, goal_state):
        self.Initial_state = initial_state
        self.Goal_state = goal_state

        self.state_space = {}
        self.state_space['Arad'] = {'R1': 'Zerind', 'R2': 'Sibiu', 'R3': 'Timisoara'}
        self.state_space['Zerind'] = {'R1': 'Oradea', 'R2': 'Arad'}
        self.state_space['Oradea'] = {'R1': 'Sibiu', 'R2': 'Zerind'}
        self.state_space['Timisoara'] = {'R1': 'Lugoj', 'R2': 'Arad'}
        self.state_space['Lugoj'] = {'R1': 'Timisoara', 'R2': 'Mehandia'}
        self.state_space['Drobeta'] = {'R1': 'Mehandia', 'R2': 'Craiova'}
        self.state_space['Craiova'] = {'R1': 'Drobeta', 'R2': 'Rimnicu Vilcea', 'R3': 'Pitesti'}
        self.state_space['Rimnicu Vilcea'] = {'R1': 'Sibiu', 'R2': 'Pitesti', 'R3': 'Craiova'}
        self.state_space['Sibiu'] = {'R1': 'Arad', 'R2': 'Fagaras', 'R3': 'Oradea', 'R4': 'Rimnicu Vilcea'}
        self.state_space['Fagaras'] = {'R1': 'Sibiu', 'R2': 'Bucharest'}
        self.state_space['Pitesti'] = {'R1': 'Rimnicu Vilcea', 'R2': 'Craiova', 'R3': 'Bucharest'}
        self.state_space['Bucharest'] = {'R1': 'Fagaras', 'R2': 'Pitesti', 'R3': 'Giurgiu', 'R4': 'Urziceni'}
        self.state_space['Giurgiu'] = {'R1': 'Bucharest'}
        self.state_space['Urziceni'] = {'R1': 'Bucharest', 'R2': 'Valsui', 'R3': 'Hirsova'}
        self.state_space['Hirsova'] = {'R1': 'Eforie', 'R2': 'Urziceni'}
        self.state_space['Eforie'] = {'R1': 'Hirsova'}
        self.state_space['Valsui'] = {'R1': 'Urziceni', 'R2': 'Iasi'}
        self.state_space['Iasi'] = {'R1': 'Valsui', 'R2': 'Neamt'}
        self.state_space['Neamt'] = {'R1': 'Iasi'}
        self.state_space['Mehandia'] = {'R1': 'Lugoj', 'R2': 'Drobeta'}

        self.step_cost = {}
        self.step_cost['Arad'] = {'R1': 75, 'R2': 140, 'R3': 118}
        self.step_cost['Zerind'] = {'R1': 71, 'R2': 75}
        self.step_cost['Oradea'] = {'R1': 152, 'R2': 71}
        self.step_cost['Timisoara'] = {'R1': 111, 'R2': 118}
        self.step_cost['Lugoj'] = {'R1': 111, 'R2': 70}
        self.step_cost['Drobeta'] = {'R1': 75, 'R2': 120}
        self.step_cost['Craiova'] = {'R1': 120, 'R2': 146, 'R3': 138}
        self.step_cost['Rimnicu Vilcea'] = {'R1': 80, 'R3': 97, 'R4': 146}
        self.step_cost['Sibiu'] = {'R1': 140, 'R2': 99, 'R3': 151, 'R4': 80}
        self.step_cost['Fagaras'] = {'R1': 99, 'R2': 211}
        self.step_cost['Pitesti'] = {'R1': 97, 'R2': 138, 'R3': 101}
        self.step_cost['Bucharest'] = {'R1': 211, 'R2': 101, 'R3': 90, 'R4': 85}
        self.step_cost['Giurgiu'] = {'R1': 90}
        self.step_cost['Urziceni'] = {'R1': 85, 'R2': 142, 'R3': 98}
        self.step_cost['Hirsova'] = {'R1': 86, 'R2': 98}
        self.step_cost['Eforie'] = {'R1': 86}
        self.step_cost['Valsui'] = {'R1': 142, 'R2': 92}
        self.step_cost['Iasi'] = {'R1': 92, 'R2': 87}
        self.step_cost['Neamt'] = {'R1': 87}
        self.step_cost['Mehandia'] = {'R1': 70, 'R2': 75}

        self.heuristics = {}
        self.heuristics['Arad'] = 366
        self.heuristics['Zerind'] = 374
        self.heuristics['Oradea'] = 380
        self.heuristics['Timisoara'] = 329
        self.heuristics['Lugoj'] = 244
        self.heuristics['Drobeta'] = 242
        self.heuristics['Craiova'] = 160
        self.heuristics['Rimnicu Vilcea'] = 193
        self.heuristics['Sibiu'] = 253
        self.heuristics['Fagaras'] = 176
        self.heuristics['Pitesti'] = 100
        self.heuristics['Bucharest'] = 0
        self.heuristics['Giurgiu'] = 77
        self.heuristics['Urziceni'] = 80
        self.heuristics['Hirsova'] = 151
        self.heuristics['Eforie'] = 161
        self.heuristics['Valsui'] = 199
        self.heuristics['Iasi'] = 226
        self.heuristics['Neamt'] = 234
        self.heuristics['Mehandia'] = 241

    def child_node(p, parent, action):
        next_state = Problem.Result(parent.state, action)
        step_cost = Problem.Path_cost(parent.state, action)
        cost = parent.path_cost + int(step_cost)
        child = Node(next_state, parent, action, cost)
        return child

    def Actions(self, state):
        return self.state_space[state].keys()

    def Results(self, state, action):
        return self.state_space[state][action]

    def Goal_test(self, state):
        return state == self.Goal_state

    def Path_cost(self, state, action):
        return self.step_cost[state][action]

    def solution(node):
        path_back = []
        while node.parent is not None:
            path_back.append(node)
            node = node.parent
        for n in reversed(path_back):
            print(n)


def bfs(problem):
    node = Node(problem.initial.state)
    if problem.Goal_test(node.State):
        return solution(node)
    frontier = deque()
    frontier.append(node)
    Explored = []
    while True:
        if frontier.IsEmpty():
            return  print("failure")
# ------------------------------------End Of Class--------------------------------------------------------------
p = Problem("Arid", "Bucharest")
print(p.Actions("Arad"))
print(p.Results("Arad", 'R1'))
print(p.Results("Arad", 'R2'))
print(p.Results("Arad", 'R3'))
print(p.Path_cost("Arad", 'R1'))