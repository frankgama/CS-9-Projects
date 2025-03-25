import sys
import re
import math


class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self, root = None):
        self.root = root
        self.global_count = 0
        
    def insert(self, theItem):
        def recursiveNodeInsert(treenode, theItem):    
            if treenode is None:
                self.global_count += 1
                return TreeNode(theItem)

            if (treenode.value > theItem):
                treenode.leftChild = recursiveNodeInsert(treenode.leftChild, theItem)
            elif (treenode.value < theItem):
                treenode.rightChild = recursiveNodeInsert(treenode.rightChild, theItem)
            return treenode
        globalstart = self.global_count
        self.root = recursiveNodeInsert(self.root, theItem)
        globalend = self.global_count   
        if globalstart < globalend:
            return 1
        else:
            return 0

    def remove(self, theItem):
        def recursiveremove(treenode, theItem):
            if treenode is None:
                return None

            if treenode.value > theItem:
                treenode.leftChild = recursiveremove(treenode.leftChild, theItem)
            elif treenode.value < theItem:
                treenode.rightChild = recursiveremove(treenode.rightChild, theItem)
            else:
                if treenode.leftChild is None and treenode.rightChild is None:
                    self.global_count -= 1
                    return None
                if (treenode.leftChild) and treenode.rightChild is None:
                    self.global_count -= 1
                    return treenode.leftChild
                if (treenode.rightChild) and treenode.leftChild is None:
                    self.global_count -= 1
                    return treenode.rightChild

                if treenode.leftChild and treenode.rightChild:
                    findMinNode = treenode.leftChild
                    while findMinNode.rightChild is not None:
                        findMinNode = findMinNode.rightChild
                    treenode.value = findMinNode.value
                    treenode.leftChild = recursiveremove(treenode.leftChild, findMinNode.value)

            return treenode

        startingcount = self.global_count
        self.root = recursiveremove(self.root, theItem)
        return 1 if self.global_count < startingcount else 0

    def __len__(self):
        return self.global_count

    def clear(self):
        count = self.global_count
        self.root = None
        self.global_count = 0
        return count

    def __contains__(self, theItem):
        return self._search(self.root, theItem)

    def _search(self, treenode, theItem):
        if treenode is None:
            return False
        if treenode.value is None:
            return False
        if treenode.value == theItem:
            return True
        elif treenode.value > theItem:
            return self._search(treenode.leftChild, theItem)
        else:
            return self._search(treenode.rightChild, theItem)

    def __getitem__(self, index):
        if isinstance(index, slice):
            treeString = str(self)
            treeOfWords = treeString.replace("(","").replace(")", "").replace("-","")
            listOfWords = treeOfWords.split()
            return listOfWords[index]
        if isinstance(index, int):
            treeString = str(self)
            treeOfWords = treeString.replace("(","").replace(")", "").replace("-","")
            listOfWords = treeOfWords.split()
            return listOfWords[index]
        else:
            raise TypeError("Not a valid index")
                

    def __str__(self):
        def recursiveStr(treenode):
            if treenode is None:
                return "-"
            if treenode.value is None:
                return "-"
            parentNode = treenode.value
            leftChild = recursiveStr(treenode.leftChild)
            rightChild = recursiveStr(treenode.rightChild)
            if leftChild == "-" and rightChild == "-":
                return str(parentNode)
            return "("+str(leftChild)+" "+str(parentNode)+" "+str(rightChild)+")"
        stringofTree = recursiveStr(self.root)
        return stringofTree

def treeExp(treeexpression):
    if isinstance(treeexpression, str):
        treeexpression = treeexpression.strip()
        position = -1
        for char in treeexpression[::-1]:
            if char == ")":
                position += len(treeexpression)
                return treeexpression[:position+1]
            else:
                position -= 1
    return None

def isValidTreeX(treeX):
    stack = []
    if isinstance(treeX, str):
        treeEx = treeX
        count = 0

        for char in treeEx:
            if char == "(":
                stack.append("(")
    
            elif char == ")":
                if not stack:
                    return False
                if count in {0,1,3,5}: 
                    count = 1
                    stack.pop()
    
                else:
                    return False
            elif char.isalpha() or char == "*":
                count +=1
    
            else:
                continue
    
    if not stack and count == 1:
        return True
    return False

def treeList(validTreeExp):
    if isinstance(validTreeExp, str):
        cleanUp = validTreeExp.replace()
def treeList(treeX):
    if isinstance(treeX, str):
        treeList = treeExp(treeX)
        treeList = treeList.replace("(","")
        treeList = treeList.replace(")","")
        treeList = treeList.split()
    return treeList

def treeParse(treeXprss):

    def recursiveTreeParse(treeList):
        if not treeList:
            return None
        log_base_2 = int(math.ceil(math.log(len(treeList), 2)))
        middle_index = (int((2**log_base_2) / 2)) - 1
        root = TreeNode(treeList[middle_index])
        root.leftChild = recursiveTreeParse(treeList[:middle_index])
        root.rightChild = recursiveTreeParse(treeList[middle_index+1:])
        return root
    return Tree(recursiveTreeParse(treeXprss))

treeExpression = treeList('((((H S V) I (F U -)) E ((L R -) A (P W J))) * (((B D X) N (C K Y)) T ((Z G Q) M )))'
)
log_base_2 = int(math.ceil(math.log(len(treeExpression), 2)))
print(treeExpression)
print(len(treeExpression))
print(log_base_2)

middle_index = (int((2**log_base_2)/2))-1
print(middle_index)
print(treeExpression[middle_index])