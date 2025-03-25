# '''
# For Loops
# '''
# # i = 0

# # # while i<10:
# # #     print(i)
# # #     if i == 4:
# # #         break
# # #     if i % 2 == 1:
# # #         continue
# # #     i += 1

# # for i in range(10):
# #     print(i)
# #     if i %2 == 1:
# #         print('Dont with', i)
# #         continue

# '''
# Slicing
# '''

# # s = "abcdefghijklmnop"

# # #prints the first ten indexes starting with 0 then adds 3 until it reaches 9.
# # print(s[0:10:3])

# # #prints the first 5 indexes
# # print(s[:5])

# # #prints everything from the 12th index
# # print(s[12:])


# '''
# Classes
# '''

# # a = ['purple', 12]
# # b = ['green',  10]





class BowlingBall:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight

def printbbinfo(bb):
    print('Color of a is', bb.color)
    print('Weight of a is',bb.weight, 'pounds')


c = BowlingBall('red', 8)
printbbinfo(c)

"""
Dictionary examples
"""


myDict = {}

for num in range(10):
    myDict[num] = num
    
print(myDict)

myDict[0] = 5

print(myDict)