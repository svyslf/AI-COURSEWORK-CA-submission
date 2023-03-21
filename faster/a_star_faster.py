from queue import PriorityQueue
from maze_decipher import adjacents
import heapq

def h_score(end, current):
    """
    Returns the estimated distance from current cell to the goal using manhattan distance formula. 

    args: (tuple) end - coordinates of the end point of maze 
          (tuple) current - coordinates of current point in traversal 

    returns: (int) h_score calculated from end and current
    """

    return abs(end[0] - current[0]) + abs(end[1] - current[1])


def a_star_faster(representation, start, end):
    """
    Returns the shortest path found between the start and end node. 
    Uses the actual distance from the start to current node and an estimated distance from current node to the end.

    args:   (list) representation - 2d array representation of the maze
            (tuple) start - start coordinates 
            (tuple) end- end coordinates
    returns: (dictionary) fwd_path - path found through the maze 

    """
    g_score = {}
    f_score = {}

    for row in range(len(representation)):
        for block in range(len(representation[0]) - 1):
            g_score[(row, block)] = float("inf")
            f_score[(row, block)] = float("inf")

    g_score[start] = 0
    f_score[start] = g_score[start] + h_score(end, start)

    open_list = []
    heapq.heappush(open_list, (f_score[start], start))

    path_taken = {}
    while len(open_list) != 0:
        current_position = heapq.heappop(open_list)
        if current_position[1] == end:
            break

        neighbours = adjacents(representation, current_position[1][0], current_position[1][1])
    
        for neighbour in neighbours:
            g_score_new = g_score[current_position[1]] + 1

            if g_score_new < g_score[neighbour]:
                path_taken[neighbour] = current_position[1]
                g_score[neighbour] = g_score_new
                f_score[neighbour] = g_score_new + h_score(end, neighbour)

                if neighbour not in open_list:
                    heapq.heappush(open_list, (f_score[neighbour], neighbour))
    try:
        fwd_path = {}
        goal = end
        while ( goal != start ):                        # Reverse the dictionary key pairs to eliminate failed paths that were explored
            fwd_path[path_taken[goal]] = goal
            goal = path_taken[goal]
        fwd_path[(0, 0)] = start                        # Reversing the dict avoids the start node, this adds it back in with some abritrary key (0,0)
        print(f"Explored %s nodes and found path with length: %s" % (len(path_taken), (len(fwd_path))))
    except KeyError:
        print("There exists no valid path in this maze!")
    # print(list(reversed(fwd_path.values())))      # This line will print out the path from start to end in readable format
    return fwd_path
