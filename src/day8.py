def part1():
    print("Part 1: ")
    p = Program("data/data8")

    print(p.execute())


def test1():
    print("Test 1: ")

    p = Program("data/data8test")

    print(p.execute() == 5)


def test2():
    print("Test 2: ")

    p = Program("data/data8test")

    p.correct_corruption()
    print(p.execute() == 8)


def part2():
    print("Part 2: ")
    p = Program("data/data8")
    p.correct_corruption()
    print(p.execute())

class Program:
    def __init__(self, path):
        with open(path, "r") as file:
            self.__lines = [line.split() for line in file.read().splitlines()]
            self.__current_line = 0
            self.__acc_value = 0

    def print_program(self):
        for line in self.__lines:
            print(f"{line[0]}\t{line[1]}")

    def nop(self):
        self.__current_line += 1

    def jmp(self, n):
        self.__current_line += n

    def acc(self, n):
        self.__current_line += 1
        self.__acc_value += n

    def __exec_instr(self):
        instr, val = self.__lines[self.__current_line]

        if instr == "nop":
            self.nop()
        elif instr == "jmp":
            self.jmp(int(val))
        elif instr == "acc":
            self.acc(int(val))
        else:
            raise Exception(f"Unsupported instruction {instr}")

    def execute(self):
        self.__current_line = 0
        self.__acc_value = 0
        instr_executed = []

        while self.__current_line < len(self.__lines):
            if self.__current_line in instr_executed:
                print("Loop Detected")
                return self.__acc_value
            instr_executed.append(self.__current_line)

            self.__exec_instr()

        return self.__acc_value

    def is_looping(self):
        self.__current_line = 0
        self.__acc_value = 0
        instr_executed = []

        while self.__current_line < len(self.__lines):
            if self.__current_line in instr_executed:
                return True
            instr_executed.append(self.__current_line)

            self.__exec_instr()

        return False

    def change_instr(self, line_nb):
        if self.__lines[line_nb][0] == "jmp":
            self.__lines[line_nb][0] = "nop"
        elif self.__lines[line_nb][0] == "nop":
            self.__lines[line_nb][0] = "jmp"

    def correct_corruption(self):
        instr_to_correct = 0
        if not self.is_looping():
            return

        while instr_to_correct < len(self.__lines):
            #print(f"Correct: Processing line {instr_to_correct}")
            self.change_instr(instr_to_correct)
            if self.is_looping():
                self.change_instr(instr_to_correct)
            else:
                #print(f"Correct: Line {instr_to_correct} worked")
                return
            instr_to_correct += 1
        #print("Correct: Issue not found")


def day8():
    print("Day 8 \n")
    test1()
    part1()
    test2()
    part2()
    print("----------------------\n")
