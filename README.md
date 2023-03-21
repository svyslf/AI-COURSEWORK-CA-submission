# MAZE SOLVER for AI & Applications CA 2023

## Instructions to run the code: 

The `maze_main.py` file in the source code runs the project. It will run the specified algorithm on all the mazes that have been provided and output required stats for the respective mazes, and provide a total runtime. 

After navigating to the correct directory, use the following command line arguments in terminal:

For the DFS implementation, run ->

	python3 maze_main.py DFS

For the A-STAR implementation, run -> 

    python3 maze_main.py A-STAR

The further exploration section references "optimized" versions of these scripts which can be found in the "faster" folder and can be ran in the command line using the following flag: 

	python3 maze_main.py DFS-faster
	python3 maze_main.py A-STAR-faster

If no argument is provided after calling the maze_main.py file, the following error will show:

	usage: maze_main.py [-h] algorithm
	maze_main.py: error: the following arguments are required: algorithm

If the wrong argument is provided, (i.e. mistyped algorithm name), the following error will show: 

	Incorrect algorithm name, the following are valid: DFS, A-STAR, DFS-faster, 
	A-STAR-faster

If an erronous maze with no end or start is provided, the console will output 

	"No exit from maze found! :("

	"No entrance to maze found! :("

And continue solving the other mazes. 

if a maze no valid path is provided, the console will output

	"There exists no valid path in this maze!" 
and exit.

Maze-corrupt.txt is provided to test this functionality.

If an incorrect filename is provided, the console will output

	"This file cannot be found!"

Note: To test custom maze.txt files, add them to the project directory, and add their name to the "files" array in maze_main.py, line 16

## Author 
Vihan Sharma , 2nd year computer science undergraduate, University of Exeter