# The Game of Life

## Introduction

On behalf of the [Clinical Developers Club](https://clinicaldevelopers.org)
this programming challenge involving a famous systems behaviour model is
released as of 11 September 2017. The original problem and model was created by
[John Conway](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## The Challenge

As a health science professional you have recently joined a research team at
the local university. The research team is staffed with highly-skilled,
well-educated academics and practioners. Unfortunately, nobody can implement
the algorithm to model the lifecycle of the strange organism found attached to
an artefact brought back from Mars. To be truthful none of the research teams
working on two continents have been able to deliver a bug-free (pardon the pun)
solution capable of handling an arbitrary number of generations nor a boundless
world. The project sponsor has threatened to cease funding this research
project.

Your role is to implement the algorithm in any programming language available on
their 1980s era mainframe computer system. There is litte documentation about
the mainframe and the programming languages supported. The sole document is a
sales brochure found in the file cabinet in which the vendor claims "[o]ver the
next few years additional programming languages will be available." Part of
this data/programming challenge is to identify a programming language in
existence between 1980 and 1989 regardless of the type of computer system
(mainframe computer, mini-computer, personal computer, time-sharing computer).
In the event you cannot locate an interpreter or compiler for the selected
programming language, you may just write your solution in that language, using
correct syntax, and marking the submission as "execute by hand." Dr. Conway,
research advisor to the team, cannot provide any assistance due to "national
security." I heard unpaid parking fines keep him from traveling to your
research laboratory.

### Birth, Survival, and Death

The evolutionary rules are simple but brutal for organisms in this universe.

- If an unoccupied cell has three neighbours, then an organism is born.
- If an occupied cell has two or three neighbours, then the organism survives to the next generation.
- If an occupied cell has zero through eight neighbours, excluding 2 and 3, the organism dies either due to loneliness (zero or one neighbour) or overcrowding (0, 1, 4, 5, 6, 7, 8).

These rules are a modified version of his original model. The accuracy of the
simplified rule set is sufficiently close to the original algorithm that over
the long run the output eventually converges, in theory.

## Examples

Formatted screen captures of Generation 0 (Seed) and Generation 1 are in the
images subdirectory.

Generation 0 (Seed)

<pre>
   1  2  3  4  5  6  7  8

1        *  *           *

2     *  *  *        *  *

3  *           *  *     *

4     *  *     *  *  *  *

5  *  *     *     *  

6  *     *     *  *  *  

7     *  *  *  *  *  *  *

8  *     *        *  *
</pre>

Generation 1

<pre>
   1  2  3  4  5  6  7  8

1     *     *        *  *

2     *           *     *

3  *

4        *              *

5  *                    *

6  *                    *

7  *                    *

8        *              *
</pre>

The struggle for survival continues for some number, n, of generations. Your
solution should be able to show the survival state for any positive value of n.
If n = 0, then output the initial state (Generation 0 - Birth). If n is
negative, then output a warning, "You are not the Great Spirit so you lack the
ability to reverse time in this universe."

## Implementation Requirements

For this challenge, either a paper-based solution representing at least five
(5) generations of evolution must be shown or for a programming solution an
arbitrary number of generations must be supported. For those implementing a
solution using a programming language, let's tackle a language you have not
used in years or a language you have never used before. It is time to stretch
your clinical developer muscles. Bonus points for the geekiest solution.

## gol.py

This is a python script that is built around a class object. Simply instantiate
a new class with `QOL()` and fast-forward the number of generations you would
like with the `nGen()` method. An example is included at the end of the file.
Also there are two different methods for calculating the number of neighbors
an organism has.

You are now able to change the grid size of the Game of Life by giving two
numbers when creating the class `QOL(rows, columns)`. I have included an example
at the end of the script with a grid size of 20x20.
