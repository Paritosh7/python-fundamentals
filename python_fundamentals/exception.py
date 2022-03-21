from aifc import Error


try:
    print(int("a"))
except ValueError as e:
    print("That can't be done",e)

print("This is the end of my program")