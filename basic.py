print("Hello, world!")
print("Fourth")
print("Fifth")  # to re-order line use ctrl+X to cut and then ctrl+V to paste
print("Sixth")
# highlight with "" or \"\"
print('My favourite quote is "To be or not to be"')
print("My favourite quote is \"To be or not to be\"")
# to comment all the code just select all the code and press ctrl+/

message = "this string is stored in a variable"
print(message)  # when you assign a varaiable
print(message)  # you don't need to use "" this to print

capital_of_spain = "Madrid"  # variables only have
capital_of_france = "Paris"  # letters, no's, _
capital_of_germany = "Berlin"  # Can't start vth no's
print(capital_of_spain)  # Can't contain spaces
print(capital_of_france)  # Can't be "for,if"
print(capital_of_germany)

pythonCreationDate = "February,1991"  # Camel case = Ex : myVariableName
java_creation_date = "May,1995"  # Snake case = Ex : my_variable_name
JavascriptCreationDate = "December, 1995"  # Pascal case = Ex : MyVariableName
print(pythonCreationDate)
print(java_creation_date)
print(JavascriptCreationDate)

song = "The first song"  # here both song1 & song
song = "The second song"  # are updated based on
print(song)  # where we put print statement
song1 = "The first song1"
print(song1)
song1 = "The second song1"

msg = "The first msg"
print(msg)
msg = "The second msg"
print(msg)
msg = "The third msg"
print(msg)

msg1, msg2 = "World", "Hello"  # multiple assignments
msg1, msg2 = msg2, msg1  # swap variables to order
msg3, msg4, msg5 = "Name", "Is", "My"
msg3, msg4, msg5 = msg5, msg3, msg4
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

age = 24  # integer
temp = 98.6  # float
is_true = True  # boolean always capital True/False
name = "Sony"  # string
my_list = [1, 2, 3]  # list

print(type(age))
print(type(temp))  # to know the type of variable
print(type(is_true))
print(type(name))
print(type(my_list))

variable = 2
print(type(variable))
# we can use same variable
variable = 0.0       # several times which is
print(type(variable))  # called Dynamic typing
# only used in Python
variable = False
print(type(variable))

variable = ""
print(type(variable))

variable = [4]
print(type(variable))

pi = 3.141592653589793
square_root_8 = 2.8284271247461903
pi = int(pi)  # type-casting changing type of variable
square_root_8 = int(square_root_8)
print(pi)
print(square_root_8)

var = "10"  # it is a string
print(var)
print(type(var))  # can convert to int because 10 is int
var = int(var)  # but can't convert a pure string like "hey"
print(var)    # if it's "hey" & convert to int
print(type(var))  # then it will be a Type Error

var1 = None  # if we want to assign a variable without a value
print(type(var1))  # then use None keyword, so var has no value now

