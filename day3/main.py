#!/usr/bin/env python3


def split_list(arr):
    half = len(arr)//2
    return arr[:half], arr[half:]


def create_set(items):
    item_set = set()
    for item in items:
        item_set.add(item)

    return item_set


# hacky way to get right result from ord() 
def priority(item):
    prio = ord(item)

    prio = prio - 96 if prio > 96 else prio - 38

    return prio


def part1(inventories):
    sum = 0

    for rucksack in inventories:
        comp1,comp2 = split_list(rucksack)

        set1 = create_set(comp1)
        set2 = create_set(comp2)
        
        # assuming input is fine and there is indeed ONLY one matching item
        item = set1.intersection(set2).pop()
        sum += priority(item)

    return sum


def part2(inventories):
    sum = 0

    while inventories:
        set1 = create_set(inventories.pop(0))
        set2 = create_set(inventories.pop(0))
        set3 = create_set(inventories.pop(0))

        item = set3.intersection(set1.intersection(set2)).pop()

        sum += priority(item)

    return sum


if __name__ == "__main__":
    with open("input.txt") as f:
        inventories = [line for line in f.read().splitlines()]

    print(part1(inventories))
    print(part2(inventories))
