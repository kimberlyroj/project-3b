# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 1/18/2021
# Description: Write a program that asks the user to enter a positive integer, then prints a list of all positive integers that divide that number evenly, including itself and 1, in ascending order
num = int(input("Please enter a positive integer:"))
print("the factors of", num, "are")
for i in range(1,num+1,1):
    if num%1==0:
        print(i)