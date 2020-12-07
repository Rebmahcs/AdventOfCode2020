def part1():
    with open("data/data7", "r") as file:
        bags = outermost_bags("shiny gold", file)
        print(f"Part 1 : {len(bags)} {bags}")


def part2():
    with open("data/data7", "r") as file:
        lines = file.read().splitlines()
        bags_dict = get_bag_dict(lines)
        bags = inner_bags("shiny gold", bags_dict).get("shiny gold", None)
        print(f"Part 2 : {bags}")


def test1():
    with open("data/data7test", "r") as file:
        bags = outermost_bags("shiny gold", file)
        print(f"Test1 : {len(bags)} {len(bags) == 4}")


def test2():
    with open("data/data7test", "r") as file:
        lines = file.read().splitlines()
        bags_dict = get_bag_dict(lines)
        bags = inner_bags("shiny gold", bags_dict)["shiny gold"]
        print(f"Test2.1: {bags} {bags == 32}")

def test2_2():
    with open("data/data7test2", "r") as file:
        lines = file.read().splitlines()
        bags_dict = get_bag_dict(lines)
        bags = inner_bags("shiny gold", bags_dict)["shiny gold"]
        print(f"Test2.2: {bags} {bags == 126}")


# Return a dict with bags name as index and possible bags  inside as values
def get_bag_dict(lines):
    split_lines = [line.split(" bags contain ") for line in lines]

    # Init dict
    bag_dict = dict()
    for bag in split_lines:
        bag_dict[bag[0]] = []

    # Add possible inside
    for bag_line in split_lines:
        inside_bag = bag_line[1].split(", ")
        for bag in inside_bag:
            bag_split = bag.split()
            if bag_split[0] != "no":
                bag_dict[bag_line[0]].append((bag_split[0], bag_split[1] + " " + bag_split[2]))
    return bag_dict


def get_bag_outer_possible(color, bag_dict):
    possible_outer = set()
    for bag, inside in bag_dict.items():
        for inside_bag in inside:
            if inside_bag[1] == color:
                possible_outer.add(bag)
    return possible_outer


def outermost_bags(color, file):
    lines = file.read().splitlines()
    bags_dict = get_bag_dict(lines)

    # Init with direclty containing
    bags = get_bag_outer_possible(color, bags_dict)
    new_color = list(bags)
    color_done = [color]

    # Get remaining colors
    while len(new_color) != 0:
        color = new_color.pop()
        new_bags = get_bag_outer_possible(color, bags_dict)
        bags = bags.union(new_bags)
        color_done.append(color)

        # Add new colors if not done already
        for new_bag in new_bags:
            if new_bag not in color_done:
                new_color.append(new_bag)

    return bags


# Return dict with key = color and value = number inner
def inner_bags(color, bags_dict, bags_cache=None):
    if bags_cache is None:
        bags_cache = dict()

    bags_inside = bags_dict[color]
    nb_inside = 0
    for number, bag in bags_inside:
        if bags_cache.get(bag, None) is None:
            bags_cache.update(inner_bags(bag, bags_dict, bags_cache))
        nb_inside += bags_cache[bag] * int(number) + int(number)

    bags_cache[color] = nb_inside
    return bags_cache


def day7():
    print("Day 7 \n")
    test1()
    part1()
    test2()
    test2_2()
    part2()
    print("----------------------\n")
