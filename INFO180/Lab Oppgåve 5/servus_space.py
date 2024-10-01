'''
    Class for solving Servus the serving robot's planning problem. Number of legal states are 37800,
    so use a full depth first search (even though it may take som seconds)
'''
from queue import LifoQueue
import copy
from servus_state import NO_SNACK
import servus_state
from servus_state import ServusState

class ServusSpace:

    def __init__(self):
        '''
        initialize the servus search space
        :param the_goal:
        '''
        # self.visited = set()
        # a hash set of states that have already been visited in the search space
        self.best = None
        self.frontier = LifoQueue()
        # the search frontier is a stack (depth-first-search here)

    def is_goal(self,path):
        '''
        Checks if a path ends in a goal state
        :param path:
        :return: true if the end state is a goal
        '''
        state = path[-1][1]
        # path is a list of pairs of (action,state).
        # [-1] gets the last pair.
        # [1] gets the last state

        if len(path) == 1:
            # a special case. If there is nothing to deliver or pickup at tables we are finished
            # in that case we are already in a goal state so we do not need to move
            if (state.t1_full == 3 and state.t2_full == 3 and
                state.t1_empty == 0 and state.t2_empty == 0 and
                state.t1_snack == servus_state.FULL_SNACK and state.t2_snack == servus_state.FULL_SNACK):
                return True
            else:
                return False

        # the last (act,state) in the path, selecting the state
        # the goal is to get back to the kitchen and empty the hands
        if state.servus_loc != 'K':
            return False
        if len(state.servus_hands) > 0:
            return False
        return True

    def solve(self, start):
        '''
        Runs a depth-first search, but finds complete solutions and compare them according to how good they are
        :param start: start state
        :return: returns the best solution in a full depth-first search
        '''
        start_path = [('start', start)]
        self.frontier.put(start_path)  # frontier is a stack (LifoQueue)
        path = self.frontier.get()
        while path is not None:
            print(f"Exploring path: {path}")  # Debugging statement
            if self.is_goal(path):
                print(f"Goal found: {path}")  # Debugging statement
                # if path is a goal, check if it is better than the best so far
                self.check_best(path)
            else:
                the_state = path[-1][1]  # the last state in the path
                children = the_state.generate_children()
                for c in children:
                    if not self.on_path(c, path):
                        # child already is on path just ignore it
                        new_path = path + [c]  # Avoid deep copy
                        self.frontier.put(new_path)
            if self.frontier.empty():  # if frontier is empty we are finished
                path = None
            else:
                path = self.frontier.get()
        return self.best

    def on_path(self, c, path):
        # go through all (action,state) pairs and check if the state of c is equal to state
        for (act,state) in path:
            if c[1] == state: return True
        return False

    def check_best(self, path):
        # compares new paths to old ones
        if self.best is None:
            # if no path so far
            self.best = path
            return
        else:
            path_end = path[-1][1]
            # the end of the new path

            best_end = self.best[-1][1]
            # the end of the best path

            full_score_best = best_end.t1_full + best_end.t2_full
            full_score_path = path_end.t1_full + path_end.t2_full
            # number of full glasses at each table for new path and best so far

            empty_score_best = best_end.t1_empty + best_end.t2_empty
            empty_score_path = path_end.t1_empty + path_end.t2_empty
            # number of empty glasses at each table for new path and best so far

            if (full_score_path != full_score_best):
                # as many full glasses at tables as possible
                if full_score_path > full_score_best: self.best = path
                return

            elif (empty_score_path != empty_score_best):
                # as few empty glasses at tables as possible
                if empty_score_path < empty_score_best: self.best = path
                return

            elif self.check_snack_status(path_end, best_end):
                # as many full snacks as possible on the tables
                # and as few empty as possible
                # requires special programmed test
                self.best = path
                return

            elif len(path) < len(self.best):
                # shortest paths are best
                self.best = path
                return

            else:
                # path is not an improvement
                return

    def check_snack_status(self,path, best):
        # computes kind of score for snacks status
        # strange but it works

        p_score = 0
        # the new path's score
        b_score = 0
        # the best so far's score

        if path.t1_snack == servus_state.FULL_SNACK: p_score = p_score + 3
        if path.t2_snack == servus_state.FULL_SNACK: p_score = p_score + 3
        # new path: adds a score of 3 if snack is full at either table

        if path.t1_snack == servus_state.NO_SNACK: p_score = p_score + 1
        if path.t2_snack == servus_state.NO_SNACK: p_score = p_score + 1
        # new path: adds a score of 1 if snack is empty at either table

        if best.t1_snack == servus_state.FULL_SNACK: b_score = b_score + 3
        if best.t2_snack == servus_state.FULL_SNACK: b_score = b_score + 3
        # best so far: adds a score of 3 if snack is full at either table

        if best.t1_snack == servus_state.NO_SNACK: b_score = b_score + 1
        if best.t2_snack == servus_state.NO_SNACK: b_score = b_score + 1
        # best so far: adds a score of 1 if snack is empty at either table

        return p_score > b_score
        # if new path scores better it has a better snack status


if __name__ == "__main__":
    start = {
        "loc": 'K',  # Servus starts in the kitchen
        "hands": [],  # No items in hands
        "t1_full": 0,  # 0 full glasses at table 1
        "t1_empty": 2,  # 2 empty glasses at table 1
        "t2_full": 0,  # 0 full glasses at table 2
        "t2_empty": 2,  # 2 empty glasses at table 2
        "t1_snack": NO_SNACK,  # No snack at table 1
        "t2_snack": NO_SNACK  # No snack at table 2
    }
    # an initial state

    space = ServusSpace()
    # create a search space with solver algorithm

    start_state = ServusState(start)
    # create a start_state

    result = space.solve(start_state)
    # solve with the state given

    if result is None:
        print('No solution')
    else:
        # print the solution
        for (act, state) in result:
            print('{:20} {}'.format(act, state))