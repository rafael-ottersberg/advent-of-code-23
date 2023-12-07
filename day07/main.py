import helper
import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)


def solution(input_file):
    strength = ['A', 'K', 'Q', 'J', 'T', '9',
                '8', '7', '6', '5', '4', '3', '2']

    result = 0
    lines = open(input_file, 'r').read().splitlines()
    kinds = [[], [], [], [], [], [], []]
    for i, line in enumerate(lines):
        hand, bid = line.split()
        bid = int(bid)

        hand_nr = [strength.index(c) for c in hand]

        unique = set()
        dup = set()
        for h in hand_nr:
            if h not in unique:
                unique.add(h)
            else:
                dup.add(h)

        if len(unique) == 5:
            kinds[0].append((hand_nr, bid))
        elif len(unique) == 1:
            kinds[6].append((hand_nr, bid))
        elif len(unique) == 4:
            kinds[1].append((hand_nr, bid))
        elif len(unique) == 2:
            if len(dup) == 1:
                kinds[5].append((hand_nr, bid))
            else:
                kinds[4].append((hand_nr, bid))
        elif len(unique) == 3:
            if len(dup) == 2:
                kinds[2].append((hand_nr, bid))
            else:
                kinds[3].append((hand_nr, bid))

    count = 1
    for k in kinds:
        k.sort(reverse=True)
        for h in k:
            result += count * h[1]
            count += 1

    return result


def solution2(input_file):
    strength_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    result = 0
    lines = open(input_file, 'r').read().splitlines()
    kinds = [[], [], [], [], [], [], []]

    joker = len(strength_2)-1
    for i, line in enumerate(lines):
        hand, bid = line.split()
        bid = int(bid)

        hand_nr = [strength_2.index(c) for c in hand]

        unique = set()
        dup = set()

        joker_count = 0
        has_jokers = 0
        for h in hand_nr:
            if h == joker:
                joker_count += 1
                has_jokers = has_jokers | 1
            if h not in unique:
                unique.add(h)
            else:
                dup.add(h)

        has_duplicate_jokers = int(joker_count > 1)

        if len(unique) - has_jokers == 5:
            kinds[0].append((hand_nr, bid))
        elif len(unique) - has_jokers <= 1:
            kinds[6].append((hand_nr, bid))
        elif len(unique) - has_jokers == 4:
            kinds[1].append((hand_nr, bid))
        elif len(unique)-has_jokers == 2:
            if len(dup) - has_duplicate_jokers <= 1:
                kinds[5].append((hand_nr, bid))
            else:
                kinds[4].append((hand_nr, bid))
        elif len(unique)-has_jokers == 3:
            if len(dup) - has_duplicate_jokers == 2:
                kinds[2].append((hand_nr, bid))
            else:
                kinds[3].append((hand_nr, bid))

    count = 1
    for k in kinds:
        k.sort(reverse=True)
        for h in k:
            result += count * h[1]
            count += 1

    return result


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1:  # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1:  # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))
