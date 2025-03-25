class Text:
    def __init__(self, chars = None):
        self.headNode = None
        self.tailNode = None
        self.sizeof = 0

        if chars is None:
            return

        elif isinstance(chars, str):
            for index in range(len(chars)):
                if index == 0:
                    self.headNode = Node(chars[index])
                    self.tailNode = self.headNode
                    prevNode = self.headNode
                    self.sizeof += 1
                if index > 0:
                    prevNode.next = Node(chars[index])
                    self.tailNode = prevNode.next
                    self.tailNode.prev = prevNode
                    prevNode = prevNode.next
                    self.sizeof += 1
            return

        elif isinstance(chars, Text):
            currNode = chars.headNode
            self.headNode = Node(currNode.char)
            self.tailNode = self.headNode
            prevNode = self.headNode
            currNode = currNode.next
            self.sizeof = 1

            while currNode:
                prevNode.next = Node(currNode.char)
                prevNode.next.prev = self.tailNode
                self.tailNode = prevNode.next
                prevNode = self.tailNode
                currNode= currNode.next
                self.sizeof += 1
        
        else:
            raise TypeError("Not a valid type of object.")

    def append(self, charc):

        if not isinstance(charc, str):
            raise TypeError("Input is wrong type.")

        if len(charc) != 1:
            raise ValueError("String too long.")

        if self.headNode is None:
            newNode = Node(charc)
            self.headNode = newNode
            self.tailNode = newNode
            self.sizeof = 1
        else:
            newNode = Node(charc)
            currtail = self.tailNode
            currtail.next = newNode
            newNode.prev = currtail
            self.tailNode = newNode
            self.sizeof += 1

    def clear(self):
        self.headNode = None
        self.tailNode = None
        self.sizeof = 0

    def copy(self):
        newList = Text()
        if not self.headNode:
            return newList
        currNode = self.headNode
        while currNode:
            newList.append(currNode.char)
            currNode = currNode.next
        
        return newList


    def extend(self, extender):
        
        if isinstance(extender, str):
            for char in extender:
                self.append(char)
            return

        elif isinstance(extender, Text):
            currNode = extender.headNode
            while currNode:
                self.append(currNode.char)
                currNode = currNode.next
        else:
            raise TypeError("Input not valid type.")

    
    def insert(self, index, character):
                
        if not isinstance(character, str) or not isinstance(index, int):
            raise TypeError("Wrong Type")
        if len(character) != 1:
            raise ValueError("Wrong size string.")

        if not self.headNode:
            newList = Text(character)
            self.headNode = newList.headNode
            self.tailNode = self.headNode
            self.sizeof += 1
            return

        if index < 0:
            negativeIndex = abs(index)
            if negativeIndex > self.sizeof:
                raise IndexError("Index out of range")

            position = 1 
            currNode = self.tailNode
            nextNode = None

            while position != negativeIndex:
                currNode = currNode.prev
                nextNode = currNode.next
                position += 1

            if negativeIndex == 1:
                newNode = Node(character)
                currNode = currNode.prev
                self.tailNode.prev = newNode
                newNode.next = self.tailNode
                newNode.prev = currNode
                currNode.next = newNode
                self.sizeof += 1
                return
           
            if negativeIndex == self.sizeof + 1 or negativeIndex == self.sizeof:
                newNode = Node(character)
                newNode.next = self.headNode
                self.headNode.prev = newNode
                self.headNode = newNode
                self.sizeof += 1
                
            newNode = Node(character)
            nextNode.next = newNode
            currNode.prev = newNode
            newNode.prev = nextNode
            newNode.next = currNode
            self.sizeof += 1
            return
        else:
            listlength = self.sizeof
            if index >= 0 and listlength >= index:
                position = 0
                currNode = self.headNode
                prevNode = None
                if index == 0:
                    newNode = Node(character)
                    newNode.next = self.headNode
                    self.headNode.prev = newNode
                    self.headNode = newNode
                    self.sizeof += 1
                    return
                
                if index == listlength:
                    newNode = Node(character)
                    self.tailNode.next = newNode
                    newNode.prev = self.tailNode
                    self.tailNode = newNode
                    self.sizeof += 1
                    return

                while position != index:
                    prevNode = currNode
                    currNode = currNode.next
                    position += 1

                newNode = Node(character)
                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = currNode
                currNode.prev = newNode
                self.sizeof += 1
                return
            else:
                raise IndexError("Index out of range")

    def pop(self, index = None):

        if self.headNode is None:
            raise IndexError("Pop from empty list.")

        lengthlist = self.sizeof

        if index == None:
            if lengthlist == 1:
                noderemoved = Node(self.headNode.char)
                self.headNode = None
                self.tailNode = None
                self.sizeof = 0
                return noderemoved.char
            else:
                noderemoved = Node(self.tailNode.char)
                prevNode = self.tailNode.prev
                self.tailNode = prevNode
                prevNode.next = None
                self.sizeof -= 1
                return noderemoved.char

        else:
            if not isinstance(index, int) or index == None:
                raise TypeError("Wrong input.")
            if index < 0 and abs(index) <= lengthlist:
                index = index + lengthlist
            else:
                index = index

            currNode = self.headNode
            position = 0
            prevNode = currNode

            if index > lengthlist - 1 or index < 0:
                raise IndexError("Index out of range")

            if lengthlist == 1 and index == 0:
                currNode = Node(self.headNode.char)
                self.headNode = None
                self.tailNode = None
                self.sizeof -= 1
                return currNode.char

            if index == 0:
                currNode = Node(self.headNode.char)
                nextNode = self.headNode.next
                nextNode.prev = None
                self.headNode = nextNode
                self.sizeof -= 1
                return currNode.char

            if index == (lengthlist - 1) or index == -1:
                noderemoved = Node(self.tailNode.char)
                prevNode = self.tailNode.prev
                prevNode.next = None
                self.tailNode = prevNode
                self.sizeof -= 1
                return noderemoved.char

            while position != index:
                prevNode = currNode
                currNode = currNode.next
                position += 1

            noderemoved = Node(currNode.char)
            prevNode.next = currNode.next
            prevNode.next.prev = prevNode
            self.sizeof -= 1
            return noderemoved.char


    def __len__(self):

        return self.sizeof

    def __str__(self):
        currNode = self.headNode
        text = []
        while currNode:
            text.append(currNode.char)
            currNode = currNode.next
        textstring = ''.join(text)
        return textstring

    def __getitem__(self, index):

        if self.headNode is None:
            raise IndexError("Empty list.")

        if not isinstance(index, (int,slice)):
            raise TypeError("Input wrong type.")

        if isinstance(index, slice):
            stringbean = str(self)
            sliceoflife = stringbean[index]
            newstring = Text(sliceoflife)    
            return newstring
        lengthlist = self.sizeof

        if index < 0:
            index += lengthlist
        
        if index < 0 or index >= lengthlist:
            raise IndexError("Index out of range.")
        
        stringbean = str(self)
        return stringbean[index]

        

    def head(self):
        return self.headNode

    def tail(self):
        return self.tailNode

    def __contains__(self, thestuff):
        if self.headNode is None:
                return False
                
        elif isinstance(thestuff, str):
            stringofself = str(self)
            if thestuff in stringofself:
                return True
            else:
                return False

        elif isinstance(thestuff, Text):
            stringofself = str(self)
            stringofstuff = str(thestuff)
            if stringofstuff in stringofself:
                return True 
            else:
                return False    
        else:
            raise TypeError("Wrong type.")

    def __add__(self, something):

        if self.headNode is None:
            if something is None:
                newList = Text()
                #print(newList)
                return  newList

            elif isinstance(something, str):
                newList = Text(something)
                return newList
            
            elif isinstance(something, Text):
                if something.headNode is None:
                    newList = Text()
                    return  newList
                else:
                    newList = Text(something)
                    return newList
            else:
                raise TypeError("Not a valid type.")
        else:
            if isinstance(something, str):
                rightOperand = Text(something)
                leftOperand = Text(self)
                leftOperand.extend(rightOperand)
                return leftOperand

            elif isinstance(something, Text):
                if something.headNode is None:
                    newList = Text(self)
                    return newList
                else:
                    rightOperand = Text(something)
                    leftOperand = Text(self)
                    leftOperand.extend(rightOperand)
                    return leftOperand
            else:
                raise TypeError("Not a valid type.")

    def __iadd__(self, something):
        if isinstance(something, str):
            for char in something:
                self.append(char)
        elif isinstance(something, Text):
            currNode = something.headNode
            while currNode:
                self.append(currNode.char)
                currNode = currNode.next
        else:
            raise TypeError("Not a valid type")
        
        return self


    def __setitem__(self, index, thing):
        if not isinstance(index, int) or not isinstance(thing, str):
            raise TypeError("Not a valid type of index or character.")
        if len(thing) != 1:
            raise ValueError("Not valid arguments")
        if not self:
            raise ValueError("No list")
        if abs(index) >= self.sizeof:
            raise IndexError("Index out of range.")
        
        lengthlist = self.sizeof
        if index < 0:
            index += lengthlist
        
        if index < 0 or index >= lengthlist:
            raise IndexError("Index out of range.")
        
        if self.headNode is None:
            raise IndexError("Empty list.")
        
        currNode = self.headNode
        position = 0

        while position != index:
            currNode = currNode.next
            position += 1
        
        currNode.char = thing


class Node:
    def __init__(self,char = None, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.char = char



# newObject = Text("Tits Mcgee")
# newObject.append(" ")
# newObject.append("J")
# newObject.append("r")
# newString = str(newObject)
# print(newString)
# newObject.extend(" and company.")
# newString = str(newObject)
# print(newString)
# lenthofthisstring = len(newObject)

# print(lenthofthisstring)

# #newObject.insert(27, "!")
# newObject.pop()
# print(newObject)
# newObject.pop(4)
# print(newObject)
# newObject.pop(1)
# print(newObject)
# newObject.pop(0)
# print(newObject)
# newObject.pop()
# print(newObject)
# print(len(newObject))

# anotherObject = Text("Word")
# anotherObject.insert(0, "a")
# #print(anotherObject)
# anotherObject.insert(5, "a")
# #print(anotherObject)
# anotherObject.pop()
# #print(anotherObject)
# anotherObject.pop(0)
# #print(anotherObject)
# theOtherstuff = Text(" play.")
# newstring = (anotherObject + theOtherstuff)
# print(newstring)
# otherObject = Text()
# lastObject = Text()
# otherObject += lastObject
# print(otherObject)
# aWord = Text("Word")
# aWord += Text(" Play")
# print(aWord[:])
