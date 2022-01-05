# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:27:34 2021

@author: julien
"""
import timeit
import sys
sys.setrecursionlimit(120)
import random
def is_palindrome(word):
    """Check if input is a palindrome."""
    if word == "" or len(word) == 1:
        return True
    elif word[0]==word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
    
    
def rec_pow(a, b):
    """Compute a**b recursively"""
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return (rec_pow(a,b/2))**2
    else:
        return ((rec_pow(a, (b-1)/2))**2)*a
    
    
    
def binary_search(sorted_list, lower, upper, element):
    """Return the position of the element in the sublist of sorted_list
    starting at position lower up to (but excluding) position upper 
    if it appears there. Otherwise return -1.
    """
    i = (lower + upper)//2
    
    if lower == upper:
        return -1
    
    elif element < sorted_list[i]:
        return binary_search(sorted_list, lower, i, element)
    
    elif element == sorted_list[i]:
        return i 
    else:
        return binary_search(sorted_list, i+1, upper, element)
         

def random_increasing_integer_sequence(length):
    """Return an increasing list of integers of the given length."""
    current = 0
    res = []
    for i in range(length):
        current += random.randint(1, 10)
        res.append(current)
    return res
   
    
def pp_words():
    with open('sortedpp.txt') as file:
        return [w.strip() for w in file]


class Sudoku:
    def __init__(self, filename):
        """Initilize rows, columns and squares as empty."""
        self.board = [([0]*9).copy() for _ in range(9)]
        self.read_board(filename)
        
    def read_board(self, filename):
        """Read a board from the given file."""
        with open(filename) as file:
            for (x, line) in enumerate(file):
                for (y, element) in enumerate(line):
                    if element in '123456789':
                        self.put(x, y, int(element))
                        
    def __str__(self):
        """Give a string representation of the board."""
        res = ''
        for x in range(9):
            if x == 0:
                res += '┌───┬───┬───┐\n'
            if x == 3 or x == 6:
                res += '├───┼───┼───┤\n'
            for y in range(9):
                if y % 3 == 0:
                    res += '│'
                if self.board[x][y] != 0:
                    res+=str(self.board[x][y])
                else:
                    res+='.'
            res+='│\n'
        res += '└───┴───┴───┘\n'
        return res

    def put(self, row, column, value):
        """Set value in cell (x,y)."""
        self.board[row][column] = value
        
    def delete(self, row, column):
        """Delete content of cell (x,y)."""
        self.board[row][column] = 0

    def check_row(self, row, value):
        """Return True if the value is already contained in the row."""
        return value in self.board[row]
    
    def check_column(self, column, value):
        """Return True if the value is already contained in the column."""
        for row in self.board:
            if value == row[column]:
                return True
        return False
    
    def check_box(self, row, column, value):
        """Return True if the 3x3 box that contains the cell with the given
        row and column contains already value.
        """
        for x in range(row//3*3, row//3*3 + 3): 
            for y in range(column//3*3, column//3*3 + 3):
                if value == self.board[x][y]:
                    return True
        return False
    
    def check(self, row, column, value):
        """Return True if the value is already in the row, column or box of
        the given cell."""
        return self.check_row(row, value) or \
            self.check_column(column, value) or \
            self.check_box(row, column, value)
        
    def find_first_empty(self):
        """Return the first empty cell if there is one, otherwise None."""
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    return (x,y)
        return None
    
    def solve(self):
        """Solve the given Sudoku. When a solution is found, print 'Found solution!'
        followed by the solution in the next line.
        """
        empty = self.find_first_empty()
        (x,y) = empty
        if empty == None :
            print(self)
            return True 
        
        for guess in (1,10):
            if self.check(x, y, guess) != True:
                self.put(x, y, guess)
                if self.solve() == True:
                    return True

                self.delete(x, y)
                     
        return False    
    
    
    
    
    
def read_positive_integer(text, position):
    """Read a number starting from the given position, return it and the first
    position after it in a tuple. If there is no number at the given position
    then return None.
    """
    strnum= ['1','2','3','4','5','6','7','8','9','0']
    if text[position] not in strnum:
        return None
    
    number =''
    rk = 0
    for i in (text[position:]):
        if i in strnum:
            number+= i
            rk +=1
            print(number)
        else:
            return (int(number),(rk+position))
    return (int(number),len(number)+position)


def evaluate(expression, position):
    """Evaluate the expression starting from the given position.
    Return the value and the first position after the read
    sub-expression. If the string starting at the given expression
    is not an arithmetic expression, return None.
    """
    value = read_positive_integer(expression, position)
    print(value)
    if value != None:
        return value 
   
    else:
        part1, nextoperator = evaluate(expression,position+1)
        operator = expression[nextoperator]
        part2, nextoperator = evaluate(expression, nextoperator + 1)
        if operator == '-':
            return part1 - part2, nextoperator+1
        elif operator == '+':
            return part1 + part2, nextoperator+1
        else:
            return part1*part2, nextoperator+1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    