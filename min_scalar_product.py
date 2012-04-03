#!/usr/bin/env python

'''
Problem

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

Input
The first line of the input file contains integer number T - the number of test cases. For each test case, the first line contains integer number n. The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

Output

For each test case, output a line

Case #X: Y

where X is the test case number, starting from 1, and Y is the minimum scalar product of all permutations of the two given vectors. 
'''

from sys import stdin

def InsertionSort(array):
    n = len(array)
    for i in range(1, n):
        while array[i] < array[i-1] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array

def main():
    no_cases = int(stdin.readline())
    for i in range(no_cases):
        v_len = int(stdin.readline())
        v1 = [int(x) for x in stdin.readline().split()]
        v2 = [int(x) for x in stdin.readline().split()]
        if not len(v1) == v_len and not len(v2) == v_len:
            return -1
        sorted_v1 = InsertionSort(v1)
        sorted_v2 = InsertionSort(v2)
        s_product = 0
        for j in range(v_len):
            s_product += sorted_v1[j] * sorted_v2.pop()
        print 'Case #%d: %d' % (i+1, s_product)
    return 0


if __name__  == '__main__':
    main()
