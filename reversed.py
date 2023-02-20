num = int(input("Number:"))

reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

    print("Reversed Number: " + str(reversed_num))

divisior = 0
for i in range(1, reversed_num + 1):
    if reversed_num % i == 0:
        divisior += 1
        print("divisior: ", i)
print("sum of divisiors c: ", divisior)
