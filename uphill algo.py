""" city block distance formula : x2 - x1 + y2 - y1"""


class Problem:

    def __init__(self, initial, goal):  # constructor for problem
        self.initial = initial
        self.goal = goal


class Node:
    def __init__(self, state, goal):
        self.state = state
        self.goal = goal
        self.succesor = []
        self.size = len(state[0])   # state[0] will get a row from list and find it length
        self.value = self.hn()

    def find(self,key):
        for x2 in range(0,self.size):
             for y2 in range(0,self.size):
                 if self.goal[x2][y2] == key:
                     return [x2, y2]

    def hn(self):
        dis = 0
        for x1 in range (0, self.size):
            for y1 in range(0, self.size):
                [x2, y2] = self.find(self.state[x1][y1])
                dis += abs(x1 - x2) + abs(y2 - y1)
        return dis

    def __repr__(self):
        pass


if __name__ == '__main__':
    initial = [[1, 2, 3],
               [4, -1, 6],
               [7, 5, 8]]
    goal = [[1, 2, 3],          # [00, 01, 02
            [4, 5, 6],          #  10, 11, 12
            [7, 8, -1]]         #  20, 21, 22]
    problem1 = Problem(initial, goal)
    nodex = Node(initial, goal)
    nodex.find(6)