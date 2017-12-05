""" This module contains classes that form the basis for part 2 of the assignment
    
    Refer the the coursework assignment for instructions on how to complete this part. 
"""
import math
import sys

class Point:

    def __init__(self, fx, fy):
        self._x = fx
        self._y = fy

    @property
    def x(self):
        """_x getter"""
        return self._x

    @property
    def y(self):
        """_y getter"""
        return self._y

    @x.setter
    def x(self, fx):
        """_x setter"""
        self._x = fx

    @y.setter
    def y(self, fy):
        """_y setter"""
        self._y = fy

    def distance(self, vPoint):
        return math.sqrt(((self._x-vPoint.x)**2)+((self._y - vPoint.y)**2))


class Shape:
    """This class is a convenient place to store the tolerance variable"""
    TOLERANCE = 1.0e-6


class Circle(Shape):

    def __init__(self, vCentre, fRadius):
        self._centre = vCentre
        self._radius = fRadius
        self._shapetype = "circle"

    def __str__(self):
        return ("This circle has its centre at ({centrex},{centrey}) and a radius of {radius}."
                .format(centrex=str(self._centre.x), centrey=str(self._centre.y), radius=str(self._radius)))

    @property
    def centre(self):
        """_centre getter"""
        return self._centre

    @property
    def radius(self):
        """_radius getter"""
        return self._radius

    @centre.setter
    def centre(self, vCentre):
        """_centre setter"""
        self._centre = fCentre

    @radius.setter
    def radius(self, fRadius):
        """_radius setter"""
        self._radius = fRadius

    def area(self):
        return 3.14*(self.radius**2)

    def compare(self, shape):
        if self.area() == shape.area():
            return 0
        elif self.area() < shape.area():
            return -1
        else:
            return 1

    def _envelopCircle(self, vCentre, fRadius):
        # dist <= R-r (R>=r)
        if (self._radius >= fRadius
                and self._centre.distance(vCentre) <= (self._radius - fRadius)):
            return True
        else:
            return False

    def envelops(self, shape):
        if shape.getShapeType() == "square":
            # caculate circumcircle
            ccmcircle_centre = Point(
                shape.topleft.x + shape.length/2, shape.topleft.y - shape.length/2)
            ccmcircle_radius = (shape.length/2) / math.sin(math.pi/4)
            return self._envelopCircle(ccmcircle_centre, ccmcircle_radius)
        elif shape.getShapeType() == "circle":
            return self._envelopCircle(shape.centre, shape.radius)
        else:
            # default result
            return False

    def equals(self, circle):
        if (self._centre.x - circle.centre.x < self.TOLERANCE
                and self._centre.y - circle.centre.y < self.TOLERANCE
                and self._radius - circle.radius < self.TOLERANCE):
            return True
        else:
            return False

    def getShapeType(self):
        return self._shapetype


class Square(Shape):

    def __init__(self, pTopLeft, fLength):
        self._topleft = pTopLeft
        self._length = fLength
        self._shapetype = "square"

    def __str__(self):
        return ("This square's top left corner is at ({topleftx},{toplefty}) and the side length is {length}"
                .format(topleftx=str(self._topleft.x), toplefty=str(self._topleft.y), radius=str(self._length)))

    @property
    def topleft(self):
        return self._topleft

    @property
    def length(self):
        return self._length

    @topleft.setter
    def topleft(self, pTopLeft):
        self._topleft = pTopLeft

    @length.setter
    def length(self, fLength):
        self._length = fLength

    def area(self):
        return self._length**2

    def compare(self, shape):
        if self.area() == shape.area():
            return 0
        elif self.area() < shape.area():
            return -1
        else:
            return 1

    def _envelopSqure(self, vTopleft, fLength):
        # l1 > dx + l2 && l1 > dy + l2. dx dy represent distance between two
        # topleft points in x and y axis
        if(self._length >= abs(vTopleft.x - self._topleft.x) + fLength
                and self._length >= abs(self._topleft.y - vTopleft.y) + fLength):
            return Trues
        else:
            return False

    def envelops(self, shape):
        if shape.getShapeType() == "square":
            return self._envelopSqure(shape.topleft, shape.length)
        elif shape.getShapeType() == "circle":
            # expand squre
            expand_topleft = Point(
                shape.centre.x - shape.radius, shape.centre.y + shape.radius)
            expand_length = 2 * shape.radius
            return self._envelopSqure(expand_topleft, expand_length)
        else:
            # default result
            return False

    def equals(self, square):
        if(self._topleft.x - square.topleft.x < self.TOLERANCE
           and self._topleft.y - square.topleft.y < self.TOLERANCE
           and self._length - square.length < self.TOLERANCE):
            return True
        else:
            return False

    def getShapeType(self):
        return self._shapetype


