'''
    Implementation of a node in a search tree for the eight game
    Written by: Bjornar Tessem
'''
import copy

class EightGameNode:
    '''
    A representation of an eight game node with the board as a 3x3 list (array/table) with
    the numbers 0 to 8 found at the tiles in the game
    In addition it contains the index of 0, which represent the empty space in the board
    '''

    DEFAULT_BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    '''
    A default board if another board is not specified in the constructor
    '''

    def legal_board(the_board):
        '''
        Checks if a board is a legal board
        :return: True if the board is a legal eight game board
        '''
        if len(the_board) != 3:
            # the list need to have the right dimensions
            return False
        if len(the_board[0]) != 3 or len(the_board[1]) != 3 or len(the_board[2]) != 3:
            # the sublists need to have the right dimension
            return False
        all_pieces = frozenset(range(9))
        # the final set of tiles need to contain the set from 0 to 8
        board_pieces = set()
        for row in the_board:
            for el in row:
                # add each value from the_board to a set
                board_pieces.add(el)
        if all_pieces != board_pieces:
            # if the created set is not equal to the all_pieces set there is something wrong
            return False
        return True

    def get_empty(board):
        '''
        Finds the position of the empty space in the board
        :return: a dictionary with the row and col of the empty space
        '''
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return {"row": i, "col": j}

    def __init__(self, the_board = DEFAULT_BOARD):
        '''
        Makes a new node from an initial board
        :param the_board: the initial board
        '''
        if EightGameNode.legal_board(the_board):
            # if the board is legal go on
            self.board = the_board
        else:
            # otherwise use the default board
            self.board = EightGameNode.DEFAULT_BOARD
        self.empty = EightGameNode.get_empty(self.board)
        # set the empty space of the board

    def move_left(self):
        if self.empty['col'] > 0:
            new_node = copy.deepcopy(self)
            row, col = new_node.empty['row'], new_node.empty['col']
            new_node.board[row][col], new_node.board[row][col - 1] = new_node.board[row][col - 1], new_node.board[row][
                col]
            new_node.empty = {'row': row, 'col': col - 1}
            return new_node
        return None

    def move_right(self):
        if self.empty['col'] < 2:
            new_node = copy.deepcopy(self)
            row, col = new_node.empty['row'], new_node.empty['col']
            new_node.board[row][col], new_node.board[row][col + 1] = new_node.board[row][col + 1], new_node.board[row][
                col]
            new_node.empty = {'row': row, 'col': col + 1}
            return new_node
        return None

    def move_up(self):
        if self.empty['row'] > 0:
            new_node = copy.deepcopy(self)
            row, col = new_node.empty['row'], new_node.empty['col']
            new_node.board[row][col], new_node.board[row - 1][col] = new_node.board[row - 1][col], new_node.board[row][
                col]
            new_node.empty = {'row': row - 1, 'col': col}
            return new_node
        return None

    def move_down(self):
        if self.empty['row'] < 2:
            new_node = copy.deepcopy(self)
            row, col = new_node.empty['row'], new_node.empty['col']
            new_node.board[row][col], new_node.board[row + 1][col] = new_node.board[row + 1][col], new_node.board[row][
                col]
            new_node.empty = {'row': row + 1, 'col': col}
            return new_node
        return None

    def __str__(self):
        '''
        Makes a string representation of the board
        :return: the string representation
        '''
        result = ''
        for row in self.board:
            result = result + '|'
            for el in row:
                if el == 0:
                    result = result + " "
                else:
                    result = result + str(el)
            result = result + '|\n'
        return result + ''

    def __eq__(self, other):
        '''
        checks if two boards are the same
        :param other: the board to check against
        :return: True if self and other board are identical in values
        '''
        for i in range (3):
            for j in range (3):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

    def __hash__(self):
        '''
        A hash function for the purpose of efficient set representation of board positions
        Used in EightGameSpace's visited set
        :return: a hash function for self
        '''
        b = self.board
        return (b[0][0]*1 +
                b[0][1]*2 +
                b[0][2]*3 +
                b[1][0]*4 +
                b[1][1]*5 +
                b[1][2]*6 +
                b[2][0]*7 +
                b[2][1]*8 +
                b[2][2]*9)

    def hamming_distance(self,other):
        '''
        Returns the number of tiles which are not correctly placed compared to other (which may be the goal)
        :param other: the other board to compare to
        :return: the number of tiles which are not correctly placed
        '''
        dist = 0
        # Your code for measuring so called Hamming distance

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j] and self.board[i][j] != 0:
                    dist += 1
        return dist


    def manhattan_distance(self,other):
        '''
        Returns the sum of the number of moves a tile must do to move from where it is in self to
        where it is in the other board if there were no other tiles on the board
        :param other: the other board to compare to
        :return: the sum of the number of moves for each tile
        '''
        dist = 0
        # Your code for measuring so called Manhattan distance

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    # Find the position of the current tile in the other board
                    for x in range(3):
                        for y in range(3):
                            if other.board[x][y] == self.board[i][j]:
                                dist += abs(i - x) + abs(j - y)
        return dist






if __name__ == "__main__":
    '''
    code for checking the moves
    '''
    s = EightGameNode([[0,1,2],[3,4,5],[6,7,8]])
    print(s)
    s = s.move_right()
    print(s)
    s = s.move_left()
    print(s)
    s = s.move_down()
    print(s)
    s = s.move_up()
    print(s)