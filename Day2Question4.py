
# Question
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number.Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

user_input = input("Enter a sequence of comma-separated numbers: ")

user_input_list = user_input.split(", ")
user_input_tuple = tuple(user_input_list)

print(user_input)
print(type(user_input_list))
print(list(user_input_list))
print(type(user_input_tuple))
print(user_input_tuple)

