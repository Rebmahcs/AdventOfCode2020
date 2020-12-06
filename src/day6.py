from functools import reduce


def part1():
    with open("data/data6", "r") as file:
        yes = count_answer(file)
        print(f"Part 1: {yes} ")


def part2():
    with open("data/data6", "r") as file:
        yes = count_answer_2(file)
        print(f"Part 1: {yes} ")


def char_range(a, b):
    for c in range(ord(a), ord(b) + 1):
        yield chr(c)


def get_answer_dict():
    answer = dict()
    for c in char_range("a", "z"):
        answer[c] = False
    return answer


def get_answer_dict_2():
    answer = dict()
    for c in char_range("a", "z"):
        answer[c] = 0
    return answer


def count_answer(file):
    answer = get_answer_dict()
    nb_yes = 0
    for line in file:
        if line == "\n":
            nb_yes += list(answer.values()).count(True)
            answer = get_answer_dict()
        else:
            for c in line.rstrip():
                answer[c] = True
    nb_yes += list(answer.values()).count(True)
    return nb_yes


def count_answer_2(file):
    answer = get_answer_dict_2()
    nb_yes = 0
    nb_person = 0
    for line in file:
        if line == "\n":
            nb_yes += list(answer.values()).count(nb_person)
            nb_person = 0
            answer = get_answer_dict()
        else:
            nb_person += 1
            for c in line.rstrip():
                answer[c] += 1
    if nb_person != 0:
        nb_yes += list(answer.values()).count(nb_person)

    return nb_yes


def test():
    with open("data/data6test", "r") as file:
        yes = count_answer(file)
        print(f"Test: {yes} {yes == 11}")

def test2():
    with open("data/data6test", "r") as file:
        yes = count_answer_2(file)
        print(f"Test2: {yes} {yes == 6}")

def day6():
    print("Day 6 \n")
    test()
    test2()
    part1()
    part2()
    print("----------------------\n")
