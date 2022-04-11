'''
@myWSU-ID: V964T747
@Name: Enosh Nyarige
@Due Date: 04 / 03 / 2022
@ Artificial Intelligence, Programming Assignment 1
Wichita State University
'''


class State:

    goal = []

    print("\nLet's start with the intended GOAL state configuration.\n\n", "*" * 60)

    for i in range(0, 3):
        for j in range(0, 3):
            print("\nEnter value for the GOAL tile at Coordinate (", i, ",", j, ")")
            p = int(input())
            goal.append(p)

    ''' 
    A sample goal states that works with my program '''
    # 1, 2, 3, 4, 5, 6, 7, 8, 0
    # 0, 1, 2, 3, 4, 5, 6, 7, 8

    '''
    Initialize the puzzle configuration, and define the heuristic components such as the cost '''

    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        '''
        If a node has a parent, then the cost of the node is calculated as follows '''
        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

    '''
    In cases where the states START = GOAL, then there is no need to do the inversions'''

    def test(self):  # check if the given state is goal
        if self.state == self.goal:
            return True
        return False

    '''
    Based on the Manhattan distance , we can compute the heuristic h(n) as follows
    We identify a digit in START and GOAL states, subtract their coordinate positions to get the absolute sum --> using abs() function '''

    def _ManhattanD(self, n):

        AStarEval = None
        tracker = None
        heuristic = None
        self.heuristic = 0

        for i in range(1, n*n):
            absol_distance = abs(self.state.index(i) - self.goal.index(i))

            # The Manhattan distance of a tile between current state and goal state can be given by
            self.heuristic = self.heuristic + absol_distance/n + absol_distance % n

        self.tracker = self.heuristic

        '''
        For the A* algorithm the evaluation function f(n) is calculated by: f(n) = h(n) + g(n) '''
        self.AStarEval = self.heuristic + self.cost

        return(self.tracker, self.AStarEval)

    @staticmethod
    # '''We start by defining legal moves of a tile; by eliminating illegal moves. This depends on the coordinate location of the tile, like at position (0,0), we eliminate Left and Down '''
    def _legalMoves_tile(x, n):

        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    '''
    From the START state, we can produce the successors of each root on the suggested path to GOAL state. 
    We have four moves with which we can produce the successors as shown below '''

    def expand(self, n):
        x = self.state.index(0)
        moves = self._legalMoves_tile(x, n)

        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            children.append(State(temp, self, direction, self.depth + 1, 1))

        return children

    ''' Backtrack from the goal to the direction of parent(s) until we get the root; there will be no parent at this stagee. '''

    def solution(self):
        followedDir = []
        movesMade = []
        steps = []
        followedDir.append(self.state)
        movesMade.append(self.direction)
        # steps.append(self.state)
        path = self
        while path.parent != None:
            path = path.parent
            followedDir.append(path.state)
            movesMade.append(path.direction)
        followedDir = followedDir[:-1]
        movesMade = movesMade[:-1]
        followedDir.reverse()
        movesMade.reverse()
        for i in range(0, (self.depth)):
            steps.append(followedDir[i])
        arrSteps = []
        
        for j in range(0, 9):
            arrSteps.append(steps[j])
            print("\nStep ", j, ":\n", arrSteps[j])
        
        return (movesMade)