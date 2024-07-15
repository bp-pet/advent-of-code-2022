import numpy as np
scoring = np.array([[2, 1, 2], [3, 2, 3], [1, 3, 1]]).transpose()
indices = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
xyz_score = {"X": 0, "Y": 3, "Z": 6}
def get_result(line):
    print(line, scoring[indices[line[0]], indices[line[2]]], xyz_score[line[2]])
    return scoring[indices[line[0]], indices[line[2]]] + xyz_score[line[2]]
print(sum(get_result(line) for line in open("day02sample.txt", "r").read().split("\n")))