#!/usr/bin/env python3


def create_set_range(ranges):
    r = set(range(ranges[0],ranges[1]+1))

    return r


def part1(sections):
    sum = 0

    for pair in sections:
        point1 = [int(number) for number in pair[0].split("-")]
        point2 = [int(number) for number in pair[1].split("-")]
        
        r1 = create_set_range(point1)
        r2 = create_set_range(point2)

        sum += r1.issubset(r2) or r2.issubset(r1)

    return sum


def part2(sections):
    sum = 0

    for pair in sections:
        point1 = [int(number) for number in pair[0].split("-")]
        point2 = [int(number) for number in pair[1].split("-")]
        
        r1 = create_set_range(point1)
        r2 = create_set_range(point2)

        sum += len(r1.intersection(r2)) > 0

    return sum


if __name__ == "__main__":
    with open("input.txt") as f:
        sections = [line.split(",") for line in f.read().splitlines()]

    print(part1(sections))
    print(part2(sections))

