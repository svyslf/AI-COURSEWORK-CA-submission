from os import system
from termcolor import colored

PATH = "-"

def represent(file:str):
    '''
    Converts the maze into a 2d array representation for traversal

    arg: file path 

    return: 2d array representation of .txt file 

    '''
    with open(file, "r") as maze:
        two_d = [line.split() for line in maze]
        two_d = list(filter(None, two_d))
    return two_d


def print_clear(representation:list[list[str]], path:dict):
    '''
    Helper function that prints out the maze in readable format (used for debug)

    args: 2d array representation of the maze, and solution path. 

    return: prints the maze with the path 
    '''
    for row in range(len(representation)):        
        for block in range(len(representation[0])-1):
            if (row, block) in path.values():
                print(colored(representation[row][block], "green"), end=" ",)
                
            else:    
                print(representation[row][block], end=" ")
 
        print(representation[row][len(representation[row])-1])
        

def locate_start(representation:list[list[str]]): 
    '''
    Helper function to locate the start of the maze (assumes start will always be on row 0)

    arg: 2d array representation of the maze

    returns: tuple with coordinates of the starting point 
    '''
    for column in range(len(representation[0])): 
        if representation[0][column] == PATH:
            return (0, column)



def locate_end(representation:list[list[str]]):
    '''
    Helper function to locate the end of the maze (assumes start will always be on the last row)

    arg: 2d array representation of the maze

    returns: tuple with coordinates of the end point 
    '''
    last_row = len(representation)-1
    for column in range(len(representation[last_row])):
        if representation[last_row][column] == PATH:
            return (last_row, column)


def adjacents(representation:list[list[str]], x:int, y:int):
    '''
    Helper function that discovers valid paths in the given mazes 

    args: 2d array representation of the maze, x and y coordinates of that representation

    returns: list of valid neighbours 
    '''
    neighbours = []

    if representation[x][y-1] == "-":
        neighbours.append((x, y-1))

    if representation[x-1][y] == "-":
        neighbours.append((x-1, y))

    if representation[x+1][y] == "-":
        neighbours.append((x+1, y))
    
    if representation[x][y+1] == "-":
        neighbours.append((x, y+1))

    return neighbours


def adjacents_large(representation:list[list[str]], x:int, y:int):
    '''
    Experimental helper function that can be applied to larger mazes for time saves on DFS. 

    args: 2d array representation of the maze, x and y coordinates of that representation

    returns: list of valid neighbours 
    '''
    neighbours = []

    if representation[x-1][y] == "-":
        neighbours.append((x-1, y))

    if representation[x][y-1] == "-":
        neighbours.append((x, y-1))

    if representation[x][y+1] == "-":
        neighbours.append((x, y+1))

    if representation[x+1][y] == "-":
        neighbours.append((x+1, y))
    
        
    return neighbours