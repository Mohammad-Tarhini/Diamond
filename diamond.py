#Write a Python program that prompts the user to enter a number of rows and then generates a symmetrical "palindrome" star pattern, centered to form a diamond shape.
# IN SOLUTION I take a point  on daimon as orign of yox system and get  an equation of line for each side  of diamon
x=int(input("please enter an positive integer number: "))
for i in range(-x+1,x):
    for j in range(-x+1,x):
        if i<=j+x-1 and  i<=-j+x-1 and i>=j-x+1 and i>=-j-x+1:
            print("*",end="")
        else:
            print(" ",end="")
        
    print("")
