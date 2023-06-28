def wrapper(fun):
    def inner():
        print('Inner Function')
        fun()
        print('Inner Function')
    return inner


@wrapper
def display():
    print('Outer Function')

a = display()