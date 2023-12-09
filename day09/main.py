import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def calculate_difference(numbers):
    return [numbers[i]- numbers[i-1] for i in range(1, len(numbers))]

def find_next_number(numbers):
    diff = calculate_difference(numbers)
    if len(set(diff)) == 1 and diff[-1] == 0:
        return numbers[-1]
    
    else:
        return numbers[-1] + find_next_number(diff)
    
def find_previous_number(numbers):
    diff = calculate_difference(numbers)
    if len(set(diff)) == 1 and diff[0] == 0:
        return numbers[0]
    
    else:
        return numbers[0] - find_previous_number(diff)

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        numbers = [int(l) for l in line.split()]

        result+=find_next_number(numbers)

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        numbers = [int(l) for l in line.split()]

        result+=find_previous_number(numbers)

    return result

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