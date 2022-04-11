# 8-puzzle-assign
### Implementing the 8-Puzzle problem using A* search algorithm


- The Program takes an input for the START state and GOAL state configurations from the user, interactively. 
- Keep track of the tiles through coordinates(i, j), where i(0, 1, 2) is the row coordinates and j(0, 1, 2) the column coordinates
- We use a heuristic(Manhattan priority function) to ensure that the next chosen possible state has a minimal number of steps to get to the goal state

- *When entering the values of each coordinates, an empty coordinate(empty tile) will have a zero(0)*

# Steps to compile and execute this Program

- Ensure the main.py and State.py files are in the same directory
- Open a CLI in the same folder as the files above
- Type `python main.py` to run the main file. 
- Follow the prompts in the CLI
    - Enter the GOAL state config
    - Enter the START state config


# Sample START and GOAL configurations that works with my program:
### START STATE `(1, 8, 2, 0, 4, 3, 7, 6, 5)`

    [7, 6, 5]
    [0, 4, 3]
    [1, 8, 2]


### GOAL STATE `(1, 2, 3, 4, 5, 6, 7, 8, 0)`

    [7, 8, 0]
    [4, 5, 6]
    [1, 2, 3]
    
    
![image](https://user-images.githubusercontent.com/43353543/162666836-5c25e7b2-2483-47d1-84de-f87ffbe4c3cb.png)
![image](https://user-images.githubusercontent.com/43353543/162666868-9a9b484c-a45c-4536-8423-2172973331cd.png)


