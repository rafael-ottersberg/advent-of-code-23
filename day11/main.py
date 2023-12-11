import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    galaxies = []
    gr, gc = set(), set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                galaxies.append(j+i*1j)
                gr.add(i)
                gc.add(j)

    ar = set(list(range(len(lines))))
    ac = set(list(range(len(lines[0]))))
    no_galaxy_r = ar - gr
    no_galaxy_c = ac - gc

    new_galaxies = galaxies.copy()

    increment = 999999 # 1 for pt1

    for c in no_galaxy_c:
        for i in range(len(galaxies)):
            if galaxies[i].real > c:
                new_galaxies[i] += increment
    for r in no_galaxy_r:
        for i in range(len(galaxies)):
            if galaxies[i].imag > r:
                new_galaxies[i] += increment * 1j

    for g in new_galaxies:
        for g2 in new_galaxies:
            dist = g2-g
            result += abs(dist.real) + abs(dist.imag)

    return int(result / 2)

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))