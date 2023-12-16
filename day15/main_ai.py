import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def hashmap_step(step):
    """Run the HASH algorithm on a single step."""
    current_value = 0
    for char in step:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def process_initialization_sequence_1(init_sequence):
    steps = init_sequence.split(',')
    return sum(hashmap_step(step) for step in steps)

def solution(input_file):
    return process_initialization_sequence_1(open(input_file).read().replace('\n',''))

def hashmap_algorithm(label):
    """Calculate the box number using the HASH algorithm."""
    current_value = 0
    for char in label:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def calculate_focusing_power(boxes):
    """Calculate the total focusing power of the lenses in the boxes."""
    total_power = 0
    for box_number, lenses in boxes.items():
        for slot_number, (label, focal_length) in enumerate(lenses, start=1):
            total_power += (box_number + 1) * slot_number * focal_length
    return total_power

def process_initialization_sequence_2(init_sequence):
    boxes = {i: [] for i in range(256)}
    steps = init_sequence.split(',')

    for step in steps:
        label, operation = step[:-2], step[-2:]
        box_number = hashmap_algorithm(label)

        if operation[0] == '-':
            boxes[box_number] = [lens for lens in boxes[box_number] if lens[0] != label]
        else:
            focal_length = int(operation[1])
            for i, lens in enumerate(boxes[box_number]):
                if lens[0] == label:
                    boxes[box_number][i] = (label, focal_length)
                    break
            else:
                boxes[box_number].append((label, focal_length))

    return calculate_focusing_power(boxes)

# Replace 'init_sequence' with your actual initialization sequence string


def solution2(input_file):
    return process_initialization_sequence_2(open(input_file).read().replace('\n',''))

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