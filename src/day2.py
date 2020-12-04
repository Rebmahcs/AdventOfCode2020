def check_validity_1(line):
    line = line.split()
    min_max = [int(x) for x in line[0].split("-")]
    character = line[1][:-1]
    occ = line[2].count(character)
    return min_max[0] <= occ <= min_max[1]


def check_validity_2(line):
    line = line.split()

    positions = [int(x) - 1 for x in line[0].split("-")]
    character = line[1][:-1]
    password = line[2]
    pass_length = len(password) - 1

    char_found = False
    for pos in positions:
        if pos <= pass_length:
            letter = password[pos]
            if pos <= pass_length and letter == character and not char_found:
                char_found = True
            elif pos <= pass_length and password[pos] == character and char_found:
                return False
    return char_found


def day2():
    password_valid = 0
    password_valid2 = 0

    with open("data/data2", "r") as file:
        for line in file:
            # Part 1
            if check_validity_1(line):
                password_valid += 1
            # Part 2
            if check_validity_2(line):
                password_valid2 += 1

    print("Day 2 \n")
    print(f"Part 1: {password_valid}")
    print(f"Part 1: {password_valid2}")
    print("----------------------\n")
