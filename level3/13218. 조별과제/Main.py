import os
import sys

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, "input.txt")

sys.stdin = open(input_file_path, "rt")


def solution(input_n):

    return int(input_n /3)


T = int(input())

for test_case in range(1, T +1):
    input_n = int(input())
    answer = solution(input_n)
    print("#{} {}".format(test_case, answer))
