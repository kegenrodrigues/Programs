# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],#k=4;k=3;k=2;k=1
              [2,3,1,5,6],#
              [4,5,2,1,3],#
              [3,4,5,2,1],#
              [5,6,4,3,2]]#

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(matrix):
    n=len(matrix)
    #Checking for repeated elements within each row
    i=0
    while i<n:
        j=0    
        while j<n:
            k=1
            while k<n-j:
                
                if matrix[i][j]==matrix[i][j+k]:
                    return False
                k+=1
            j+=1        
        i+=1    
    no_repeated_row=True    
    
    #Checking for repeated elements within each column(of different rows)
    i=0
    while i<n:
        j=0    
        while j<n:
            k=1
            while k<n-j:
                
                if matrix[j][i]==matrix[j+k][i]:
                    return False
                k+=1
            j+=1        
        i+=1   
    no_repeated_row=True
    
    #Checking for valid numbers 
    valid=[]
    i=1
    while i<=n:
        
        
        valid.append(i)
        i+=1
        
    i=0
    while i<n:
        j=0    
        while j<n:
            k=1
            while k<n-j:
                
                if (matrix[i][j] not in valid):
                    return False
                k+=1
            j+=1        
        i+=1 
    return True
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False


