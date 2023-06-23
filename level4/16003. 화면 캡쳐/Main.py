import os
import sys

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, "input.txt")

sys.stdin = open(input_file_path, "rt")

def solution(input_str):
    
    num = int(input_str)
    
    filenames = []
    for i in range(1, num+1):
        filename =str(i) +".png"
        filenames.append(filename)
        
    
    filenames.sort(key=lambda x: int(str(x)[0]))
    
    filenames_str = ' '.join(filenames)
             
    return filenames_str

T = int(input())

for test_case in range(1, T+1):
    TC = input()
    answer = solution(TC)
    print("#{} {}".format(test_case, answer))
