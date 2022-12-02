#!/usr/bin/env python3

# theres so little possible combinations that you can just define them all quickly
# although, do notice that the two outcome lists are very similar so theres probably
# some mathematically obscure way to compute both

outcomes = {
    "A X":4,
    "A Y":8,
    "A Z":3,

    "B X":1,
    "B Y":5,
    "B Z":9,

    "C X":7,
    "C Y":2,
    "C Z":6,
}

outcomes2 = {
    "A X":3,
    "A Y":4,
    "A Z":8,

    "B X":1,
    "B Y":5,
    "B Z":9,

    "C X":2,
    "C Y":6,
    "C Z":7,
}


def outcome(moves, guide):
    sum = 0

    for move in moves:
        sum += guide[move]

    return sum


if __name__ == "__main__":
    with open("input.txt") as f:
        moves = [line for line in f.read().splitlines()]

    print(outcome(moves, outcomes))
    print(outcome(moves, outcomes2))