class Assignment:

    def __init__(self):
        # use a dictionary store all shapes, each key index a list of shapes in
        # this type
        self._shapes_dictionary = {}

    def _addNewShape(self, tResult):
        new_point = Point(float(tResult[1]), float(tResult[2]))
        if float(tResult[3]) >= Shape.TOLERANCE:
            if tResult[0] == 'square':
                new_shape = Square(new_point, float(tResult[3]))
                self._shapes_dictionary[tResult[0]].append(new_shape)
            elif tResult[0] == 'circle':
                new_shape = Circle(new_point, float(tResult[3]))
                self._shapes_dictionary[tResult[0]].append(new_shape)

    def analyse(self, szFilename):
        try:
            shapes = open(szFilename, 'r')
        except IOError:
            print 'cannot open file: ', szFilename  # catch exception if file can't open
        else:
            while True:
                shape = shapes.readline()
                if shape:
                    result = shape.strip().split(' ')
                    if self._shapes_dictionary.has_key(result[0]):
                        self._addNewShape(result)
                    else:
                        self._shapes_dictionary[result[0]] = []
                        self._addNewShape(result)
                else:
                    break  # break in end

    def shape_count(self):
        count = 0
        for key in self._shapes_dictionary:
            count += len(self._shapes_dictionary[key])
        return count

    def circle_count(self):
        return len(self._shapes_dictionary["circle"])

    def square_count(self):
        return len(self._shapes_dictionary["square"])

    def max_circle_area(self):
        max_area = 0.0
        for circle in self._shapes_dictionary["circle"]:
            temp_area = circle.area()
            max_area = max_area if max_area > temp_area else temp_area
        return max_area

    def min_circle_area(self):
        min_area = self._shapes_dictionary["circle"][0].area()
        for circle in self._shapes_dictionary["circle"]:
            temp_area = circle.area()
            min_area = min_area if min_area < temp_area else temp_area
        return min_area

    def max_square_area(self):
        max_area = 0.0
        for square in self._shapes_dictionary["square"]:
            temp_area = square.area()
            max_area = max_area if max_area > temp_area else temp_area
        return max_area

    def min_square_area(self):
        min_area = self._shapes_dictionary["square"][0].area()
        for square in self._shapes_dictionary["square"]:
            temp_area = square.area()
            min_area = min_area if min_area < temp_area else temp_area
        return min_area

    def mean_circle_area(self):
        mean_area = 0.0
        for circle in self._shapes_dictionary["circle"]:
            mean_area += circle.area()
        return mean_area/len(self._shapes_dictionary["circle"])

    def mean_square_area(self):
        mean_area = 0.0
        for square in self._shapes_dictionary["square"]:
            mean_area += square.area()
        return mean_area/len(self._shapes_dictionary["square"])

    def std_dev_circle_area(self):
        std_dev = 0.0
        for circle in self._shapes_dictionary["circle"]:
            std_dev += (circle.area() - self.mean_circle_area())**2
        return math.sqrt(std_dev/len(self._shapes_dictionary["circle"]))

    def std_dev_square_area(self):
        std_dev = 0.0
        for square in self._shapes_dictionary["square"]:
            std_dev += (square.area() - self.mean_square_area())**2
        return math.sqrt(std_dev/len(self._shapes_dictionary["square"]))

    def median_circle_area(self):
        sort_circles = sorted(self._shapes_dictionary["circle"])
        return sort_circles[len(self._shapes_dictionary["circle"]) / 2].area()

    def median_square_area(self):
        sort_squares = sorted(self._shapes_dictionary["square"])
        return sort_squares[len(self._shapes_dictionary["square"]) / 2].area()


if __name__ == "__main__":
    # You should add your own code heere to test your work
    print "=== Testing Part 2 ==="
    assignment = Assignment()
    if len(sys.argv) > 1:
        assignment.analyse(sys.argv[1])
    else:
        file_path = raw_input("Please enter a file path:")
        assignment.analyse(file_path)
    print "Dataset has {} shapes".format(assignment.shape_count())
    print "Dataset has {} circles".format(assignment.circle_count())
    print "Dataset has {} squares".format(assignment.square_count())
    print "Maximum area of circle in Dataset is {}".format(assignment.max_circle_area())
    print "Minimum area of circle in Dataset is {}".format(assignment.min_circle_area())
    print "Maximum area of square in Dataset is {}".format(assignment.max_square_area())
    print "Minimum area of square in Dataset is {}".format(assignment.min_square_area())
    print "Mean area of circles in this Dataset is {}".format(assignment.mean_circle_area())
    print "Mean area of square in this Dataset is {}".format(assignment.mean_square_area())
    print "std_dev of circle areas in this Dataset is {}".format(assignment.std_dev_circle_area())
    print "std_dev of square areas in this Dataset is {}".format(assignment.std_dev_square_area())
    print "Median area of circle in Dataset is {}".format(assignment.median_circle_area())
    print "Median area of square in Dataset is {}".format(assignment.median_square_area())

    shape1 = assignment._shapes_dictionary["square"][1]
    shape2 = assignment._shapes_dictionary["square"][2]
    shape3 = assignment._shapes_dictionary["circle"][1]
    shape4 = assignment._shapes_dictionary["circle"][2]

    print shape1.envelops(shape2)
    print shape3.envelops(shape4)
    print shape1.envelops(shape3)

    print shape1.equals(shape2)
    print shape1.equals(shape1)
    print shape3.equals(shape4)
    print shape3.equals(shape3)
    print shape1.topleft.distance(shape2.topleft)