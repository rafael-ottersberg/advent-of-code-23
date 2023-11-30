import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
print(parent_directory)
sys.path.append(parent_directory)

import helper

import numpy as np
import pandas as pd

def solution(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    print(lines)


    return 0



if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    print(solution(file_directory / 'test.txt'))
    print('\n*******************************\n')
    print(solution(file_directory / 'input.txt'))
