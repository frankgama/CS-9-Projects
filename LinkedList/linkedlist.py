class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    #constructor which takes in one listNode, and defaults to None
    #has two memebr variable, a reference to the head node and the count
    def __init__(self, headNode: ListNode = None):
        self.headNode = headNode
        self.numberof = 0
    
    def add(self, value):
        #call the head to help traverse
        currentNode = self.headNode

        #create a new node to add to the lise
        newNode = ListNode(value)

        #if list is empty, insert the new node at the beginning
        #adjust count
        if currentNode == None:
            self.headNode = newNode
            self.numberof +=1
            return
        #if the head node value is greater than the value to insert
        #insert the new node at the head and adjust list and count
        if currentNode.value > value:
            newNode.next = currentNode
            self.headNode = newNode
            self.numberof +=1
            return

        #traverse list to find correct index of new node
        while currentNode.value < value:

            #adding to the tail, make new node the tail, and adjust count
            if currentNode.next == None:
                currentNode.next = newNode
                self.numberof +=1
                return

            #if adding anywhere in between head and tail, adjust list
            #adjust references and insert new node, andjust count
            if currentNode.next.value > value:
                nextNode = currentNode.next
                currentNode.next = newNode  
                newNode.next = nextNode 
                self.numberof +=1
                return
            #traversal and update of current node to the next one in the list
            currentNode = currentNode.next

        if currentNode.value == value:
            nextNode = currentNode.next
            currentNode.next = newNode  
            newNode.next = nextNode
            return

    def count(self):
        return self.numberof

    def get(self, index):
        
        if self.headNode == None:
            raise IndexError('Index out of range.')
        currentIndex = 0
        length_of_list = self.count()
        currentNode = self.headNode

        if index > (length_of_list - 1):
            raise IndexError('Index out of range.')

        if index < 0:
            index += length_of_list

        if index < 0:
            raise IndexError('Index out of range.')               
        if index == 0:
            if currentNode == None:
                raise IndexError('Index out of range.')
            return currentNode.value
        #if currentNode is None:
            #   raise IndexError(error)

        while currentNode != None:
            if index == currentIndex:
                #print(currentNode.value)
                return currentNode.value
            currentNode = currentNode.next
            currentIndex += 1
        if currentNode == None:
            raise IndexError('Index out of range.')
        raise IndexError('Index out of range.')
            

    def head(self):

        if self.headNode == None:
            return None
        return self.headNode

    def print(self, reverse: bool = False):
        
        currentNode = self.headNode
        printedList = []
    
        if currentNode == None:
            print(printedList)
            return
            
        
        while currentNode.next != None:
            printedList.append(str(currentNode.value))
            currentNode = currentNode.next
        printedList.append(str(currentNode.value))
        
        if reverse == True:
            reverseList = []
            currentInd = -1
            numItems = self.count() * -1
            while currentInd != numItems:
                reverseList.append(str(printedList[currentInd]))
                currentInd -= 1
            reverseList.append(str(printedList[currentInd]))
            print(f"[{', '.join(reverseList)}]")
            return

        print(f"[{', '.join(printedList)}]")

    def remove(self, index):
        #see if node if valid and find length of list
        currentNode = self.headNode
        if currentNode == None:
            raise IndexError('Index out of range.')
        length_of_list = self.count()
        
        #convert negative index to positive
        if index < 0:
            index += length_of_list

        if index < 0 or index > length_of_list - 1:
            raise IndexError('Index out of range.')

        #remove the head and only object in list
        #adjust count
        if index == 0 and length_of_list == 1: 
            nodeDeleted = self.headNode.value
            self.headNode = None
            self.numberof -= 1
            return nodeDeleted

        #remove head adjust count
        if index == 0: 
            nodeDeleted = currentNode.value
            self.headNode = currentNode.next
            self.numberof -= 1
            return nodeDeleted
        
        nodeToDelete = self.get(index)

        #traverse list until you find the correct node
        #use two variables to keep track of current and previous nodes
        prevNode = currentNode
        while currentNode.value != nodeToDelete:
            prevNode = currentNode
            currentNode = currentNode.next

        #remove the node and adjust the new list references to point to correct ones
        if currentNode.value == nodeToDelete:
                prevNode.next = currentNode.next
                currentNode = None
                self.numberof -= 1
                return nodeToDelete

    def remove_all(self, value):
        times_erased = 0
        if self.headNode == None:
            return times_erased

        currentNode = self.headNode
        prevNode = None
        

        while currentNode != None: 
            if currentNode.value == value:
                if prevNode is None:
                    self.headNode = currentNode.next
                else:
                    prevNode.next = currentNode.next
                
                times_erased +=1
                self.numberof -=1
                currentNode = currentNode.next
                #self.print()
            else:
                prevNode = currentNode
                currentNode = currentNode.next

        return times_erased

# newList = LinkedList()
# for i in range(10):
#     newList.add('mine')
# newList.print()
# print(newList.remove_all('mine'))

# secondList = LinkedList()
# for i in range(10):
#     secondList.add(i+1)
# secondList.print()

# newList.print()
# print(newList.get(12))
# print(newList.get(1))
# print(newList.get(0))
# print(newList.remove(0))
# newList.print()
# print(newList.remove(-1))
# newList.print()
# print(newList.remove(1))
# newList.print()
# newList.add(1.5)
# print(newList.get(-11))
# print(newList.get(12))
# print(newList.count())
# newList.print()
# newList.print(True)
# newList.print()
# print(newList.remove(1))
# newList.print()
# print(newList.remove(1))
# newList.print()
# print(newList.remove(0))
# newList.print()
# print(newList.remove(0))
# newList.print()
# newList.add(1.5)
# newList.print()
# newList.add(1.5)
# newList.print()
# newList.add(1.5)
# print(newList.remove(-1))
# newList.print()


# listOfrandoms = ["Frank", "Honey", "Emily", "Tits"]
# sortedList = LinkedList()
# for num in listOfrandoms:
#     sortedList.add(num)
# sortedList.print()
# sortedList.get(2)
# sortedList.get(-2)
# sortedList.get(-5)
# sortedList.get(0)
# sortedList.print(True)

# newList2 = LinkedList()
# newList2.print()