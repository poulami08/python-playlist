try:
    a = int(input("enter a number : "))
    c = 1/a
    print(c)
except ValueError as e:
    print("exception occured")
    print(e)

except ZeroDivisionError as e:
    print("exception2 occured")
    print(e)

print("thanks for using this code!")