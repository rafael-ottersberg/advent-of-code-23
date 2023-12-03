import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

import numpy as np
import pandas as pd

colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solution(input_file):
    result = 0
    lines = helper.read_file_lines(input_file, strip_lines=True)
    for line in lines:
        pass

    return result


def solution2(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0


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