# Arithmetic operators
a, b, c = 2, 2, 0.5
sum = a + b + c
product = a * b * c
print(a + b + c)
print(0 - (sum))
print(a * b * c)
print(sum / product)
e, f, g = 2, 8, 5
prod = e * f
print(prod // g)  # floor division it rounds the integer
print(prod % g)  # modulus it gives remainder
print(e ** f)  # exponentiation raise to the power
print(f ** g)

number = 0
number += 5
print(number)   # To increment or decrement a variable
number -= 2
print(number)  # we use shorthand operators
number += number
print(number)

h, i, j, k = False, False, True, True
print(h or i)
print(i or j)      # logical OR only False if both are False
print(j or k)      # otherwise True
print(h or i or j or k)
print(h and i)
print(i and j)     # logical AND only True if both are True
print(j and k)     # otherwise False
print(h and i and j and k)
print(not h)      # if h is False then not h is True
print(not j)      # boolean negation
print(not (h and i))
print(not (i or j))


def greet():  # : is colon
    print("Hello, World!")


def say_goodbye():
    print("Goodbye, World!")


greet()  # yes, even after printing they won't execute
say_goodbye()  # unless, call functns greet() & say_goodbye()


def print_number(n):
    print(n)   # function declaration


print_number(10)  # when you  call a func(), you don't need
print_number(20)  # indented whitespace


def farewell(name):  # we take variables & strings inside parantheses
    msgs = "Goodbye, " + name  # we combine strings with + operator known as concatenation
    print(msgs)


farewell("Anu")  # Anu, Nithya, Nandu are called Arguments
farewell("Nithya")  # we define function with parameters
farewell("Nandu")


def two_sum(odd, even):
    print(even + odd)


def three_sum(odd, pos, even):
    print(even + odd + pos)


two_sum(7, 10)
three_sum(3, 5, 8)
two_sum(10, 9)
three_sum(5, 14, 6)


def product(num1, num2):  # when we return a value we use
    return num1 * num2  # that value not single time but multiple times


print(product(2, 4))
print(product(8, 2))
print(product(4, 8))
print(product(8, 8))


def greet(name: str) -> None:  # type hint
    print("Hello, " + name)
    return  # this line can be return/return None/simply skip this line


print(type(greet("Anuu")))  # still we get same output


def add_one(n):  # local scope & global scope
    n = n + 1
    print(n)  # local scope


n = 10  # global sccope

add_one(n)  # output 11

print(n)  # output 10

n = 100


def print_local_variable(num: int) -> None:
    print(num)


print_local_variable(n)
print(n)

# second parameter must have a default value


def greet(name, punctuation="!") -> None:
    print("Hello, " + name + punctuation)


greet("Papa", "!")  # default arguments
greet("Papa")


def check_equal(x, y) -> bool:
    return x == y           # Comparison Operators


def check_not_equal(x, y) -> bool:
    return x != y


def check_less_than(x, y) -> bool:
    return x < y


def check_greater_than(x, y) -> bool:
    return x > y


def check_less_than_or_equal(x, y) -> bool:
    return x <= y


def check_greater_than_or_equal(x, y) -> bool:
    return x >= y


print("2 is equal to 2:", check_equal(2, 2))
print("-2 is equal to 2:", check_equal(-2, 2))

print("-2 is not eual to 2:", check_not_equal(-2, 2))
print("2 is not eual to 2:", check_not_equal(2, 2))

print("2 is less than 3:", check_less_than(2, 3))
print("3 is less than 3:", check_less_than(3, 3))

print("3 is greater than 2:", check_greater_than(3, 2))
print("3 is greater than 3:", check_greater_than(3, 3))

print("3 is less than or equal to 3:", check_less_than_or_equal(3, 3))
print("4 is less than or equal to 3:", check_less_than_or_equal(4, 3))

print("3 is greater than or equal to 3:", check_greater_than_or_equal(3, 3))
print("2 is greater than or equal to 3:", check_greater_than_or_equal(2, 3))

# if we have IF statement inside a function
# the code under IF statement need to be intended twice


def is_balance_low(balance: int) -> None:
    if balance <= 100:
        print("Warning: Low balance")


is_balance_low(99)
is_balance_low(100)
is_balance_low(101)


def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        new_balance = balance - bill
        return new_balance
    return balance


print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))

# can have multiple return statements in IF & Else


def get_min(a: int, b: int) -> int:
    if a <= b:
        return a
    else:
        return b


print(get_min(10, 11))
print(get_min(5, -7))
print(get_min(20, 20))

# Else-If or simply Elif Statement


def check_range(num: int) -> str:
    if num < 0:
        return "negative"
    elif num == 0:
        return "zero"
    elif num > 0 and num < 10:
        return "positive single digit"
    elif num >= 10:        # or you can put Else here in place of Elif
        return "positive multi digit"


print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))

# we can use logic operators like OR, AND, NOT
# in conditional statements


def discount_applies(age: int) -> bool:
    if age < 18 or age >= 65:
        return True
    return False


print(discount_applies(17))
print(discount_applies(18))
print(discount_applies(40))
print(discount_applies(65))
print(discount_applies(70))


def is_truthy(value) -> str:
    if value:
        return "Truthy"
    return "Falsy"


print(0, "is", is_truthy(0))
print(10, "is", is_truthy(10))

print(0.0, "is", is_truthy(0.0))
print(10.0, "is", is_truthy(10.0))

print("empty str", "is", is_truthy(""))
print("non-empty str", "is", is_truthy("non-empty str"))
