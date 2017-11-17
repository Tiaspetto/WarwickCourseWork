"""
This module represents some classes for a simple word game.

There are a number of incomplete methods in the which you must implement to make fully functional.

About the game board!
The board's tiles are indexed from 1 to N, and the first square (1,1) is in the top left.
A tile may be replaced by another tile, hence only one tile may occupy a space at any one time.
"""


class LetterTile:
    """ This class is complete. You do not have to do anything to complete this class """

    def __init__(self, letter):
        self.letter = letter.lower()

    def get_letter(self):
        """ Returns the letter associatedd with this tile. """
        return self.letter

    def get_score(self):
        """ Returns the score asscoiated with the letter tile """
        return {
            'a':  1,
            'b':  2,
            'c':  2,
            'd':  3,
            'e':  1,
            'f':  3,
            'g':  2,
            'h':  3,
            'i':  1,
            'j':  3,
            'k':  2,
            'l':  3,
            'm':  5,
            'n':  3,
            'o':  1,
            'p':  2,
            'q':  2,
            'r':  3,
            's':  1,
            't':  1,
            'u':  1,
            'v':  3,
            'w':  3,
            'x':  5,
            'y':  3,
            'z':  5,
            '-':  0
        }[self.letter]


class GameBoard:
    """ This class represents the gameboard itself.
        You are requried to complete this class.
    """

    def __init__(self, nWidth, nHeight):
        """ The constructor for setting up the gameboard """
        # expand boarders
        self._gameboard = [([LetterTile('-')] * (nWidth + 2))
                           for i in range(nHeight+2)]
        self._width = nWidth
        self._height = nHeight

    def set_tile(self, nx, ny, Tile):
        self._gameboard[ny][nx] = Tile

    def get_tile(self, nx, ny):
        return self._gameboard[ny][nx].get_letter()

    def remove_tile(self, nx, ny):
        self._gameboard[ny][nx] = LetterTile('-')

    def get_words(self):
        """ Retuns a list of the words on the board sorted in alphabetic order."""
        word_list = []
        start_hor_node = []
        start_ver_node = []
        for ny in range(1, self._height + 1):
            for nx in range(1, self._width + 1):
                if self._gameboard[ny][nx].get_letter() != '-':
                    # check horizon
                    if(self._gameboard[ny][nx+1].get_letter() != '-' and self._gameboard[ny][nx-1].get_letter() == '-'):
                        node = [ny, nx]
                        start_hor_node.append(node)
                    # check vertical
                    if(self._gameboard[ny+1][nx].get_letter() != '-' and self._gameboard[ny-1][nx].get_letter() == '-'):
                        node = [ny, nx]
                        start_ver_node.append(node)

        for hor in start_hor_node:
            new_word = []
            index = 0
            while(self._gameboard[hor[0]][hor[1]+index].get_letter() != '-'):
                new_word.append(self._gameboard[hor[0]][
                                hor[1]+index].get_letter())
                index += 1

            word_list.append(''.join(new_word))

        for ver in start_ver_node:
            new_word = []
            index = 0
            while(self._gameboard[ver[0]+index][ver[1]].get_letter() != '-'):
                new_word.append(
                    self._gameboard[ver[0]+index][ver[1]].get_letter())
                index += 1
            word_list.append(''.join(new_word))

        return sorted(word_list)

    def top_scoring_words(self):
        """ Returns a list of the top scoring words. 
            If there is a single word, then the function should return a single item list.
            If multilpe words share the highest score, then the list should contain the words sorted alphabetically.     
        """
        word_value_dict = {}
        start_hor_node = []
        start_ver_node = []
        for ny in range(1, self._height + 1):
            for nx in range(1, self._width + 1):
                if self._gameboard[ny][nx].get_letter() != '-':
                    # check horizon
                    if(self._gameboard[ny][nx+1].get_letter() != '-' and self._gameboard[ny][nx-1].get_letter() == '-'):
                        node = [ny, nx]
                        start_hor_node.append(node)
                    # check vertical
                    if(self._gameboard[ny+1][nx].get_letter() != '-' and self._gameboard[ny-1][nx].get_letter() == '-'):
                        node = [ny, nx]
                        start_ver_node.append(node)

        for hor in start_hor_node: # qury horzion word node
            new_word = []
            index = 0
            score = 0
            while(self._gameboard[hor[0]][hor[1]+index].get_letter() != '-'):
                new_word.append(self._gameboard[hor[0]][
                                hor[1]+index].get_letter())
                score += self._gameboard[hor[0]][hor[1]+index].get_score()
                index += 1
            word_value_dict[''.join(new_word)] = score

        for ver in start_ver_node: # qury vertical word node
            new_word = []
            index = 0
            score = 0
            while(self._gameboard[ver[0]+index][ver[1]].get_letter() != '-'):
                new_word.append(
                    self._gameboard[ver[0]+index][ver[1]].get_letter())
                score += self._gameboard[ver[0]+index][ver[1]].get_score()
                index += 1
            word_value_dict[''.join(new_word)] = score

        max_score = max(zip(word_value_dict.values(), word_value_dict.keys()))

        result = []
        for k, v in word_value_dict.items():
            if v == max_score[0]:
                result.append(k)

        return sorted(result)

    def print_board(self):
        """ Prints a visual representation of the board
            Please use the - character for unused spaces
        """
        for ny in range(1, self._height + 1):
            print '\n'
            for nx in range(1, self._width + 1):
                print self._gameboard[ny][nx].get_letter(),
        print '\n'

    def letters_placed(self):
        count = 0
        for ny in range(1, self._height + 1):
            for nx in range(1, self._width + 1):
                if self._gameboard[ny][nx].get_letter() != '-':
                    count += 1

        return count

if __name__ == "__main__":
    """ This is just a sample for testing you might want to add your own tests here """
    board = GameBoard(10, 10)

    d = LetterTile("d")
    e = LetterTile("e")
    m = LetterTile("m")
    o = LetterTile("o")
    u = LetterTile("u")
    c = LetterTile("c")
    k = LetterTile("k")

    board.set_tile(1, 1, d)
    board.set_tile(2, 1, e)
    board.set_tile(3, 1, m)
    board.set_tile(4, 1, o)
    board.set_tile(5, 1, k)
    board.set_tile(3, 2, u)
    board.set_tile(3, 3, c)
    board.set_tile(4, 3, k)
    board.set_tile(3, 4, k)
    board.set_tile(4, 4, u)
    board.set_tile(5, 4, c)
    board.set_tile(6, 4, m)

    print "There are {} letters placed on the board.".format(board.letters_placed())

    print "=== Words ==="
    for word in board.get_words():
        print word

    board.print_board()


    print "=== Top Scoring Words ==="
    for word in board.top_scoring_words():
        print word