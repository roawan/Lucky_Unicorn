# Ask user to input a number
number = int(input("Choose a number"))
# Multiply it by 5
times_five = number * 5


answer = "{} times 5 is equal to " \
         "{}" .format(number, times_five)


# Output the result
print(answer)
