try:
    i = int(input("enter a number : "))
    c =1/i
except Exception as e:
    print(e)
    exit()

finally:
    print("we are done")

print("thanks for using the program")