num = int(input("Please enter a positive integer:"))
print("the factors of", num, "are")
for i in range(1,num+1,1):
    if num%1==0:
        print(i)