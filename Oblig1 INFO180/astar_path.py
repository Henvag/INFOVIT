'''
    Class representing a path in a search tree and its cost
    Written by Bjornar Tessem
'''


class AStarPath:
    '''
    The representation of an AStarPath
    '''

    def __init__(self, the_path = [], the_h = 0 ):
        '''
        Constructor for AStarPath
        :param the_path: the path as a list of EightGameNodes
        :param the_h: the h-value for the last node in the path
        '''
        self.path = the_path
        self.h = the_h

    def __lt__(self,other):
        '''
        Computes the total heuristic f for the AStarPath based on the length so far +
        the h-value. Used for ranking the paths in the PriorityQueue of the EightGameSpace solve method
        :param other: the one to compare with self
        :return: True if the total heuristic f for self is smaller than for other
        '''
        self_f = len(self.path)-1+self.h
        other_f = len(other.path) - 1 + other.h
        return self_f < other_f

