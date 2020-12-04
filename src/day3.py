from functools import reduce


def load_map(path):
    with open(path, "r") as file:
        return file.read().splitlines()


def count_trees(tree_map, down, right):
    nb_trees = 0
    current_x = 0
    max_x = len(tree_map[0])

    for current_i in range(down, len(tree_map), down):
        current_x += right
        if current_x >= max_x:
            current_x -= max_x
        if tree_map[current_i][current_x] == "#":
            nb_trees += 1

    return nb_trees


def part1():
    data = load_map("data/data3")
    print(f"Part 1: {count_trees(data, 1, 3)}")


def part2():
    tree_map = load_map("data/data3")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [count_trees(tree_map, slope[1], slope[0]) for slope in slopes]
    print(f"Part 2: {reduce(lambda x, y: x * y, trees)}")


def day3():
    print("Day 3 \n")
    part1()
    part2()
    print("----------------------\n")
