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

def has_neighbour(lines, i, j):
    for ii in [-1,0,1]:
        for ji in [-1,0,1]:
            x= i+ii
            y = j + ji
            if x >= 0 and y >= 0 and x < len(lines) and y < len(lines[0]):
                char = lines[i+ii][j+ji]
                if not char.isnumeric() and char != '.':
                    return True

def find_neighbours(position_array, i, j):
    nr_set = set()
    for ii in [-1,0,1]:
        for ji in [-1,0,1]:
            x= i+ii
            y = j + ji
            if x >= 0 and y >= 0 and x < position_array.shape[0] and y < position_array.shape[1]:
                nr = position_array[x][y]
                if not np.isnan(nr) and nr != 0:
                    nr_set.add(int(nr))

    return nr_set



def solution(input_file):
    lines = helper.read_file_lines(input_file, strip_lines=True)
    result = 0
    result2 = 0
    numbers = []
    number_id = 1
    position_array = np.zeros((len(lines), len(lines[0])))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '*':
                position_array[i,j]=np.nan
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            current_nr = ''
            current_indices = []
            if char.isnumeric() and not line[j-1].isnumeric():
                jn = j
                while jn < len(line) and line[jn].isnumeric():
                    current_indices.append((i,jn))
                    current_nr += line[jn]
                    jn += 1
                
                current_number = int(current_nr)

                for coor in current_indices:
                    k,l = coor
                    if has_neighbour(lines,k,l):
                        result += current_number
                        numbers.append(current_number)
                        for m in range(j, jn):
                            position_array[i, m] = number_id

                        number_id += 1

                        break

    
    for i in range(position_array.shape[0]):
        for j in range(position_array.shape[1]):
            if position_array[i,j] == 0:
                neighbours = find_neighbours(position_array, i,j)
                if len(list(neighbours)) == 2:
                    nr1, nr2 = neighbours
                    n1 = numbers[nr1-1]
                    n2 = numbers[nr2-1]

                    result2 += n1*n2

    return result2


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