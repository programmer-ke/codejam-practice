#!/usr/bin/env python

'''
Problem

You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

    One line containing the value C, the amount of credit you have at the store.
    One line containing the value I, the number of items in the store.
    One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
    Each test case will have exactly one solution.

Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.
'''

from sys import stdin

def GetItems(item_list, total_cost):
    for i in range(len(item_list)):
        complement = total_cost - item_list[i]
        if complement in item_list[i+1:]:
            j = item_list[i+1:].index(complement)
            j = j+1+i
            break
    return (i+1, j+1)

def main():
    no_cases = int(stdin.readline())
    for i in range(no_cases):
        t_cost = int(stdin.readline())
        n_items = int(stdin.readline())
        items = [int(x) for x in stdin.readline().split()]
        if len(items) != n_items:
            return 1
        p_items = GetItems(items, t_cost)
        print 'Case #%d: %d %d' % (i+1, p_items[0], p_items[1])
    return 0


if __name__ == '__main__':
    main()
