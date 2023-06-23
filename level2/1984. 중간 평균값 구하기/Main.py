import os
import sys

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, "input.txt")

sys.stdin = open(input_file_path, "rt")


def solution(input_str):
    
    nums = list(map(int, input_str.split()))

    max_value = max(nums)
    min_value = min(nums)
    
    nums.remove(max_value)
    nums.remove(min_value)
        
    return round(sum(nums)/ len(nums)) 

T = int(input())

for test_case in range(1, T + 1):
    TC = input()
    answer = solution(TC)
    print("#{} {}".format(test_case, answer))
