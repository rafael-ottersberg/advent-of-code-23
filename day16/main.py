import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

parts = '/\\-|'

global_grid = set()
searched = set()

def trace_ray(dir, coord, cols, rows, dim):
    global searched
    global global_grid
    if (dir, coord) in searched:
        return None
    
    searched.add((dir, coord))

    #print(dir, coord)
    if dir.real:
        sorted_t = rows[int(coord.imag)][::int(dir.real)]

        next_tile = None
        for tile in sorted_t:
            if int(dir.real)*tile[0].real > int(dir.real)*coord.real and tile[1]!= 2:
                next_tile = tile
                break
        
        if next_tile is not None:
            next_coord = next_tile[0]

            for i in range(int(coord.real), int(next_coord.real)+int(dir.real), int(dir.real)):
                global_grid.add(complex(i, coord.imag))

            match next_tile[1]:
                case 3: # '|'
                    trace_ray(1j, next_coord, cols, rows, dim)
                    trace_ray(-1j, next_coord, cols, rows, dim)
                case 1: # '\'
                    trace_ray(dir.real*1j, next_coord, cols, rows, dim)
                case 0: # '/'
                    trace_ray(dir.real*-1j, next_coord, cols, rows, dim)
        else:
            if dir.real > 0:
                for i in range(int(coord.real), dim, int(dir.real)):
                    global_grid.add(complex(i, coord.imag))
            else:
                for i in range(int(coord.real), -1, int(dir.real)):
                    global_grid.add(complex(i, coord.imag))

    else:
        next_tile = None
        sorted_t = cols[int(coord.real)][::int(dir.imag)]
        for tile in sorted_t:
            if int(dir.imag)*tile[0].imag > int(dir.imag)*coord.imag and tile[1] != 3:
                next_tile = tile
                break
        
        if next_tile is not None:
            next_coord = next_tile[0]

            for i in range(int(coord.imag), int(next_coord.imag), int(dir.imag)):
                global_grid.add(complex(coord.real, i))

            match next_tile[1]:
                case 2: # '-'
                    trace_ray(1, next_coord, cols, rows, dim)
                    trace_ray(-1, next_coord, cols, rows, dim)
                case 1: # '\'
                    trace_ray(dir.imag*1, next_coord, cols, rows, dim)
                case 0: # '/'

                    trace_ray(dir.imag*-1, next_coord, cols, rows, dim)
        else:
            if dir.imag > 0:
                for i in range(int(coord.imag), dim, int(dir.imag)):
                    global_grid.add(complex(coord.real, i))
            else:
                for i in range(int(coord.imag), -1, int(dir.imag)):
                    global_grid.add(complex(coord.real, i))

def print_ray(lines, global_grid):
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            coord = col + row *1j
            if c in parts and coord in global_grid:
                print(c, end='')
            elif coord in global_grid:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def solution(input_file):
    global global_grid
    global searched

    global_grid = set()
    searched = set()

    lines = open(input_file, 'r').read().splitlines()
    dim = len(lines)

    cols = [[] for _ in range(dim)]
    rows = [[] for _ in range(dim)]

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            coord = col + row *1j
            if c in parts:
                tile = (coord, parts.index(c))
                cols[col].append(tile)
                rows[row].append(tile)
 
    for col in cols:
        col.sort(key=lambda x: x[0].imag)
    for row in rows:
        row.sort(key=lambda x: x[0].real)

    trace_ray(1, -1, cols, rows, dim)

    # print_ray(lines, global_grid)

    return len(global_grid) - 1

def solution2(input_file):
    global global_grid
    global searched

    global_grid = set()
    searched = set()

    lines = open(input_file, 'r').read().splitlines()
    dim = len(lines)

    cols = [[] for _ in range(dim)]
    rows = [[] for _ in range(dim)]

    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            coord = col + row *1j
            if c in parts:
                tile = (coord, parts.index(c))
                cols[col].append(tile)
                rows[row].append(tile)
 
    for col in cols:
        col.sort(key=lambda x: x[0].imag)
    for row in rows:
        row.sort(key=lambda x: x[0].real)

    energ = 0
    for i in range(dim):
        coord = complex(i, -1)
        global_grid = set()
        searched = set()
        trace_ray(1j,coord,cols, rows, dim)
        energ = max(energ, len(global_grid))

        coord = complex(i, dim)
        global_grid = set()
        searched = set()
        trace_ray(-1j,coord,cols, rows, dim)
        energ = max(energ, len(global_grid))
    
        coord = complex(-1, i)
        global_grid = set()
        searched = set()
        trace_ray(1,coord,cols, rows, dim)
        energ = max(energ, len(global_grid))

        coord = complex(dim, i)
        global_grid = set()
        searched = set()
        trace_ray(-1,coord,cols, rows, dim)
        energ = max(energ, len(global_grid))

    return energ - 1

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))