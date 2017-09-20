"""Game of Life.

If an unoccupied cell has three neighbours, then an organism is born.
If an occupied cell has two or three neighbours, then the organism survives to the next generation.
If an occupied cell has zero through eight neighbours, excluding 2 and 3,
the organism dies either due to loneliness (zero or one neighbour)
or overcrowding (0, 1, 4, 5, 6, 7, 8).
"""
import random


class GOL:
    """Game of Life class."""

    def __init__(self, row=None, column=None):
        """Initialize seed generation.

        Use default grid of 8x8 or otherwise values given at institation.
        """
        self.limit = False
        if row is None or column is None:
            self.gen = [[[0, 0, 1, 1, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 1, 1],
                        [1, 0, 0, 0, 1, 1, 0, 1],
                        [0, 1, 1, 0, 1, 1, 1, 1],
                        [1, 1, 0, 1, 0, 1, 0, 0],
                        [1, 0, 1, 0, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 0, 1, 1, 0]]]
        else:
            self.gen = [[]]
            for r in xrange(row):
                self.gen[0].append(list())
                for i in xrange(column):
                    self.gen[0][r].append(int(round(random.random())))

    def __neighbors(self, row, column):
        """Calculate number of neighbors."""
        # Remove count if life
        neighbors = 0 - self.gen[-1][row][column]

        if row == 0:
            rowRange = xrange(0, 2)
        elif row == len(self.gen[-1]) - 1:
            rowRange = xrange(-1, 1)
        else:
            rowRange = xrange(-1, 2)

        if column == 0:
            colRange = xrange(0, 2)
        elif column == len(self.gen[-1][0]) - 1:
            colRange = xrange(-1, 1)
        else:
            colRange = xrange(-1, 2)

        for i in rowRange:
            for j in colRange:
                neighbors = neighbors + self.gen[-1][row + i][column + j]
        return neighbors

    def __neighbors2(self, row, column):
        """Alt calculate number of neighbors and ~x0.5 slower."""
        rStart = row - 1
        rEnd = row + 2
        if row == 0:
            rStart = 0
        elif row == len(self.gen[-1]) - 1:
            rEnd = len(self.gen[-1])

        cStart = column - 1
        cEnd = column + 2
        if column == 0:
            cStart = 0
        elif column == len(self.gen[-1][0]) - 1:
            cEnd = len(self.gen[-1])

        rows = self.gen[-1][rStart:rEnd]
        grid = list()
        for r in rows:
            grid.append(r[cStart:cEnd])
        flatten = [i for j in grid for i in j]
        neighbors = sum(flatten) - self.gen[-1][row][column]
        return neighbors

    def __nextGen(self):
        """Generate the next generation grid."""
        if self.limit is True:
            return
        temp = list()
        for row in xrange(len(self.gen[-1])):
            temp.append(list())
            for col in xrange(len(self.gen[-1][0])):
                n = self.__neighbors(row, col)
                if self.gen[-1][row][col] == 0:
                    if n == 3:
                        temp[row].append(1)
                    else:
                        temp[row].append(0)
                elif n == 2 or n == 3:
                    temp[row].append(1)
                else:
                    temp[row].append(0)
        # Grid not changing, so no need to re-run expensive operations.
        if self.gen[-1] == temp:
            self.limit = True
        self.gen.append(temp)

    def nGen(self, n):
        """Fastforward n number of generations."""
        if n < 0:
            print("You are not the Great Spirit so you lack the ability to reverse time in this universe.")
        elif n == 0:
            self.grid(n)
        else:
            for i in range(n):
                self.__nextGen()
            self.grid(n)

    def grid(self, n=-1):
        """Print grid of life."""
        if n > len(self.gen):
            n = -1
        # Print top row legend
        legend = range(1, len(self.gen[n][0]) + 1)
        digits = len(str(len(legend)))
        legendStr = " "
        for num in legend:
            spacer = " " * (digits - len(str(num)))
            legendStr = legendStr + " {}{}".format(spacer, str(num))
        print(legendStr)
        # Print grid and column legend
        for i, r in enumerate(self.gen[n]):
            # Right spacing for multiple digits
            rowString = "{}".format(" " * digits).join([" " if c == 0 else "*" for c in r])
            if digits > 1:
                spacer = " " * (digits - len(str(i + 1)))
                print("{}{} {}".format(spacer, i + 1, rowString))
            else:
                print("{} {}".format(i + 1, rowString))


# Standard Game of Life
g = GOL()
g.nGen(22)
# Larger Game of Life
t = GOL(20, 20)
t.grid()
t.nGen(200)
# Huge Game of Life
g = GOL(100, 100)
g.nGen(500)
