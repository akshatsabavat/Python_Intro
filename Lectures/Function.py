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