import os
import sys
import pathlib
import math

import shapely

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper


directions_vec = {
    'U': -1j,
    'D': 1j,
    'R': 1,
    'L': -1
}



def solution(input_file):
    lines = open(input_file, 'r').read().splitlines()
    grid = dict()
    coord = 0
    for i, line in enumerate(lines):
        dir, dist, color = line.split(' ')

        for i in range(1, int(dist) + 1):
            coord += directions_vec[dir]
            grid[coord] = color


    coords = [(int(c.real), int(c.imag)) for c in grid.keys()]

    ring = shapely.Polygon(coords)

    print(ring.area + len(coords)/2+1)
    return 0

def are_neighbouring_directions_equal(lines, i):
    l = len(lines)
    d1 = lines[i - 1 % l].split(' ')[0]
    d2 = lines[i + 1 % l].split(' ')[0]
    #d1 = lines[i - 1 % l][-2]
    #d2 = lines[i + 1 % l][-2]
    return d1 == d2


def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()
    grid = dict()
    coord = 0
    
    up_down_ranges = dict()
    left_right_ranges = dict()
    on_edge = 0
    
    directions = 'RDLU'
    min_y = float('inf')
    max_y = float('-inf')
    for i, line in enumerate(lines):
        min_y = min(coord.imag, min_y)
        max_y = max(coord.imag, max_y)
        dir, dist, color = line.split(' ')
        dist = int(dist)
        
        #hex_dist, hex_dir = color[2:-2], color[-2:-1]
        #dist = int(hex_dist, 16)
        #dir = directions[int(hex_dir)]

        on_edge += dist
        if dir in 'UD':
            sign = 'U-D'.index(dir) - 1
            if int(coord.real) in up_down_ranges:
                up_down_ranges[int(coord.real)].append(range(int(coord.imag) + sign, int(coord.imag) + sign * (dist), sign))
            else:
                up_down_ranges[int(coord.real)] = [range(int(coord.imag) + sign, int(coord.imag) + sign * (dist), sign)]
        else:
            typ = are_neighbouring_directions_equal(lines, i)
            sign = 'L-R'.index(dir) - 1
            if int(coord.imag) in left_right_ranges:
                left_right_ranges[int(coord.imag)].append((range(int(coord.real), int(coord.real) + sign * (dist+1), sign), typ))
            else:
                left_right_ranges[int(coord.imag)] = [(range(int(coord.real), int(coord.real) + sign * (dist+1), sign), typ)]


        coord += directions_vec[dir] * dist


    inside = 0

    print(min_y, max_y)

    for y in range(int(min_y), int(max_y) + 1):
        if y % 100000 == 0: print(y)
        x_crossings = []
        for x in up_down_ranges:
            for rng in up_down_ranges[x]:
                if y in rng:
                    x_crossings.append(x)

        if y in left_right_ranges:
            x_crossings.extend(left_right_ranges[y])

        x_crossings = [(x if isinstance(x, int) else x[0].start, x) for x in x_crossings]
        x_crossings.sort()
        x_crossings = [x for _, x in x_crossings]
        
        first = None
        substract = 0
        for i in range(len(x_crossings)):
            next = x_crossings[i]
            if not isinstance(next, int):
                if not next[1]:
                    substract += len(next[0])
                    continue

            if first is None:
                first = next
                substract = 0

            else:
                second = next
                if not isinstance(first, int): first = max(first[0])
                if not isinstance(second, int): second = min(second[0])

                inside += second - first - 1 - substract
                first = None          
            
    return on_edge + inside

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))