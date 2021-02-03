# Number 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list[4:8] + my_list[0:4])

# Number 2
n = int(input("Please enter a single digit variable: "))
if 0 <= n < 10:
    print(list(range(0, n, 2)))
else:
    print("Invalid value!")
