#loop syntax stays very differnt in python as its all about indentation
for x in "Python" :
    print(x) # prints the letters one by one

for q in ['a','b','c']:
    print(q) # prints all the elements of the array

for x in range(0,10,2): #range function has 3 arguments start no, end no and step if step is 2 it prints even numbers
    print(x) # range doesnt return a list

#flag technique
names = ["Ahon","Mary"]
flag = False
for name in names:
    if name.startswith("J"):
        print("Found")
        flag = True
        break

if not flag:
    print("Not found")

#Guess Game (while loop application)
guess_number = 0
answer = 5

while answer != guess_number:
    guess_number = int(input("Enter Guess = ")) #int is the type coeertion used to conver the user imput to string
else:
    print("Correct number guessed") # this is used when the while loop runs successfully with no break statement
