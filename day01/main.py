import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

import numpy as np
import pandas as pd

def solution(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0
    for line in lines:
        for i in range(len(line)):
            try:
                number_l = int(line[i])
                break

            except:
                pass
            try:
                number_l = match_next_chars(line, i)
                assert number_l != None
                break
            except:
                pass
        for i in range(len(line)):
            try:
                number_r = int(line[-(i+1)])
                break
            except:
                pass
            try:
                number_r = match_next_chars(line, -(1+i))
                
                assert number_r != None
                break
            except:
                pass

        number = int(f'{number_l}{number_r}')
        result += number
    return result

def match_next_chars(line, index):
    nr_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for nr_str in nr_dict.keys():
        if line[index:index+len(nr_str)] == nr_str:
            return nr_dict[nr_str]
        



if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    print(solution(file_directory / 'test.txt'))
    print('\n*******************************\n')
    print(solution(file_directory / 'input.txt'))
