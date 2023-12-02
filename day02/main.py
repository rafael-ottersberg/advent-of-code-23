import os
import sys
import pathlib
import time

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
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0
    for line in lines:
        game_part, numbers_part = line.split(':')
        game = game_part.split(' ')[1]
        rounds = numbers_part.split('; ')
        all_possible = True
        for round in rounds:
            if not all_possible:
                break
            number_color = round.split(', ')
            for nc in number_color:
                n, c = nc.strip().split(' ')
                if int(n) > colors[c]:
                    all_possible = False
                    break

        if all_possible:
            result += int(game)


    return result


def solution2(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0

    for line in lines:
        game_part, numbers_part = line.split(':')
        game = game_part.split(' ')[1]
        rounds = numbers_part.split('; ')
        min_color = dict()
        for round in rounds:

            number_color = round.split(', ')
            for nc in number_color:
                n, c = nc.strip().split(' ')
                if c not in min_color:
                    min_color[c] = int(n)
                else:
                    if int(n) > min_color[c]:
                        min_color[c] = int(n)

        
        res = min_color['red'] * min_color['blue'] * min_color['green']
        result += res

    return result


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    print(helper.benchmark(solution)(file_directory / 'test.txt'))
    print('\n*******************************\n')
    print(helper.benchmark(solution)(file_directory / 'input.txt'))
    print('\n-------------------------------\n')
    print(helper.benchmark(solution2)(file_directory / 'test.txt'))
    print('\n*******************************\n')
    print(helper.benchmark(solution2)(file_directory / 'input.txt'))