# function declaration syntax

# Java Script Style - 1 (ES5)
# const MyName = function() {
#    return
# }

# Java Script Style - 2
# function Myname() {
#    return
# }

# Java Script Style - 3 (ES6)
# const Myname = () => {
#    return someVal;
# }

#Python function syntax
def Add(number, by):
    return number + by

print(Add(2,3))

#Multiple returns also possible in the form of tuples
def Multiply(number,by):
    return (number,by,number * by)

print(Multiply(2,5))

#Making code more readable
print(Multiply(number = 2, by = 3))

#Argument techniques
def multiply(*list): #Lets Python know that u wanna pass in a tuple
    total = 1
    for number in list:
        total *= number
    return total

print(multiply(2,3,4,5,2,1))

def save_user(**user): #lets us pass multiple different object types
    print(user)

save_user(id = 2010110063, name = "Akshat Sabavat") # returns a object like in javascript