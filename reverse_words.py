#!/usr/bin/env python
'''
Problem

Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.
'''

from sys import stdin
def ReverseString(in_str):
    str_lst = in_str.split()
    rv_str_lst = []
    for i in range(len(str_lst)):
        rv_str_lst.append(str_lst.pop())
        out_str = ' '.join(rv_str_lst)
    return out_str

def main():
    no_cases = int(stdin.readline())
    for i in range(no_cases):
        instr = stdin.readline()
        print 'Case #%d: %s' % (i+1, ReverseString(instr))
    return 0

if __name__ == '__main__':
    main()
