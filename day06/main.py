import numpy as np
import helper
import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)


def solution(input_file):
    result = 1
    lines = open(input_file, 'r').read().splitlines()
    numbers = map(int, lines[0].split()[1:])
    distances = map(int, lines[1].split()[1:])

    print(numbers, distances)

    for tim, rec in zip(numbers, distances):
        count = 0
        for t in range(1, tim):
            res = t * (tim - t)
            if res > rec:
                count += 1

        result *= count

    return result


def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()
    numbers = int(lines[0].split(':')[1].replace(' ', ''))
    results = int(lines[1].split(':')[1].replace(' ', ''))

    start = 0
    count = 0
    for t in range(1, numbers):
        res = t * (numbers - t)
        if res > results:
            start = t
            count += 1

    result = numbers + 1 - 2 * start

    return result


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1:  # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 0:  # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))
