#!/usr/bin/env python

'''
Problem

In the exciting game of Join-K, red and blue pieces are dropped into an N-by-N table. The table stands up vertically so that pieces drop down to the bottom-most empty slots in their column. For example, consider the following two configurations:

    - Legal Position -

          .......
          .......
          .......
          ....R..
          ...RB..
          ..BRB..
          .RBBR..

          

   - Illegal Position -

          .......
          .......
          .......
          .......
   Bad -> ..BR...
          ...R...
          .RBBR..

In these pictures, each '.' represents an empty slot, each 'R' represents a slot filled with a red piece, and each 'B' represents a slot filled with a blue piece. The left configuration is legal, but the right one is not. This is because one of the pieces in the third column (marked with the arrow) has not fallen down to the empty slot below it.

A player wins if they can place at least K pieces of their color in a row, either horizontally, vertically, or diagonally. The four possible orientations are shown below:

      - Four in a row -

     R   RRRR    R   R
     R          R     R
     R         R       R
     R        R         R

     
In the "Legal Position" diagram at the beginning of the problem statement, both players had lined up two pieces in a row, but not three.

As it turns out, you are right now playing a very exciting game of Join-K, and you have a tricky plan to ensure victory! When your opponent is not looking, you are going to rotate the board 90 degrees clockwise onto its side. Gravity will then cause the pieces to fall down into a new position as shown below:

    - Start -

     .......
     .......
     .......
     ...R...
     ...RB..
     ..BRB..
     .RBBR..

     

   - Rotate -

     .......
     R......
     BB.....
     BRRR...
     RBB....
     .......
     .......

     

   - Gravity -

     .......
     .......
     .......
     R......
     BB.....
     BRR....
     RBBR...

Unfortunately, you only have time to rotate once before your opponent will notice.

All that remains is picking the right time to make your move. Given a board position, you should determine which player (or players!) will have K pieces in a row after you rotate the board clockwise and gravity takes effect in the new direction.
Notes

    You can rotate the board only once.
    Assume that gravity only takes effect after the board has been rotated completely.
    Only check for winners after gravity has finished taking effect.

Input

The first line of the input gives the number of test cases, T. T test cases follow, each beginning with a line containing the integers N and K. The next N lines will each be exactly N characters long, showing the initial position of the board, using the same format as the diagrams above.

The initial position in each test case will be a legal position that can occur during a game of Join-K. In particular, neither player will have already formed K pieces in a row.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is one of "Red", "Blue", "Neither", or "Both". Here, y indicates which player or players will have K pieces in a row after you rotate the board.
'''
from sys import stdin

def rotate(board):
    new_board = []
    for row in board:
        new_row = []
        width = len(row)
        row = row.replace('.', '')
        to_append = width - len(row)
        if to_append:
            for i in range(to_append):
                new_row.append('.')
        for c in row:
            new_row.append(c)
        new_board.append(new_row)
    return new_board

def check_sequential(c, l):
    for x in l:
        if not x == c: return False
        #print c, 'against', x
    return True

def check_win(board, k):
    height = len(board)
    width = len(board[0])
    ans_set = []
    for x, row in enumerate(board):
        for y, c in enumerate(row):
            xtrue = x + k <= height
            ytrue = y + k <= width
            nytrue = y - (k-1) >= 0
            if not c == '.':
                color = c
                if ytrue:
                    if check_sequential(color, [ch for ch in row[y:y+k]]):
                        ans_set.append(color)
                if xtrue:
                    if check_sequential(color, [r[y] for r in board[x:x+k]]):
                        ans_set.append(color)
                if ytrue and xtrue:
                    temp = y
                    l = []
                    for rw in board[x:x+k]:
                        l.append(rw[temp])
                        temp+=1


                    if check_sequential(color, l):
                        ans_set.append(color)
                if nytrue and xtrue:
                    temp, l = y, []
                    
                    for rx in board[x:x+k]:
                        l.append(rx[temp])
                        temp-=1

                    if check_sequential(color, l):
                        ans_set.append(color)
    if 'R' in ans_set and 'B' in ans_set:
        return 'Both'
    elif 'R' in ans_set:
        return 'Red'
    elif 'B' in ans_set:
        return 'Blue'
    else:
        return 'Neither'
                
def main():
    no_cases = int(stdin.readline())
    for case in range(no_cases):
        length, k = [int(x) for x in stdin.readline().split()]
        board = []
        for row in range(length):
            board.append(stdin.readline().replace('\n', ''))
        board = rotate(board)
        verdict = check_win(board, k)
        print 'Case #%d: %s' % (case+1, verdict)
    return

if __name__ == '__main__':
    main()
