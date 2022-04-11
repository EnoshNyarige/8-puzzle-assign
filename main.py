'''
@myWSU-ID: V964T747
@Name: Enosh Nyarige
@Due Date: 04 / 03 / 2022
@ Artificial Intelligence, Programming Assignment 1
Wichita State University
'''

from queue import LifoQueue, PriorityQueue, Queue
from time import time

from State import State


''' 
Lets implement how the A* Algorithm will behave, using a Manhattan heuristic... '''


def AStarSearch(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root._ManhattanD(n)
    frontier.put((evaluation[1], counter, root)) 

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child._ManhattanD(n)
                frontier.put((evaluation[1], counter, child))
    return


''' 
lets keep track of the number of inversions we are doing from START state to desired GOAL state '''


def countInversions(puzzle):
    count = 0
    for i in range(len(puzzle) - 1):
        for j in range(i + 1, len(puzzle)):
            if ((puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                count += 1
    return count


''' 
There are some combinations that will not be solvable even when we do more inversions. Its best we dont look at such a puzzle.
Ideally, the number of inversions that are not even indicate a unsolvable puzzle --> '''


def _isSolvable(puzzle):
    numOfInversions = countInversions(puzzle)
    if (numOfInversions % 2 == 0):
        return True
    else:
        return False


def main():

    startConfig = []

    ''' 
    Starting from the tile at coordinate (0, 0), ask for the user input for the 3 * 3 matrix and read the input as an in array '''

    print("\n", "*" * 60, "\nThe START state configuration for the puzzle next\n\n", "*" * 60)
    for i in range(0, 3):
        for j in range(0, 3):
            print("\nEnter value for the START tile at Coordinate (", i, ",", j, ")")
            p = int(input())
            startConfig.append(p)

    ''' 
    A sample START state that works '''
    # 1, 8, 2, 0, 4, 3, 7, 6, 5

    # '''
    # Show the start state as an array to the user '''

    # print("\n\nThe given state is: \n", startConfig)

    if _isSolvable(startConfig):
        print("\nThis pair of START and GOAL states puzzle is solvable... \n")

        timeComplexity = time()
        AStarSolution = AStarSearch(startConfig, 3)
        AStarTime = time() - timeComplexity

        '''
        Lets start with showing the order of steps involved to get to the solution '''
        print('\nTo get you the desired GOAL state, I did the following inversions: \n\n ',
              AStarSolution[0])

        '''
        It is also worth to note the number of nodes that were explored in the inversion process to get to the goal state '''
        print('\nNumber of explored nodes is in the inversions above is:\n',
              AStarSolution[1])

    else:
        print("Try a different set of START and GOAL states!")


main()
