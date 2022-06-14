#!/usr/bin/env python3.7

def split_and_join(line):
    linea = "this is a string", 
    lineb = "quick brown fox jumps over a lazy dog"
    line = line.split(" ")
    line = "-".join(line)
    return line      
   
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
