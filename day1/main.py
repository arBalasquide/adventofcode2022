#!/usr/bin/env python3


def part1(inventory):
    sums = []

    for i in range(0, len(inventory)):
        sums.append(sum(inventory[i]))

    sums.sort()

    return sums[len(sums)-1]


def part2(inventory):
    sums = []

    for i in range(0, len(inventory)):
        sums.append(sum(inventory[i]))

    sums.sort()

    return sum(sums[-3:])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inventory = [[int(calorie) for calorie in line.split("\n")] for line in f.read().rstrip().split("\n\n")]

    print(part1(inventory))
    print(part2(inventory))
