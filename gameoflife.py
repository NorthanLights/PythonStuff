# Works on Windows platform only.

from copy import deepcopy
from time import sleep
from os import system
from random import randrange

ROW = 20
COL = 20
MOVE = {'U': lambda x, y: (x-1, y), 'D': lambda x, y: (x+1, y),
        'R': lambda x, y: (x, y+1), 'L': lambda x, y: (x, y-1),
        'RU': lambda x, y: (x-1, y+1), 'LU': lambda x, y: (x-1, y-1),
        'RD': lambda x, y: (x+1, y+1), 'LD': lambda x, y: (x+1, y-1)}

_dftcoords = ((1, 0), (2, 1), (2, 2), (1, 2), (0, 2))

def random_grid(freq):
    return [[2 if randrange(freq) == freq-1 else 0 for _ in range(COL)]
                                                       for _ in range(ROW)]

def new_grid(coords):
    grid = [[0 for _ in range(COL)] for _ in range(ROW)]
    for i, j in coords:
        grid[i][j] = 2
    return grid

def display(grid):
    for i in range(ROW):
        for j in range(COL):
            print(chr(grid[i][j]), end='')
        print()

def neighbors_num(grid, coord):
    count = 0
    for direction in MOVE:
        x, y = MOVE[direction](*coord)
        if grid[x%ROW][y%COL] == 2:
            count += 1
    return count
        
def next_grid(grid):
    new_grid = deepcopy(grid)
    for i in range(ROW):
        for j in range(COL):
            neighbors = neighbors_num(grid, (i, j))
            if neighbors == 3:
                new_grid[i][j] = 2
            elif neighbors < 2 or neighbors > 3:
                new_grid[i][j] = 0
    grid[:] = new_grid

def gameoflife(random=False, freq=3, coords=_dftcoords, sleepsecs=0.05):
    grid = random_grid(freq) if random \
                        else new_grid(coords)
    while True:
        system('cls')
        display(grid)
        sleep(sleepsecs)
        next_grid(grid)
    
gameoflife(True)
