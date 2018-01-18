import random
import os.path
from functions import generate_next, show_board

class AI:
    def __init__(self):
        """
        This initialises a new ai with a:
        1) game_boards list to store
            all the games played so far.
        2) the ai's internal memory that
            stores all boards its seen
            in a dictionary.
        :return:
        """
        
        self.game_boards_current = []
        self.game_boards_memory = dict()    
        self.file_name = "memory.txt"
        
        # check if the file exists
        if os.path.isfile(self.file_name):
            self.load()

    def move(self, board):
        """
        Takes in a board and returns what index of
            board to play the next move.
        board:  a list of 9 spaces that signals a game board.
        :param board: list[]
        :return: int

        >>> ai = AI()
        >>> board = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        >>> index = ai.move(board)
        >>> print(index)
        0
        >>> len(ai.game_boards_current)
        1
        >>> board_better = [0, 2, 0, 0, 1, 0, 0, 0, 0]
        >>> board_better_key = str(board_better)
        >>> ai.game_boards_memory[board_better_key] = 5
        >>> index = ai.move(board)
        >>> print(index)
        1
        """

        # generate all possible next moves
        next_moves_list = generate_next(board)

        # figure out the best move
        # get a random index
        index = random.randint(0, len(next_moves_list)-1)
        best_move = next_moves_list[index]

        ##

        # return the index of where to play the next move
        return best_move[0]
                
    def get_board_value(self, board):
        """
        returns the value of that board in the computers memory.

        board:  a list of 9 spaces that signals a game board.
        :param board: list[]
        :return: int

        >>> ai = AI()
        >>> board = [0,0,0]
        >>> board_key = str(board)
        >>> ai.get_board_value(board_key)
        0
        >>> ai.game_boards_memory[board_key] = 5
        >>> ai.get_board_value(board_key)
        5
        """
        # use string representation as the key of the dictionary
        board_key = str(board)
        if board_key in self.game_boards_memory:
            value = self.game_boards_memory.get(board_key)
        else:
            value = 0.5
            self.game_boards_memory[board_key] = value

        return value

    def has_lost(self):
        pass

    def has_drawn(self):
        pass

    def has_won(self):
        pass
    
    def stop_learning(self):
        pass
        
    def start_learning(self):
        pass
    
    def stop_self_saving(self):
        pass
        
    def start_self_saving(self):
        pass

    def save(self):
        """
        Save the contents of the database into a file.

        :param file_name: str
        :return: number of entries saved
        """
        
        file_name = self.file_name
        entries = 0
        target_file = open(file_name, 'w')

        for key in self.game_boards_memory:
            target_file.write(str(key) + ":" + str(self.game_boards_memory[key]) + "\n")
            entries += 1

        target_file.close()

    def load(self):
        """
        Load the contents of a file into its database (dict)

        :param file_name: str
        :return: number of entries loaded
        """
        file_name = self.file_name
        entries = 0

        target_file = open(file_name, 'r')

        for line in target_file:
            temp_list = line.strip("\n").split(":")
            if len(temp_list) == 2:
                self.game_boards_memory[temp_list[0]] = float(temp_list[1])
                entries += 1

        return entries

    def get_memory(self):
        """
        Return a string representation of the ai's memory
        :return:
        """
        s = ""
        for board_key in self.game_boards_memory:
            s += (str(board_key) + "\n" + str(self.game_boards_memory[board_key]) + "\n")
        return s




