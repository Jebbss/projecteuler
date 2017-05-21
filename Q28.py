# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:

#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

def main():
    sumDiag = 1
    for x in range (1,501):
        sumDiag += sum4Corner(x)
    print sumDiag

def sum4Corner(n):
    area = 4*((2*n + 1)**2)
    return area - 12*n
    
