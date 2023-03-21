from maze_decipher import adjacents_large


def depth_first_search_faster(representation:list, start:tuple, end:tuple):
    """
    The depth first search implementation that solves the given mazes 

    args:   (list) representation - 2d array representation of the maze
            (tuple) start - start coordinates 
            (tuple) end - end coordinates
    returns: (dictionary) fwd_path -  path found through the maze
    """
    to_explore = [start]
    explored = set(start)

    path_taken = {}

    while len(to_explore) > 0:
        current_position = to_explore.pop()

        y = current_position[0]
        x = current_position[1]

        if current_position == end:
            break

        # in the order of optimal movement => west, north, south, east
        neighbours = adjacents_large(representation, y, x)
        for neighbour in neighbours:
            if neighbour not in explored:
                path_taken[neighbour] = current_position
                to_explore.append(neighbour)
                explored.add(neighbour)
    try:
        fwd_path = {}
        goal = end
        while ( goal != start ):                        # Reverse the dictionary key pairs to eliminate failed paths that were explored 
            fwd_path[path_taken[goal]] = goal
            goal = path_taken[goal]
        fwd_path[(0, 0)] = start                        # Reversing the dict avoids the start node, this adds it back in w some abritrary key (0,0)
        print(f"Explored %s nodes and found path with length: %s" % (len(explored), (len(fwd_path))))

    except KeyError:
        print("There exists no valid path in this maze!")

#    print(list(reversed(fwd_path.values())))        # This will print out the path from start to end in readable format
    return fwd_path
