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
    cards = []
    for i, line in enumerate(lines):
        p1, p2 = line.split(': ')[1].split(' | ')
        n1, n2 = [], []
        for n in p1.split(' '):
            if n != '':
                n1.append(int(n))
        for n in p2.split(' '):
            if n != '':
                n2.append(int(n))

        n1 = set(n1)
        n2 = set(n2)

        overlap = n1.intersection(n2)

        cards.append(overlap)
        len_o = len(list(overlap))
        if len_o > 0:
            r=0
            r = 1 * 2**(len_o-1)
            result += r


    result2 = 0
    factors = np.ones(len(lines), dtype=np.int64)

    for i, c in enumerate(cards):
        result2 += factors[i]
        for j in range(len(c)):
            factors[i+j+1] += factors[i]


    return result, result2


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if True:
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if False:
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))