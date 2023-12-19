# 117126771750596, too high
# ca. 75min
import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def eval_expression(location, part, rules_dict):
    rules = rules_dict[location]
    for rule in rules:
        exp, goto = rule
        if exp is None:
            return check_and_eval(goto, part, rules_dict)
        
        if exp[1] == '>':
            if part[exp[0]] > exp[2]:
                return check_and_eval(goto, part, rules_dict)
            else:
                continue

        if exp[1] == '<':
            if part[exp[0]] < exp[2]:
                return check_and_eval(goto, part, rules_dict)
            else:
                continue

def check_and_eval(goto, part, rules_dict):
    if goto == 'A':
        return True
    elif goto == 'R':
        return False
    else:
        return eval_expression(goto, part, rules_dict)

def solution(input_file):
    global rules_dict
    result = 0
    rules_dict = {}

    rule_section, part_section = open(input_file, 'r').read().split('\n\n')
    rules = rule_section.splitlines()
    parts = part_section.splitlines()

    for rule in rules:
        name, exp = rule.strip('}').split('{')
        expressions = exp.split(',')
        rules_dict[name] = [] 

        for expr_do in expressions:
            if not '<' in expr_do and not '>' in expr_do:
                do = expr_do
                rules_dict[name].append((None, do))
                continue
            
            expr, do = expr_do.split(':')
            var = expr[0]
            op = expr[1]
            number = int(expr[2:])

            rules_dict[name].append(((var, op, number), do))
    
    part_list = []
    for part in parts:
        d = {}
        ps = part.strip('{').strip('}').split(',')
        for p in ps:
            c, nr = p.split('=')
            d[c] = int(nr)
        part_list.append(d)

    for part in part_list:
        if eval_expression('in', part, rules_dict):
            result += sum(part.values())

    return result


def eval_expression_range(location, part, rules_dict):
    all_possibilities = 0
    rules = rules_dict[location]
    for rule in rules:
        exp, goto = rule
        if exp is None:
            all_possibilities += check_and_eval_range(goto, part, rules_dict)
            continue
        
        if exp[1] == '>':
            if part[exp[0]].stop > exp[2]:
                p = part.copy()
                p[exp[0]] = range(exp[2]+1, part[exp[0]].stop)
                all_possibilities += check_and_eval_range(goto, p, rules_dict)

                part[exp[0]] = range(part[exp[0]].start, exp[2]+1)

        if exp[1] == '<':
            if part[exp[0]].start < exp[2]:
                p = part.copy()
                p[exp[0]] = range(part[exp[0]].start, exp[2])
                all_possibilities += check_and_eval_range(goto, p, rules_dict)

                part[exp[0]] = range(exp[2], part[exp[0]].stop)

    return all_possibilities


def check_and_eval_range(goto, part, rules_dict):
    if goto == 'A':
        possibilities = 1
        for v in part.values():
            possibilities = possibilities * len(v)
        return possibilities
    
    elif goto == 'R':
        return 0
    
    else:
        return eval_expression_range(goto, part, rules_dict)
    

def solution2(input_file):
    global rules_dict
    rules_dict = {}

    rule_section, _ = open(input_file, 'r').read().split('\n\n')
    rules = rule_section.splitlines()

    for rule in rules:
        name, exp = rule.strip('}').split('{')
        expressions = exp.split(',')
        rules_dict[name] = [] 

        for expr_do in expressions:
            if not '<' in expr_do and not '>' in expr_do:
                do = expr_do
                rules_dict[name].append((None, do))
                continue
            
            expr, do = expr_do.split(':')
            var = expr[0]
            op = expr[1]
            number = int(expr[2:])

            rules_dict[name].append(((var, op, number), do))

    characters = 'xmas'
    part = {c: range(1, 4001) for c in characters}

    return eval_expression_range('in', part, rules_dict)


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