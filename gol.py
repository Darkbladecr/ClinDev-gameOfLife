"""Game of Life.

If an unoccupied cell has three neighbours, then an organism is born.
If an occupied cell has two or three neighbours, then the organism survives to the next generation.
If an occupied cell has zero through eight neighbours, excluding 2 and 3,
the organism dies either due to loneliness (zero or one neighbour)
or overcrowding (0, 1, 4, 5, 6, 7, 8).
"""
import os
import random
import time


def clear():
    """Clear console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
            # Build random grid based on rows and columns given
            self.gen = [[]]
            for r in range(row):
                self.gen[0].append(list())
                for i in range(column):
                    self.gen[0][r].append(int(round(random.random())))

    def __neighbors(self, row, column):
        """Calculate number of neighbors."""
        # Remove count if life in cell
        neighbors = 0 - self.gen[-1][row][column]

        if row == 0:
            rowRange = range(0, 2)
        elif row == len(self.gen[-1]) - 1:
            rowRange = range(-1, 1)
        else:
            rowRange = range(-1, 2)

        if column == 0:
            colRange = range(0, 2)
        elif column == len(self.gen[-1][0]) - 1:
            colRange = range(-1, 1)
        else:
            colRange = range(-1, 2)

        for i in rowRange:
            for j in colRange:
                neighbors = neighbors + self.gen[-1][row + i][column + j]
        return neighbors

    def __nextGen(self):
        """Generate the generation's grid and append to list if not at the end."""
        if self.limit is True:
            return
        temp = list()
        for row in range(len(self.gen[-1])):
            temp.append(list())
            for col in range(len(self.gen[-1][0])):
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
        else:
            self.gen.append(temp)

    def nGen(self, n):
        """Fastforward n number of generations and return grid."""
        if n < 0:
            return "You are not the Great Spirit so you lack the ability to reverse time in this universe."
        elif n + 1 > len(self.gen):
            for i in range(len(self.gen), n + 1):
                self.__nextGen()
        return self.grid(n)

    def grid(self, n=-1):
        """Print grid for n generation or otherwise for latest one."""
        if n + 1 > len(self.gen):
            n = -1
        # Print Generation number
        if n == -1:
            string = "Generation {}\n".format(len(self.gen) - 1)
        else:
            string = "Generation {}\n".format(n)
        # Print top row legend
        legend = range(1, len(self.gen[n][0]) + 1)
        digits = len(str(len(legend)))
        legendStr = " "
        for num in legend:
            spacer = " " * (digits - len(str(num)))
            legendStr = legendStr + " {}{}".format(spacer, str(num))
        string += "{}\n".format(legendStr)
        # Print grid and column legend
        for i, r in enumerate(self.gen[n]):
            # Right spacing for multiple digits
            rowString = "{}".format(" " * digits).join([" " if c == 0 else "*" for c in r])
            if digits > 1:
                spacer = " " * (digits - len(str(i + 1)))
                string += "{}{} {}\n".format(spacer, i + 1, rowString)
            else:
                string += "{} {}\n".format(i + 1, rowString)
        return string

    def play(self, n=None):
        """Play all the generations until you hit the limit, or a particular n generation."""
        if type(n) is int:
            print(self.nGen(n))
        else:
            if self.limit is True:
                for i in range(len(self.gen)):
                    print(self.nGen(i))
                    time.sleep(1)
                    clear()
            else:
                i = 0
                while self.limit is False:
                    grid = self.nGen(i)
                    if self.limit is False:
                        print(grid)
                        time.sleep(1)
                        clear()
                        i = i + 1


clear()
# Standard Game of Life
g = GOL()
g.play()
# Larger Game of Life
# g = GOL(20, 20)
# g.play(100)
# Huge Game of Life
# g = GOL(100, 100)
# g.play(10)
