from pathlib import Path


def read_input() -> [list[int], list[int]]:
    list1: list[int] = []
    list2: list[int] = []
    file = Path("input.txt")
    with file.open("r", encoding="utf-8") as f:
        for line in f:
            line_parts = line.split("   ")
            line_parts = [int(line_part.strip()) for line_part in line_parts]
            list1.append(line_parts[0])
            list2.append(line_parts[1])

    return list1, list2


def find_difference(list1: list[int], list2: list[int]) -> int:
    amount = 0
    list1.sort()
    list2.sort()

    for el1, el2 in zip(list1, list2):
        difference = abs(el1 - el2)

        amount += difference

    return amount


def find_similarity_score(list1: list[int], list2: list[int]) -> int:
    amount = 0

    for i, element in enumerate(list1):
        occurrences = list2.count(element)
        if occurrences != 0:
            score = element * occurrences
            amount += score

    return amount


if __name__ == "__main__":
    list1, list2 = read_input()
    diff = find_difference(list1, list2)
    print(diff)
    sim_score = find_similarity_score(list1, list2)
    print(sim_score)

pass
