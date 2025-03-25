class Text:
    def __init__(self, chars = None):

        if char is None:
            self.headNode = None
            self.tailNode = None
            self.sizeof = 0

        elif isinstance(chars, str):
            for index in range(len(char)):
                prevNode = None
                if index == 0:
                    self.headNode = Node(chars[index])
                    self.tailnode = self.headNode
                    prevNode = self.headNode
                    self.sizeof += 1

                prevNode.next = Node(chars[index])
                self.tailNode = prevNode.next
                self.tailNode.prev = prevNode
                prevNode = prevNode.next
                self.sizeof += 1

        elif isinstance(chars, Text):
            self.headNode = None
            self.tailNode = None
            self.sizeof = 0

            currNode = chars.headNode
            prevNode = None
            while currNode:
                if self.headNode == None:
                    self.headNode = Node(currNode.char,)
                    self.tailNode = self.headNode
                    prevNode = self.headNode
                    self.sizeof += 1
                    currNode = currNode.nexthm

                self.tailNode = Node(currNode.char)
                prevNode.next = self.tailNode
                self.tailNode.prev = prevNode
                prevNode = self.tailNode
                self.sizeof+=1
                currNode= currNode.next

    def append(self, charc):
        prevtail = self.tailNode
        self.tailNode = Node(charc)
        prevtail.next = self.tailNode
        self.tailNode.prev = prevtail

    def clear(self):
        self.headNode = None
        self.tailNode = None
        self.sizeof = 0

    def copy(self):
        currNode = self.headNode
        text = []
        while currNode:
            text.append(currNode.char)
            currNode = currNode.next
        textstring = ''.join(text)
        return textstring

    def extend(self, extender = None):
        if isinstance(extender, str):
            newText = Text(extender)
            self.tailNode.next = newText.headNode
            newText.headNode.prev = self.tailNode
            self.tailNode = newText.tailNode

    def insert(self, index, character):
        listlength = self.sizeof
        maxoflist = listlength + 1
        if index > maxoflist:
            return

        position = 0
        currNode = self.headNode
        prevNode = None
        if index == 0:
            newNode = Node(character)
            newNode.next = self.headNode
            self.headNode.prev = newNode
            self.headNode = newNode
            self.sizeof += 1

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

        if position == listlength + 1:
            newNode = Node(character)
            self.tailNode.next = newNode
            newNode.prev = self.tailNode
            self.sizeof += 1

    def pop(self, index = None):
        lengthlist = self.sizeof

        if index == None:
            if lengthlist == 1:
                currNode = self.headNode
                self.headNode = None
                self.tailNode = None
                self.sizeof -= 1
                return currNode.char

            noderemoved = self.tailNode
            prevNode = noderemoved.prev
            prevNode.next = None
            self.tailNode = prevNode
            self.sizeof -= 1
            return noderemoved.char

        else:
            currNode = self.headNode
            position = 0
            prevNode = None
            if lengthlist == 1 and index == 0:
                currNode = self.headNode
                self.headNode = None
                self.tailNode = None
                self.sizeof -= 1
                return currNode.char
            if index == lengthlist - 1:
                noderemoved = self.tailNode
                prevNode = noderemoved.prev
                prevNode.next = None
                self.tailNode = prevNode
                self.sizeof -= 1
                return noderemoved.char

            while position != index:
                prevNode = currNode
                currNode = currNode.next
                position += 1

            prevNode.next = currNode.next
            currNode.next.prev = prevNode
            self.sizeof -= 1
            return currNode.char


    def __len__(self):
        return self.sizeof

    def __str__(self):
        thetext = self.copy()
        return thetext

    def __getitem__(self, index):
        lengthlist = self.sizeof

        if index > lengthlist-1:
            return
        currNode = self.headNode
        position = 0

        while position! == index:
            currNode = currNode.next
        iteminnode = currNode.char
        return iteminnode







    def head(self):
        return self.headNode

    def tail(self):
        return self.tailNode


class Node:
    def __init__(self,char, next = None, prev = None):
        self.next = next
        self.prev = prev
        self.char = char

