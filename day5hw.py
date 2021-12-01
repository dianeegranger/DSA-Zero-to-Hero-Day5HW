# November 30, 2021

# Diane Granger 
# dianeegranger@gmail.com

# Data Structures and Algorithms Zero to Hero
# LetsUpgrade
# Instructor:  Subrat Kkumar Swain

# Day 5 Assignment
# Dynamic Programming using Memoization Method
# Rod Cutting Problem
# Problem Statement:
# Different lengths of Rods are given to you.  
# You have to sell x meters of rod.
# What combination of rods will add up to x meters and give the you Maximum Profit? 

def rodcut(price, length):
  rev = [0] * (length + 1)  # initialize new array to all 0s
  cuts = [-1] * (length + 1)  # initialize new array to all -1s
  
  maxrev = -1   # sentinel value

  for i in range(1, length + 1):
        for j in range(i):
            temp = price[j] + rev[i - j - 1] 
            if temp > maxrev:
                maxrev = price[j] + rev[i - j - 1]    # get max price
                cuts[i] = j + 1   # get rod cut for max price
        rev[i] = maxrev
  return rev[length], cuts

def print_cuts(cuts, length):
    print('Rod Cuts: ')
    while length > 0:
        print(cuts[length], end=" ")
        length -= cuts[length]

if __name__ == '__main__':

  # sample data
  price = [1, 5, 8, 9, 10, 17, 17, 20]
  length = 4

  max_value, cuts = rodcut(price, length)
  print('Maximum Revenue: ', max_value)
  print_cuts(cuts, length)

# OUTPUT
# PS C:\Users\diane\OneDrive\Desktop\LetsUpgrade\Data Structures and Algorithms\dsa probs> python -u "c:\Users\diane\OneDrive\Desktop\LetsUpgrade\Data Structures and Algorithms\dsa probs\day5hw.py"
# Maximum Revenue:  10
# Rod Cuts:
# 2 2
# PS C:\Users\diane\OneDrive\Desktop\LetsUpgrade\Data Structures and Algorithms\dsa probs> 