# write a program to print third, fifth and sevemth element from a list using enumerte function.

list = [1,2,3,4,5,6,7,8,9,12,50,14,47,125]
for index, item in enumerate(list):
    if index%2 == 0:
        print(f"the {index +1}th element is {item}")
