#!/usr/local/bin/python3

def aoc():

    total=0

    with open("./input") as infile:
        line = infile.readline()
        while line:
            digitsline=""
            cal_value=""
            if line.strip():
                for i in line:
                    if i.isdecimal():
                        digitsline+=i
            cal_value=digitsline[:1] + digitsline[-1:]
            total+=int(cal_value)
            line = infile.readline()

    print(total)

if __name__ == '__main__':
  aoc()
