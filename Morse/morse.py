import sys
import re
import math

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def build_morse_dict(self, node, path="", morse_dict=None):
        if morse_dict is None:
            morse_dict = {}
        
        if node is None:
            return morse_dict
        
        if node.value != "*":
            morse_dict[node.value] = path
        
        self.build_morse_dict(node.leftChild, path + ".", morse_dict)
        self.build_morse_dict(node.rightChild, path + "-", morse_dict)
        
        return morse_dict

    def decode_morse(self, node, morse_code):
        current_node = node
        decoded_message = []
        
        for char in morse_code.split():
            if char == "":
                decoded_message.append(" ")
                continue
            
            for signal in char:
                if signal == ".":
                    if current_node.leftChild:
                        current_node = current_node.leftChild
                elif signal == "-":
                    if current_node.rightChild:
                        current_node = current_node.rightChild
                else:
                    decoded_message.append("?")
                    break
            
            decoded_message.append(current_node.value if current_node.value != "*" else "?")
            current_node = node  # Reset to root for the next character
        
        return "".join(decoded_message)

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
    if not treeX:
        return False

    stack = []
    count = 0
    for char in treeX:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            stack.pop()
            if count not in {0, 1, 3, 5}:
                return False
        elif char.isalpha() or char == "*":
            count += 1
        else:
            continue

    return not stack and count == 1

def treeList(treeX):
    if isinstance(treeX, str):
        treeList = treeExp(treeX)
        treeList = treeList.replace("(", "")
        treeList = treeList.replace(")", "")
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
    if not treeXprss or not isinstance(treeXprss, list):
        raise Exception("ERROR: Invalid tree file.")
    return Tree(recursiveTreeParse(treeXprss))

def encoder(message, morse_dict=None):
    # If no tree-based dictionary is provided, use the default dictionary
    if morse_dict is None:
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
        }

    message = ' '.join(message.split())
    words = message.upper()
    result = []

    for letter in words:
        if letter in morse_dict:
            result.append(morse_dict[letter])
        elif letter == " ":
            result.append("  ")
        else:
            continue

    output = ' '.join(result)
    output = re.sub(r' {2,}', "  ", output)
    print(output.strip())

def decoder(message, tree=None):
    if tree is None:
        # Default dictionary for decoding
        myDict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z'
        }

        redux = re.sub(r'\t', " ", str(message))
        redux = re.sub(r' {3,}', '  ', redux)
        redux = re.sub(r'\t{2,}', "  ", redux)
        redux = re.sub(r'\t', " ", redux)
        splitWords = redux.split("  ")
        splitwords = "  ?  ".join(splitWords)
        splitWords = splitwords.split("  ")
        lengthplusspace = len(splitWords) + (len(splitWords) - 1)
        for i in range(lengthplusspace):
            if (i % 2 == 0):
                continue
            else:
                splitWords.insert(i, " ")
        characters = []
        for word in splitWords:
            if word == " ":
                characters.append(" ")
            else:
                currList = word.split()
                characters += currList
        position = 0
        for letter in characters:
            if letter == " " or letter == "?":
                characters[position] = " "
            elif letter in myDict:
                characters[position] = myDict[letter]
            else:
                characters[position] = "?"
            position += 1
        decoded_message = ''.join(characters)
        decoded_message = re.sub(r' {2,}', " ", decoded_message)
        print(decoded_message)
    else:
        # Decode using the tree
        lines = message.split("  ")  # Split words by double spaces
        decoded = []
        for word in lines:
            decoded.append(tree.decode_morse(tree.root, word.strip()))
        print(" ".join(decoded).strip())

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == '-d':
            for line in sys.stdin:
                decoder(line.strip())
        elif sys.argv[1] == '-e':
            for line in sys.stdin:
                encoder(line.strip())
        else:
            print("USAGE: morse.py [-e or -d] [tree-file]")
            return
    elif len(sys.argv) == 3:
        textfile = sys.argv[2]
        try:
            count = 0
            with open(f"{textfile}") as treefile:
                lines = treefile.readlines()
                count +=1
            if count !=1:
                print("ERROR: Invalid tree file.")
                return
            
            treeNotation = lines[0].strip()
            treex = treeExp(treeNotation)
            if not isValidTreeX(treex):
                print("ERROR: Invalid tree file.")
                return
            
            treex = treeList(treex)
            tree = treeParse(treex)

            morse_dict = tree.build_morse_dict(tree.root)

            if sys.argv[1] == '-d':
                for line in sys.stdin:
                    decoder(line.strip(), tree)
            elif sys.argv[1] == '-e':
                for line in sys.stdin:
                    encoder(line.strip(), morse_dict)
            else:
                print("USAGE: morse.py [-e or -d] [tree-file]")
                return
        except FileNotFoundError:
            print("ERROR: Invalid tree file.")
        except Exception as e:
            print("ERROR: Invalid tree file.")

if __name__ == "__main__":
    main()