import os
import sys

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, "input.txt")

sys.stdin = open(input_file_path, "rt")

def solution(r):
    
    cnt = 0

    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            #print(f"x: {x}, y: {y}")
            if x * x + y * y <= r * r:
                cnt += 1

    return cnt

# Read the number of test cases
T = int(input())

# Process each test case
for test_case in range(1, T + 1):
    TC = int(input())
    answer = solution(TC)
    print("#{} {}".format(test_case, answer))
    
