#!/usr/bin/env python

'''
Problem

After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Input

The first line of input contains 3 integers, L, D and N separated by a space. D lines follow, each containing one word of length L. These are the words that are known to exist in the alien language. N test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.

Output

For each test case, output

Case #X: K

where X is the test case number, starting from 1, and K indicates how many words in the alien language match the pattern.
'''

from sys import stdin

def Tokenize(string):
    n = len(string)
    tokens = []
    i = 0
    while i < n: 
        if string[i] == '(':
            token = []
            i+=1
            while string[i] != ')':
                token.append(string[i])
                i+=1
            token = set(''.join(token))
        else:
            token = string[i]
        tokens.append(token)
        i+=1
    return tokens

def Matches(tokens, dword):
    for i in range(len(dword)):
        if not dword[i] in tokens[i]:
            return False
    return True

def main():
    meta = [int(x) for x in stdin.readline().split()]
    wlen, dlen, no_cases = meta[0], meta[1], meta[2]
    dictionary = []
    for i in range(dlen):
        dictionary.append(stdin.readline())
    for i in range(no_cases):
        word = Tokenize(stdin.readline())
        no_matches = 0
        for j in range(dlen):
            if Matches(word, dictionary[j]):
                no_matches+=1
        print 'Case #%d: %d' % (i+1, no_matches)
    return 0

if __name__ == '__main__':
    main()
