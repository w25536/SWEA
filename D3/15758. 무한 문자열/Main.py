import os
import sys

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, "input.txt")

sys.stdin = open(input_file_path, "rt")


def solution(input_str):
    s1, s2 = input_str.split()

    gcd = math.lcm(len(s1), len(s2))

    s11 = s1 * int(gcd / len(s1))
    s22 = s2 * int(gcd / len(s2))

    if s11 == s22 :
        return "yes"
    else:
        return "no"


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    answer = solution(input())
    print("#{} {}".format(test_case, answer))
