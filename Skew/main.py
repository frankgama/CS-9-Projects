class SkewHeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left.value > right.value:
        left, right = right, left
    left.right = merge(left.right, right)
    left.left, left.right = left.right, left.left
    return left


class SkewHeap:
    def __init__(self):
        self.root = None
        self.count = 0

    def push(self, value):
        new_node = SkewHeapNode(value)
        self.root = merge(self.root, new_node)
        self.count += 1

    def pop(self):
        if not self.root:
            return "ERROR: Heap is empty."
        min_value = self.root.value
        self.root = merge(self.root.left, self.root.right)
        self.count -= 1
        return min_value

    def top(self):
        if not self.root:
            return "ERROR: Heap is empty."
        return self.root.value

    def size(self):
        return self.count

    def print_tree(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return "-"
        left = self.print_tree(node.left)
        right = self.print_tree(node.right)
        if left == "-" and right == "-":
            return f"{node.value}"
        return f"({left} {node.value} {right})"


def main():
    heap = SkewHeap()

    while True:
        try:
            command = input().strip()
            if not command:
                continue

            if command.startswith("push"):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("ERROR: No argument.")
                else:
                    heap.push(parts[1])

            elif command == "pop":
                print(heap.pop())

            elif command == "top":
                print(heap.top())

            elif command == "count":
                print(heap.size())

            elif command == "print":
                print(heap.print_tree())

            elif command == "exit":
                break

            else:
                print("ERROR: Unknown command.")
        except EOFError:
            break


if __name__ == "__main__":
    main()