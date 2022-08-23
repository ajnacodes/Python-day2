# 🚨 type a 2 digit number and it will calculate the 2 numbers
two_digit_number = input("Type a two digit number: ")
# convert string to integer
num_one = int(two_digit_number[0])
num_two = int(two_digit_number[1])
# calculate result
result = num_one + num_two
print(result)