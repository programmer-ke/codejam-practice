#!/usr/bin/env python

'''
Problem

A company is located in two very tall buildings. The company intranet connecting the buildings consists of many wires, each connecting a window on the first building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings is to the left and one is to the right. The windows on the left building are seen as points on its right wall, and the windows on the right building are seen as points on its left wall. Wires are straight segments connecting a window on the left building to a window on the right building.

You've noticed that no two wires share an endpoint (in other words, there's at most one wire going out of each window). However, from your viewpoint, some of the wires intersect midway. You've also noticed that exactly two wires meet at each intersection point.

How many intersection points do you see?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with a line containing an integer N, denoting the number of wires you see.

The next N lines each describe one wire with two integers Ai and Bi. These describe the windows that this wire connects: Ai is the height of the window on the left building, and Bi is the height of the window on the right building.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of intersection points you see. 
'''

from sys import stdin

def main():
    no_cases = int(stdin.readline())
    for case in range(no_cases):
        no_input = int(stdin.readline())
        wires, left_side = dict(), list()
        for i in range(no_input):
            l = [int(c) for c in stdin.readline().split()]
            wires[l[0]] = l[1]
            left_side.append(l[0])
        left_side.sort()
        intersections = 0
        for index, w in enumerate(left_side):
            rs = wires[w]
            for o in left_side[index+1:]:
                if wires[o] < rs:
                    intersections+=1
        print 'Case #%d: %d' % (case+1, intersections)

if __name__ == '__main__':
    main()
