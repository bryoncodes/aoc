#!/usr/local/bin/python3

numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

def get_nums(line, reversed):

    numbers_low_index = len(line)
    digits_low_index = len(line)

    for i in numbers:
        if reversed: 
            if numbers[i][::-1] in line:
                number_index=line.find(numbers[i][::-1])
                if number_index < numbers_low_index:
                    numbers_low_index = number_index
                    number = i
        else:
           if numbers[i] in line:
                number_index=line.find(numbers[i])
                if number_index < numbers_low_index:
                    numbers_low_index = number_index
                    number = i 

    for i in range(numbers_low_index):
        if line[i].isdecimal():
            digits_low_index = i 
            break

    return str(number) if numbers_low_index < digits_low_index else line[digits_low_index]

def aoc():

    total=0

    with open("./input") as infile:
        line = infile.readline().strip()
        while line:
            first = get_nums(line, False)
            last = get_nums(line[::-1], True)
            cal_value = first + last
            total+=int(cal_value)
            line = infile.readline().strip()

    print(total)

if __name__ == '__main__':
  aoc()
