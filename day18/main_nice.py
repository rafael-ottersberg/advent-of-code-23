import os
import sys
import pathlib

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

    coord = 0
    path_length = 0

    inside_calc = 0
    for i, line in enumerate(lines):
        dir, dist, _ = line.split(' ')
        dist = int(dist)

        last_coord = coord
        coord += directions_vec[dir] * dist

        path_length += dist

        if dir in 'UD':
            diff = coord - last_coord
            inside_calc += coord.real * diff.imag

    inside_calc = abs(inside_calc)
    inside = inside_calc - path_length / 2 + 1    
    return int(path_length + inside)


def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()

    coord = 0
    path_length = 0
    directions = 'RDLU'

    inside_calc = 0
    for i, line in enumerate(lines):
        _, _, color = line.split(' ')        
        hex_dist, hex_dir = color[2:-2], color[-2:-1]
        dist = int(hex_dist, 16)
        dir = directions[int(hex_dir)]

        last_coord = coord
        coord += directions_vec[dir] * dist

        path_length += dist

        if dir in 'UD':
            diff = coord - last_coord
            inside_calc += coord.real * diff.imag

    inside_calc = abs(inside_calc)
    inside = inside_calc - path_length / 2 + 1    
    return int(path_length + inside)

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