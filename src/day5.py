def part1():
    with open("data/data5", "r") as file:
        print(max([compute_seat_id(seat) for seat in file.read().splitlines()]))


def part2():
    with open("data/data5", "r") as file:
        seat_list = [compute_seat_id(seat) for seat in file.read().splitlines()]
        seat_list.sort()
        last_seat = -1
        for seat in seat_list:
            if seat == last_seat + 2:
                print(seat - 1)
                return
            last_seat = seat


def compute_seat_id(seat):
    row = ""
    for c in seat[:-3]:
        row += "0" if c == "F" else "1"

    col = ""
    for c in seat[-3:]:
        col += "0" if c == "L" else "1"

    return int(row, 2) * 8 + int(col, 2)


def test():
    test_data = (("FBFBBFFRLR", 357), ("BFFFBBFRRR", 567), ("FFFBBBFRRR", 119), ("BBFFBBFRLL", 820))
    for i, data in enumerate(test_data):
        seat_id = compute_seat_id(data[0])
        print(f"Test {i}: {data[0]} => {data[1]} : {seat_id == data[1]}")


def day5():
    print("Day 5 \n")
    # test()
    part1()
    part2()
    print("----------------------\n")
