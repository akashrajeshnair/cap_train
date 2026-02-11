class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_middle(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

def create_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def print_list(head):
    out = []
    cur = head
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    if out:
        print(" ".join(out))
    print()


n = int(input("Enter number of elements: "))
vals = list(map(int, input("Enter the elements: ").split()))
head = create_list(vals)
head = delete_middle(head)
print_list(head)

