# #read from stdin

# x = input('Enter somthing: ')
# print('You said', x)
# print('You input is a', type(x))

# #But I want an int..

# x = int(x)

# #look up the function format

# print('Your input squared is', x**2)

#read from a file

# file = open('2024inputEx.txt')
# all_the_text = file.read()
# print(all_the_text, end='')
# file.close()


# line_number=1

# file = open('2024inputEx.txt')

# for line in file:
#     print(line_number, line)
#     line_number +=1

# file.close()

# with open('2024inputEx.txt') as file:
#     lines = 0
#     for line in file:
#         lines +=1
#         print('The file had' + str(lines) + 'lines')

# print("Outside the with bloick.")


# with open('2024inputEx.txt', 'rb') as file:
#     print(file.read(12))
#     print(file.readline())


with open('2024inputEx.txt', 'w') as file:
    file.write('Hello!\n')


