"""Game of Life.

If an unoccupied cell has three neighbours, then an organism is born.
If an occupied cell has two or three neighbours, then the organism survives to the next generation.
If an occupied cell has zero through eight neighbours, excluding 2 and 3,
the organism dies either due to loneliness (zero or one neighbour)
or overcrowding (0, 1, 4, 5, 6, 7, 8).
"""


class GOL:
    """Game of Life class."""

    def __init__(self):
        """Initialize seed generation."""
        self.gen = [[0, 0, 1, 1, 0, 0, 0, 1],
                    [0, 1, 1, 1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 1, 1, 0, 1],
                    [0, 1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 0, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 0, 0, 1, 1, 0]]

    def __neighbors(self, row, column):
        """Calculate number of neighbors."""
        # Remove count if life
        neighbors = 0 - self.gen[row][column]

        if row == 0:
            rowRange = xrange(0, 2)
        elif row == 7:
            rowRange = xrange(-1, 1)
        else:
            rowRange = xrange(-1, 2)

        if column == 0:
            colRange = xrange(0, 2)
        elif column == 7:
            colRange = xrange(-1, 1)
        else:
            colRange = xrange(-1, 2)

        for i in rowRange:
            for j in colRange:
                neighbors = neighbors + self.gen[row + i][column + j]
        return neighbors

    def __neighbors2(self, row, column):
        """Alt calculate number of neighbors."""
        rStart = row - 1
        rEnd = row + 2
        if row == 0:
            rStart = 0
        elif row == 7:
            rEnd = 8

        cStart = column - 1
        cEnd = column + 2
        if column == 0:
            cStart = 0
        elif column == 7:
            cEnd = 8

        rows = self.gen[rStart:rEnd]
        grid = list()
        for r in rows:
            grid.append(r[cStart:cEnd])
        flatten = [i for j in grid for i in j]
        neighbors = sum(flatten) - self.gen[row][column]
        return neighbors

    def __nextGen(self):
        """Generate the next generation grid."""
        temp = list()
        for row in xrange(8):
            temp.append(list())
            for col in xrange(8):
                n = self.__neighbors(row, col)
                if self.gen[row][col] == 0:
                    if n == 3:
                        temp[row].append(1)
                    else:
                        temp[row].append(0)
                elif n == 2 or n == 3:
                    temp[row].append(1)
                else:
                    temp[row].append(0)
        self.gen = temp

    def nGen(self, n):
        """Fastforward n number of generations."""
        if n < 0:
            print("You are not the Great Spirit so you lack the ability to reverse time in this universe.")
        elif n == 0:
            self.grid()
        else:
            for i in range(n):
                self.__nextGen()
            self.grid()

    def grid(self):
        """Print grid of life."""
        legend = [str(i) for i in range(1, 9)]
        print("  {}".format(" ".join(legend)))
        for i, r in enumerate(self.gen):
            rowString = " ".join([" " if c == 0 else "*" for c in r])
            print("{} {}".format(i + 1, rowString))

g = GOL()
g.nGen(1000)
