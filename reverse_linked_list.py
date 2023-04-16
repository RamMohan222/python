class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'{self.value}'
   
def display(root):
    print(root, end=",")
    if root.next:
        display(root.next)

def reverse(root):
    previousNode = None
    currentNode = root

    while currentNode:

        temp = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = temp

    return previousNode

root = Node(1, Node(2, Node(3,Node(4, Node(5, Node(6))))))

display(root)
start = reverse(root)
print()
display(start)
