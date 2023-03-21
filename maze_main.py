from dfs import depth_first_search
from faster.dfs_faster import depth_first_search_faster
from a_star import a_star
from faster.a_star_faster import a_star_faster
from maze_decipher import represent, locate_start, locate_end
import time
import argparse


def main():
    '''
    Main function that runs the project and accepts command line arguments. 
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm")

    argument = parser.parse_args()

    files = ["maze-Small.txt", "maze-Medium.txt", "maze-Large.txt", "maze-Vlarge.txt"]

    allowed = ["DFS", "A-STAR", "DFS-faster", "A-STAR-faster"]
    if argument.algorithm not in allowed:
        print("Incorrect algorithm name, the following are valid: DFS, A-STAR, DFS-faster, A-STAR-faster ")
        exit()

    else:
        start_time_all = time.time()
        for file in files:
            print("\n")
            print("Searching", file, "using", argument.algorithm)
            try: 
                rep = represent(file)
            except FileNotFoundError:    
                print("This file cannot be found!")
                exit()

            start = locate_start(rep)
            end = locate_end(rep)

            if start == None:
                print("No entrance to maze found! :(")
                exit()

            if end == None: 
                print("No exit from maze found! :(") 
                exit()

            if argument.algorithm == "DFS":
                start_time = time.time()
                depth_first_search(rep, start, end)
                end_time = time.time() - start_time
                print("Time taken to execute:", end_time, "seconds \n")
            
            if argument.algorithm == "DFS-faster":
                start_time = time.time()
                depth_first_search_faster(rep, start, end)
                end_time = time.time() - start_time
                print("Time taken to execute:", end_time, "seconds \n")

            elif argument.algorithm == "A-STAR":
                start_time = time.time()
                a_star(rep, start, end)
                end_time = time.time() - start_time
                print("Time taken to execute:", end_time, "seconds \n")

            elif argument.algorithm == "A-STAR-faster":
                start_time = time.time()
                a_star_faster(rep, start, end)
                end_time = time.time() - start_time
                print("Time taken to execute:", end_time, "seconds \n")



        end_time_all = time.time() - start_time_all
        print("Time taken to execute all:", end_time_all, "seconds \n")



if __name__ == "__main__":
    main()
