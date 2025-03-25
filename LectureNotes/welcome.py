import sys

#find the length of the argv array
lengthOfArgs = len(sys.argv)

try:
    #if there are too many or not enough parameters, the program ends
    if lengthOfArgs != 3:
        print("USAGE: welcome.py characters replacements")
        exit()

    #the two sets are passed to local variables
    firstSet = sys.argv[1]
    secondSet = sys.argv[2]

    #get length of the strings and then compare. If not equal in length, throw error
    lengthOfFirstSet = len(firstSet)
    lengthOfSecondSet = len(secondSet)

    if lengthOfFirstSet != lengthOfSecondSet:
        raise ValueError("ERROR: Arguments must be the same length.")
    
    #read in a line from user and turn it into a list
    #this is not only for accessing the characters
    #it is also so we can update and replace the character
    #which would be more complicated with a string.
    #if we use replace, it might replace a character we had
    #previously replaced, causing confusion and the wrong answer
    myString = list(sys.stdin.read())
    
    #if the user enters a blank space, end the program
    if myString[0] == '\n':
        exit()

    #create iterator for the index of the string from the user
    iterator = 0 

    '''
    this while loop will compare each individual index from the user string.
    subsequently it will iterate through the first set backwards, so as to
    only use the first instance of a character should there be more than
    one instance of it. If we find a match we use the corresponding index 
    of the first set, to find the character we will replace with in the 
    the second set. This will break the for loop. The iterator will be
    incremented and the for loop will run again in the new index until we 
    reach the end and have replaced every character. 
    '''
    while iterator < len(myString):
        for indices in range((lengthOfFirstSet-1), -1, -1):
            #print(firstSet[indices])
            if myString[iterator] == firstSet[indices]: 
                #print(iterator)
                #print(myString[iterator])
                myString[iterator] = secondSet[indices]
                #print(secondSet[indices])
                break
            
        iterator+=1
    #convert the updated list to a string
    myString = ''.join(myString)
    
    #print the new string
    print(myString, end='')


#error where two strings are not the same size
except ValueError as ve:
        print(ve)
    

