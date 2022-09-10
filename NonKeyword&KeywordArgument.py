def adder(x, y, z):
    print("sum", x+y+z)

adder(1,2,3)


# Non keyword argument
def non_key_arg(*num):
    print(type(num))
    sum = 0
    for x in num:
        sum += x
    

    print("sum", sum)

# Keyword argument
def key_arg(**kargs):
    print(type(kargs))
    
    for key, value in kargs.items():
        print(key, value)

def both_key_and_non_arg(*args, **kargs):

    print(args)
    print(kargs)


non_key_arg(1, 2, 3, 4, 5)

key_arg(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890, age=40, name="John")

both_key_and_non_arg(1,2,3,4, name="john", age=10)