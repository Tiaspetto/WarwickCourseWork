import itertools


# python dictionary class achived by using hash table, so it's search
# complexity is O(1)
MoseCodeDict = {".-": 'A',
                "-...": 'B',
                "-.-.": 'C',
                "-..": 'D',
                ".": 'E',
                "..-."	: 'F',
                "--.": 'G',
                "....": 'H',
                "..": 'I',
                ".---": 'J',
                "-.-": 'K',
                ".-..": 'L',
                "--": 'M',
                "-.": "N",
                "---": "O",
                ".--.": "P",
                "--.-": "Q",
                ".-.": "R",
                "...": "S",
                "-": "T",
                "..-": "U",
                "...-": "V",
                ".--": "W",
                "-..-": "X",
                "-.--": "Y",
                "--..": "Z",
                ".----": "1",
                "..---": "2",
                "...--": "3",
                "....-": "4",
                ".....": "5",
                "-....": "6",
                "--...": "7",
                "---..": "8",
                "----.": "9",
                "-----": "0"
                }


class MorseCodeTreeNode:

    def __init__(self, cElem=""):
        self.elem = cElem
        self.lchild = None
        self.rchild = None


class ReverseMorseCodeTree:

    def __init__(self):
        self.root = MorseCodeTreeNode()

# Use Recursion build tree
    def add(self, parent, czCode, myChar):
        if len(czCode) == 0:
            return

        code = czCode[0]
        subcode = czCode[1:]

        if code == ".":
            if parent.lchild == None:
                parent.lchild = MorseCodeTreeNode()
            if len(subcode) == 0:
                parent.lchild.elem = myChar  # find place, put char into node
            self.add(parent.lchild, subcode, myChar)
        elif code == "-":
            if parent.rchild == None:
                parent.rchild = MorseCodeTreeNode()
            if len(subcode) == 0:
                parent.rchild.elem = myChar  # find place, put char into node
            self.add(parent.rchild, subcode, myChar)
    
    def creat(self):
        for k,v in MoseCodeDict.items():
    	    self.add(self.root, k[::-1], v)

    def _get(self,parent,czCode):
    	if len(czCode) == 0:
            return parent.elem
        
        code = czCode[0]
        subcode = czCode[1:]
         
        if code == ".":
        	return self._get(parent.lchild,subcode)
        elif code == "-":
            return self._get(parent.rchild,subcode)
        elif code == "x":
        	return (self._get(parent.lchild,subcode),self._get(parent.rchild,subcode))

    def get(self, czCode):
        return self._get(self.root, czCode)


def morseDecode(inputStringList):
    myCharlist = []
    myWord = ""
    for myChar in inputStringList:
        myCharlist.append(MoseCodeDict[myChar])
    return myWord.join(myCharlist)


def morsePartialDecode(inputStringList):
    morse_tree = ReverseMorseCodeTree()
    morse_tree.creat()

    myCharlist = []
    myWord = ""
    for myChar in inputStringList:
        myCharlist.append(morse_tree.get(myChar))
    
    print myCharlist
    #dictionaryFileLoc = './dictionary.txt'


class Maze:

    def __init__(self):
        """
        Constructor - You may modify this, but please do not add any extra parameters
        """

        pass

    def addCoordinate(self, x, y, blockType):
        """
        Add information about a coordinate on the maze grid
        x is the x coordinate
        y is the y coordinate
        blockType should be 0 (for an open space) of 1 (for a wall)
        """

        # Please complete this method to perform the above described function
        pass

    def printMaze(self):
        """
        Print out an ascii representation of the maze.
        A * indicates a wall and a empty space indicates an open space in the maze
        """

        # Please complete this method to perform the above described function
        pass

    def findRoute(self, x1, y1, x2, y2):
        """
        This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
        It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
        in the order in which the coordinates must be followed
        If no route is found, return an empty list
        """
        pass


def morseCodeTest():
    """
    This test program passes the morse code as a list of strings for the word
    HELLO to the decode method. It should receive a string "HELLO" in return
    """

    hello = ['....', '.', '.-..', '.-..', '---']
    print morseDecode(hello)


def partialMorseCodeTest():
    """
    This test program passes the partial morse code as a list of strings 
    to the morsePartialDecode method
    """

    # This is a partial representation of the word TEST, amongst other
    # possible combinations
    #test = ['x', 'x', 'x..', 'x']
    #print morsePartialDecode(test)

    # This is a partial representation of the word DANCE, amongst other
    # possible combinations
    #dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    #print morsePartialDecode(dance)

    dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    morsePartialDecode(dance)

def mazeTest():
    """
    This sets the open space coordinates for the example
    maze in the assignment.
    The remainder of coordinates within the max bounds of these specified coordinates
    are assumed to be walls
    """
    myMaze = Maze()
    myMaze.addCoordinate(1, 0, 0)
    myMaze.addCoordinate(1, 1, 0)
    myMaze.addCoordinate(7, 1, 0)
    myMaze.addCoordinate(1, 2, 0)
    myMaze.addCoordinate(2, 2, 0)
    myMaze.addCoordinate(3, 2, 0)
    myMaze.addCoordinate(4, 2, 0)
    myMaze.addCoordinate(6, 2, 0)
    myMaze.addCoordinate(7, 2, 0)
    myMaze.addCoordinate(4, 3, 0)
    myMaze.addCoordinate(7, 3, 0)
    myMaze.addCoordinate(4, 4, 0)
    myMaze.addCoordinate(7, 4, 0)
    myMaze.addCoordinate(3, 5, 0)
    myMaze.addCoordinate(4, 5, 0)
    myMaze.addCoordinate(7, 5, 0)
    myMaze.addCoordinate(1, 6, 0)
    myMaze.addCoordinate(2, 6, 0)
    myMaze.addCoordinate(3, 6, 0)
    myMaze.addCoordinate(4, 6, 0)
    myMaze.addCoordinate(5, 6, 0)
    myMaze.addCoordinate(6, 6, 0)
    myMaze.addCoordinate(7, 6, 0)
    myMaze.addCoordinate(5, 7, 0)

morseCodeTest()
partialMorseCodeTest()
# mazeTest()
