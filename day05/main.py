import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

import numpy as np
import pandas as pd

def solution(input_file):
    lines = open(input_file, 'r').read().splitlines()
    result = 0
    for i, line in enumerate(lines):
        pass

    return result


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