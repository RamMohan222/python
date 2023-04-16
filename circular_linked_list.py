class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'{self.value}'

# solution 1
def is_circular(root):
    slow = root
    fast = root.next
    while slow and fast:
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next

    return False

# solution 2
def is_circular2(slow, fast):
    if slow == None or fast == None:
        return False
    
    if slow == fast:
        return True
        
    if fast.next:
        return is_circular2(slow.next, fast.next.next)

    return None

# solution 3
def is_circular3(root, list=[]):
    if root == None:
        return None
    
    if root in list:
        return root
    
    list.append(root)
    return is_circular3(root.next)

        
node3 = Node(3)
node3.next = Node(4, Node(5, Node(6, node3)))
root = Node(1, Node(2, node3))

print(is_circular(root))
print(is_circular2(root, root.next))
print(is_circular3(root))
