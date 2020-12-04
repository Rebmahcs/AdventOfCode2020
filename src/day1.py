import time
from functools import reduce


def load_file(path):
    with open(path, "r") as file:
        return [int(x) for x in file.readlines()]


# Dumb approch.

def find_2020_tuple(data):
    for x in data:
        for y in data:
            if x + y == 2020:
                return x, y


def find_2020_truple(data):
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    return x, y, z


def multiply_terms(terms):
    return reduce(lambda x, y: x * y, terms)


# Approach 2
#
# In order to have 2 terms that sum to X we must have 2 terms == X/2 or one greater than X/2 and one shorter than X/2
# So we can sort the data and split into two list in order to process less combinations
# TODO: Find how to generalize this behaviour for n terms

def split_data(data, value):
    for i, val in enumerate(data):
        if val > value:
            return [data[:i - 1], data[i:]]


# TODO Not working for n > 3
def find_elements(sorted_data, n, target):
    # Check if the is n element that sum to target
    split_value = target / n
    if sorted_data.count(split_value) == n:
        return [split_value for _ in range(n)]

    if n == 1:
        return None
    # If we have only 2 element to find,  split the data at the middle and find 2 terms that sum to target
    if n == 2:
        spliced_data = split_data(sorted_data, split_value)
        i = iter(spliced_data[0])
        j = reversed(spliced_data[1])

        val = next(i)
        val2 = next(j)
        try:
            while True:
                term_sum = val + val2
                if term_sum == target:
                    return [val, val2]
                elif term_sum < target:
                    val = next(i)
                else:
                    val2 = next(j)
        except StopIteration:
            return None

    else:
        for a in sorted_data:
            element = find_elements(sorted_data, n - 1, target - a)
            if element is not None:
                element.append(a)
                return element


def part1():
    data = load_file("data/data1")
    data2 = load_file("data/data1")
    data2.sort()

    print("Part 1")

    start = time.time()
    print(multiply_terms(find_2020_tuple(data)))
    end = time.time()
    print("Time for dummy approach" + str(end - start))

    start = time.time()
    print(multiply_terms(find_elements(data2, 2, 2020)))
    end = time.time()
    print("Time for v1 approach" + str(end - start))


def part2():
    data = load_file("data/data1")
    data2 = load_file("data/data1")
    data2.sort()

    print("Part 2")
    start = time.time()
    print(multiply_terms(find_2020_truple(data)))
    end = time.time()
    print("Time for dummy approach" + str(end - start))

    start = time.time()
    print(multiply_terms(find_elements(data2, 3, 2020)))
    end = time.time()
    print("Time for v1 approach" + str(end - start))


def day1():
    print("Day 1 \n")
    part1()
    print("\n")
    part2()
    print("----------------------\n")
