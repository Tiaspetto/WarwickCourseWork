import itertools
import numpy as np

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
        for k, v in MoseCodeDict.items():
    	    self.add(self.root, k[::-1], v)

    def _get(self, parent, czCode):
    	if len(czCode) == 0:
            return parent.elem

        code = czCode[0]
        subcode = czCode[1:]

        if code == ".":
        	return self._get(parent.lchild, subcode)
        elif code == "-":
            return self._get(parent.rchild, subcode)
        elif code == "x":
        	return (self._get(parent.lchild, subcode), self._get(parent.rchild, subcode))

    def get(self, czCode):
        return self._get(self.root, czCode)


class WordTierTreeNode:

    def __init__(self, myChar=""):
    	self.elem = myChar
    	self.childNodes = [None]*26


class WordTireTree:

    def __init__(self):
        self.root = WordTierTreeNode()

    def add(self, parent, szWord):
        if len(szWord) == 0:
    	    return
         
        # ASCII difference as index
    	index = ord(szWord[0].lower()) - ord('a')

    	if index < 26 and index >= 0:
    	    if parent.childNodes[index] == None:
    		    parent.childNodes[index] = WordTierTreeNode(szWord[0])
            subWord = szWord[1:]
            self.add(parent.childNodes[index], subWord)
        else:  # ignore uncoded char
            subWord = szWord[1:]
            self.add(parent, subWord)

    def creat(self):
        dictionaryFileLoc = './dictionary.txt'
        try:
            word_list = open(dictionaryFileLoc, 'r')
        except IOError:
            print 'cannot open file: ', szFilePath  # catch exception if file can't open
        else:
            while True:
                word = word_list.readline()
                if word and len(word) > 1:
                    self.add(self.root, word.strip())
                else:
                    break  # break in end

    def checkValidWord(self, szWord):
        return self._checkValidWord(self.root, szWord)

    def _checkValidWord(self, parent, szWord):
    	if len(szWord) == 0:
    	    return True
    	index = ord(szWord[0].lower()) - ord('a')

    	if parent.childNodes[index] == None:
    		return False

    	subWord = szWord[1:]
    	return self._checkValidWord(parent.childNodes[index], subWord)

morse_tree = ReverseMorseCodeTree()
morse_tree.creat()

word_tier_tree = WordTireTree()
word_tier_tree.creat()


def morseDecode(inputStringList):
    myCharlist = []
    myWord = ""
    for myChar in inputStringList:
        myCharlist.append(MoseCodeDict[myChar])
    return myWord.join(myCharlist)


def wordCombinations(charLsit):
    total = reduce(lambda x, y: x * y, map(len, charLsit))
    retList = []

    for i in range(0, total):
        step = total
        tempItem = []
        for l in charLsit:
            step /= len(l)
            tempItem.append(l[i/step % len(l)])
        retList.append(tuple(tempItem))
    return retList


def morsePartialDecode(inputStringList):
    myCharlist = []
    myWord_list = []
    for myChar in inputStringList:
        myCharlist.append(morse_tree. get(myChar[::-1]))

    for word in wordCombinations(myCharlist):
    	tempWord = ""
        myWord_list.append(tempWord.join(list(word)))

    valid_words = []

    for word in myWord_list:
        if word_tier_tree.checkValidWord(word):
       	    valid_words.append(word)

    return valid_words


class Maze:

    def __init__(self):
        """
        Constructor - You may modify this, but please do not add any extra parameters
        """
        self.maxHeight = 1
        self.maxWidth = 1
        self.maze = np.array([1])

    def expandMaze(self, nWidth, nHeight):
    	expandW = nWidth-self.maxWidth
        while(expandW > 0):
            self.maze = np.column_stack((self.maze, np.ones(self.maxHeight)))
            expandW -= 1
        self.maxWidth = nWidth

        expandH = nHeight-self.maxHeight
        while(expandH > 0):
        	self.maze = np.row_stack((self.maze, np.ones(self.maxWidth)))
        	expandH -= 1
        self.maxHeight = nHeight

    def addCoordinate(self, x, y, blockType):
        """
        Add information about a coordinate on the maze grid
        x is the x coordinate
        y is the y coordinate
        blockType should be 0 (for an open space) of 1 (for a wall)
        """
        if ((x+1) > self.maxWidth) or ((y+1) > self.maxHeight):
            self.expandMaze(max(self.maxWidth, x+1), max(self.maxHeight, y+1))

        self.maze[y, x] = blockType
        # Please complete this method to perform the above described function
        pass

    def printMaze(self):
        """
        Print out an ascii representation of the maze.
        A * indicates a wall and a empty space indicates an open space in the maze
        """
        for row in self.maze:
            for elem in row:
                if elem == 1:
                    print "*",
                else:
                    print " ",
            print "\n"
        # Please complete this method to perform the above described function
    
 
    def findRoute(self, x1, y1, x2, y2):
        path = [(x1,y1)]
        self.maze[y1, x1] = -1

        while path:
            x, y = path[-1]		
            if(x,y) == (x2,y2):
                break
   
            Flag = False #flag to know wether find path or not
            for xi, yi in[(0,-1),(0,1),(-1,0),(1,0)]:
                if x+xi<self.maxWidth and y+yi<self.maxHeight and self.maze[y+yi, x+xi] == 0:
                    self.maze[y+yi, x+xi] = -1
                    path.append((x+xi, y+yi))
                    Flag = True
                    break
            
            # if not find path, pop dead end 
            if Flag == False:
                path.pop()
        return path


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
    # test = ['x', 'x', 'x..', 'x']
    # print morsePartialDecode(test)

    # This is a partial representation of the word DANCE, amongst other
    # possible combinations
    # dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    # print morsePartialDecode(dance)
    
    test = ['x', 'x', 'x..', 'x']
    print morsePartialDecode(test)
    dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    print morsePartialDecode(dance)

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
    myMaze.addCoordinate(8, 8, 1)
    myMaze.printMaze()
    print myMaze.findRoute(1,0,7,6)

morseCodeTest()
partialMorseCodeTest()
mazeTest()
