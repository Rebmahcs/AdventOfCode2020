import re


class Passport:
    def __init__(self):
        self.__byr = None
        self.__iyr = None
        self.__eyr = None
        self.__hgt = None
        self.__hcl = None
        self.__ecl = None
        self.__pid = None
        self.__cid = None

    def set_birth_year(self, year):
        self.__byr = int(year)

    def set_issue_year(self, year):
        self.__iyr = int(year)

    def set_expiration_year(self, year):
        self.__eyr = int(year)

    def set_height(self, height):
        self.__hgt = height

    def set_hair_color(self, color):
        self.__hcl = color

    def set_eye_color(self, color):
        self.__ecl = color

    def set_passport_id(self, pid):
        self.__pid = pid

    def set_country_id(self, cid):
        self.__cid = cid

    def is_valid(self):
        return self.__byr is not None and self.__iyr is not None and \
               self.__eyr is not None and self.__hgt is not None and \
               self.__hcl is not None and self.__ecl is not None and \
               self.__pid is not None

    def is_valid2(self):
        if self.__byr is None or self.__byr < 1920 or self.__byr > 2002:
            return False
        if self.__iyr is None or self.__iyr < 2010 or self.__iyr > 2020:
            return False
        if self.__eyr is None or self.__eyr < 2020 or self.__eyr > 2030:
            return False
        if self.__pid is None or len(self.__pid) != 9:
            return False
        if self.__hgt is not None:
            unit = self.__hgt[-2:]
            val = int(self.__hgt[:-2])
            if unit == "cm":
                if val < 150 or val > 193:
                    return False
            elif unit == "in":
                if val < 59 or val > 76:
                    return False
            else:
                return False
        else:
            return False

        pattern = re.compile("^#[a-f0-9]{6}$")
        if self.__hcl is None or not pattern.match(self.__hcl):
            return False
        if self.__ecl is None or self.__ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        return True

    def set_correct_field(self, field):
        arr = field.split(":")

        if arr[0] == "byr":
            self.set_birth_year(arr[1])
        elif arr[0] == "iyr":
            self.set_issue_year(arr[1])
        elif arr[0] == "eyr":
            self.set_expiration_year(arr[1])
        elif arr[0] == "hgt":
            self.set_height(arr[1])
        elif arr[0] == "hcl":
            self.set_hair_color(arr[1])
        elif arr[0] == "ecl":
            self.set_eye_color(arr[1])
        elif arr[0] == "pid":
            self.set_passport_id(arr[1])
        elif arr[0] == "cid":
            self.set_country_id(arr[1])


def part1():
    with open("data/data4", "r") as data:
        passport = Passport()
        nb_valid = 0
        for line in data:
            if line == "\n":
                if passport.is_valid():
                    nb_valid += 1
                passport = Passport()
            fields = line.split()
            for field in fields:
                passport.set_correct_field(field)
        if passport.is_valid():
            nb_valid += 1
        print(f"Part 1: {nb_valid}")


def part2():
    with open("data/data4", "r") as data:
        passport = Passport()
        nb_valid = 0
        for line in data:
            if line == "\n":
                if passport.is_valid2():
                    nb_valid += 1
                passport = Passport()
            fields = line.split()
            for field in fields:
                passport.set_correct_field(field)
        if passport.is_valid2():
            nb_valid += 1
        print(f"Part 2: {nb_valid}")


def day4():
    print("Day 4 \n")
    part1()
    part2()
    print("----------------------\n")
