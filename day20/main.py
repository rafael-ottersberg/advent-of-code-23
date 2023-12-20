import os
import sys
import pathlib
from collections import deque

import math

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

class Conjunction:
    def __init__(self, children):
        self.states = {}
        self.children = children

    def add_input(self, identifier):
        self.states[identifier] = 0

    def process(self, pulse, source, dest, queue):
        self.states[source] = pulse

        new_pulse = 1
        new_source = dest
        if all(self.states.values()):
            new_pulse = 0

        for child in self.children:
            queue.append((new_pulse, child, new_source))

class FlipFlop:
    def __init__(self, children):
        self.state = 0
        self.children = children

    def process(self, pulse, source, dest, queue):
        if not pulse:
            self.state = int(not self.state)

            new_source = dest        
            for child in self.children:
                queue.append((self.state, child, new_source))        

def solution(input_file):
    start_children = []

    flip_flops = {}
    conjunctions = {}
    lines = open(input_file, 'r').read().splitlines()
    for line in lines:
        description, dest = line.split(' -> ')
        destinations = dest.split(', ')
        if 'broadcaster' in description:
            for id in destinations:
                start_children.append(id)

        id = description[1:]
        if '%' in description:
            flip_flops[id] = destinations
        if '&' in description:
            conjunctions[id] = destinations

    modules = {}
    for ff in flip_flops:
        modules[ff] = FlipFlop(flip_flops[ff])

    for cc in conjunctions:
        modules[cc] = Conjunction(conjunctions[cc])

    for m in modules:
        for c in modules[m].children:
            if c in modules:
                if type(modules[c]) == Conjunction:
                    modules[c].add_input(m)

    queue = deque()

    lowp = 0
    highp = 0
    for i in range(1000):
        # init children
        lowp += 1
        for st in start_children:
            if st in modules:
                if type(modules[st]) == Conjunction:
                    modules[st].add_input('broadcaster')
            queue.append((0, st, 'broadcaster'))

        # empty queue
        while queue:
            pulse, dest, src = queue.popleft()
            #print(f'{src} --{pulse}--> {dest}')
            if pulse:
                highp += 1
            else:
                lowp += 1

            if dest in modules:
                modules[dest].process(pulse, src, dest, queue)

    return lowp, highp, lowp*highp

def solution2(input_file):

    start_children = []

    flip_flops = {}
    conjunctions = {}

    id_observe = None

    lines = open(input_file, 'r').read().splitlines()
    for line in lines:
        description, dest = line.split(' -> ')
        destinations = dest.split(', ')
        if 'broadcaster' in description:
            for id in destinations:
                start_children.append(id)

        id = description[1:]
        if '%' in description:
            flip_flops[id] = destinations
        if '&' in description:
            conjunctions[id] = destinations

    modules = {}
    for ff in flip_flops:
        modules[ff] = FlipFlop(flip_flops[ff])

    for cc in conjunctions:
        modules[cc] = Conjunction(conjunctions[cc])

    for m in modules:
        for c in modules[m].children:
            if c in modules:
                if type(modules[c]) == Conjunction:
                    modules[c].add_input(m)
                
            if c == 'rx':
                id_observe = m

    queue = deque()

    observe = list(modules[id_observe].states.keys())
    #print(observe)

    indices = {}

    all_one = False

    i=0
    while not all_one:
        i += 1
        # init children
        for st in start_children:
            if st in modules:
                if type(modules[st]) == Conjunction:
                    modules[st].add_input('broadcaster')
            queue.append((0, st, 'broadcaster'))

        # empty queue
        while queue:
            pulse, dest, src = queue.popleft()
            #print(f'{src} --{pulse}--> {dest}')

            if src in observe and pulse == 1:
                if src not in indices:
                    indices[src] = i
                
                if len(indices) >= 4:
                    all_one = True
                    break

            if dest in modules:
                modules[dest].process(pulse, src, dest, queue)


    return math.lcm(*list(indices.values()))

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))