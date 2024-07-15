import numpy as np
scoring = np.array([[3, 0, 6], [6, 3, 0], [0, 6, 3]]).transpose()
indices = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
def get_result(line):
    return scoring[indices[line[0]], indices[line[2]]] + indices[line[2]] + 1
print(sum(get_result(line) for line in open("day02input.txt", "r").read().split("\n")))