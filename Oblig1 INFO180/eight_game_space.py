'''
    Implementation of the search space for the eight game
    Written by: Bjornar Tessem
'''
from copy import deepcopy



from astar_path import AStarPath
from eight_game_node import EightGameNode
from queue import PriorityQueue


class EightGameSpace:
    '''
    This class is a representation of the search space for the eight game.
    It allows for an A* search for an optimal solution
    '''

    DEFAULT_GOAL = EightGameNode(EightGameNode.DEFAULT_BOARD)
    '''
    The standard goal for the eight game
    '''

    def add_move(self,new_paths, path, node):
        '''
        Adds a single new path to a set of paths contained in new_paths
        Copies path and adds node into the new path
        :param new_paths: the list of paths to add the new path to
        :param path: the path to which a next move is added
        :param node: the eight game node that is generated from the last node of path
        :return:
        '''
        if node is not None:
            new_path = deepcopy(path)
            # make a deep copy of path
            new_path.append(node)
            # append node to this path
            h_value = self.h(node)
            # get the h_value of the new node, i.e., estimate of shortest number of moves to the goal
            new_paths.append(AStarPath(new_path, h_value))
            # makes a AStarPath object with the new path and the h_value


    def h(self,node):
        '''
        :param node: the node for which a h-value shall be computed 
        :return: the h-value
        '''''
        # Here you can select h-functions by commenting out the ones you do not want
        #return 0 # no heuristic is used, implies breadth-first-search
        #return node.hamming_distance(self.goal) # choose a hamming distance heuristic
        return node.manhattan_distance(self.goal) # choose a manhattan-distance heuristic

    def __init__(self, the_goal = DEFAULT_GOAL):
        '''
        initialize the eight game space
        :param the_goal:
        '''
        self.visited = set()
        # a hash set of positions that have already been visited in the game tree
        self.goal = the_goal
        # a goal position, by default the DEFAULT_GOAL
        self.start = None
        # no startnode specified
        self.frontier = PriorityQueue()
        # the search frontier is a priority queue

    def is_goal(self, node):
        '''
        checks if a node is a goal in this search
        :param node: the node to check
        :return: True if node is a goal
        '''
        if self.goal == node:
            return True
        else:
            return False

    def get_new_paths(self, astar_path):
        '''
        makes a list of paths that are new paths based on the astar_path
        only generates new paths if last node is not visited
        adds the last node of the path to the visited set
        :param astar_path: the path to add new paths for
        :return: the set of new paths
        '''
        new_paths = []
        last = astar_path.path[-1]
        # find the last node of the astar_path
        if not self.is_visited(last):
            # only do this if last is not already visited

            # make moves where the empty space moves in different
            # directions
            self.add_move(new_paths, astar_path.path, last.move_left())
            self.add_move(new_paths, astar_path.path, last.move_right())
            self.add_move(new_paths, astar_path.path, last.move_up())
            self.add_move(new_paths, astar_path.path, last.move_down())

            self.visited.add(last)
            # add last to the set of visited nodes
        return new_paths

    def is_visited(self, node):
        '''
        Check if a node is alredy visited
        :param node: the node to check
        :return: True if node has already been visited
        '''
        return node in self.visited

    def solve(self,start):
        '''
        Solves the eight game from a node from start
        :param start: the start node of the search
        :return: the astar path that is a solution
        '''
        self.start = start
        # initialise the start
        self.frontier.put(AStarPath([start]))
        # initialise the search frontier
        print("Frontier size")
        while not self.frontier.empty():
            # if frontier is empty there is no solution
            # otherwise continue search
            print("\r", self.frontier.qsize(), end=' ')
            next_path = self.frontier.get()
            # get the next path from the frontier PriorityQueue
            last_node = next_path.path[-1]
            # get the last node of this path
            if self.is_goal(last_node):
                # if we have a solution
                print("\nNodes visited ", len(self.visited)+1)
                # print the number of nodes visited in the search space
                return next_path.path
                # and return the found path
            new_paths = self.get_new_paths(next_path)
            # else find the children for this path and put on the frontier
            for a_path in new_paths:
                self.frontier.put(a_path)
                print("\r",self.frontier.qsize(), end = ' ')

        return None



if __name__ == "__main__":
    '''
    Running the test of eight game space search
    '''

    space = EightGameSpace()
    # various start nodes to try out
    # solution = space.solve(EightGameNode([[1,2,3],[4,5,6],[7,8,0]]))
    # solution = space.solve(EightGameNode([[1,2,3],[4,0,6],[7,5,8]]))
    # solution = space.solve(EightGameNode([[0,1,2],[3,4,5],[6,7,8]]))
    # solution = space.solve(EightGameNode([[1,2,3],[7,4,5],[8,0,6]]))

    # These following two have the longest solution - 32 moves -
    # and may take some minutes even with the Manhattan heuristic
    # solution = space.solve(EightGameNode([[8,6,7],[2,5,4],[3,0,1]]))
    solution = space.solve(EightGameNode([[6,4,7],[8,5,0],[3,2,1]]))

    # Print the solution and the length of the solution
    if solution != None:
        print("Solution length: ", len(solution))
        for el in solution:
            print(el)
    else:
        print("\n","No solution")








