# Parameter n is a number
# return 100 times parameter

# This breaks ability to import function enlarge from other files
# if left in global scope:
# print('Hello, world')
# y = int(input('Please input a number '))
# print(y, enlarge(y))

def enlarge(n):
    return n * 100

x = 5
print(enlarge(x))

y = int(input('Please choose a number: '))
print(enlarge(y))

# if __name__ == '__main__':
#     # only run the code below if executing this script from the command line
#     # otherwise don't run it
#     print('Hello!')
#     y = int(input('Please choose a number: '))
#     print(y, enlarge(y))