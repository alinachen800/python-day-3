# two types of loops 1. while loops 2. for loops
# while loop -you do not know how many times it's going to happen
# risk of creating an infinite loop
'''
2 ways to avoid the infinite loop
 1. make a condition that can be false
 2. use the break keywords
'''
# for loop- when you know the amount of time

while True:
    borrow_sweater = input("Can I borrow your sweater?")
    if borrow_sweater == "Yes":
        print("Thank you!")
        break
    else:
        print("oh no")

#Blastoff
#Create a countdown before a spaceship launches
count = 10
while count >= 1:
    print(count)
    count = count - 1
print("Blastoff!")
