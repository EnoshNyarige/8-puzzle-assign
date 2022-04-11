# 8-puzzle-assign
### Implementing the 8-Puzzle problem using A* search algorithm


- The Program takes an input for the START state and GOAL state configurations from the user, interactively. 
- Keep track of the tiles through coordinates(i, j), where i(0, 1, 2) is the row coordinates and j(0, 1, 2) the column coordinates
- We use a heuristic(Manhattan priority function) to ensure that the next chosen possible state has a minimal number of steps to get to the goal state

- *When entering the values of each coordinates, an empty coordinate(empty tile) will have a zero(0)*

### Steps to compile and execute this Program

- ABC
- DEF


### Sample SSART and Goal configurations that works with my program are as follows
## START STATE(1, 8, 2, 0, 4, 3, 7, 6, 5)
[
    [1, 8, 2]
    [0, 4, 3]
    [7, 6, 5]
]

## GOAL STATE(1, 2, 3, 4, 5, 6, 7, 8, 0)
[
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 0]
]
