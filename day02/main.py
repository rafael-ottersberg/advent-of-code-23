import os
import sys
import pathlib
import time

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

import numpy as np
import pandas as pd

def solution(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0
    return result


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    print(helper.benchmark(solution)(file_directory / 'test.txt'))
    print('\n*******************************\n')
    print(helper.benchmark(solution)(file_directory / 'input.txt'))