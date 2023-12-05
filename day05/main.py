import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper
import numpy as np


def solution(input_file):
    lines = open(input_file, 'r').read().splitlines()
    result = 0
    
    sts = {}
    stf = {}
    ftw = {}
    wtl = {}
    ltt = {}
    tth = {}
    htl = {}

    maps = [sts, stf, ftw, wtl, ltt, tth, htl]

    map_count = -1
    for i, line in enumerate(lines):
        if line == '':
            continue
        if i == 0:
            seeds = [int(nr) for nr in line.split(': ')[1].split()]
            continue

        if 'map:' in line:
            map_count += 1
            continue

        numbers = [int(nr) for nr in line.split()]

        difference = numbers[0]-numbers[1]

        maps[map_count][(numbers[1], numbers[1]+numbers[2])] = difference


    result = np.inf
    for seed in seeds:
        a = seed
        for m in maps:
            for f in m:
                if a >= f[0] and a < f[1]:
                    a += m[f]
                    break

        result = min(result, a)

    return result

def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()
    result = 0
    
    sts = {}
    stf = {}
    ftw = {}
    wtl = {}
    ltt = {}
    tth = {}
    htl = {}

    maps = [sts, stf, ftw, wtl, ltt, tth, htl]

    map_count = -1
    for i, line in enumerate(lines):
        if line == '':
            continue
        if i == 0:
            seeds = [int(nr) for nr in line.split(': ')[1].split()]
            continue

        if 'map:' in line:
            map_count += 1
            continue

        numbers = [int(nr) for nr in line.split()]
        difference = numbers[1]-numbers[0]
        maps[map_count][(numbers[0], numbers[0]+numbers[2])] = difference


    z = 0
    while True:
        a = z
        for m in reversed(maps):
            for f in m:
                if  a >= f[0] and a < f[1]:
                    a += m[f]
                    break

        for i, s in enumerate(seeds):
            if i % 2 == 0:
                if a >= seeds[i] and a < seeds[i] + seeds[i+1]:
                    return z
                    
        z += 1


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