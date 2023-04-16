
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"{self.value}"


'''
It uses two pointers slow and fast
slow incremented 1 step 
fast incremented 2 steps in each iteration
'''

# By using recursion


def is_circular_list(slow, fast):
    if slow and fast:
        if (slow == fast):
            return True
        if fast.next:
            return is_circular_list(slow.next, fast.next.next)

    return False


def is_circular_list2(node):
    slow = node
    fast = node.next

    while fast and slow:
        if fast == slow:
            return True
        if fast.next:
            slow = slow.next  # incremented 1 step
            fast = fast.next.next  # incremented 2 steps

    return False


# Test data
joinNode = Node(4)
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = joinNode
root.next.next.next.next = Node(5, Node(6, Node(7, joinNode)))

print(is_circular_list(root, root.next))
print(is_circular_list2(root))
