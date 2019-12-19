"""Write code to remove repeated element from an unsorted linked list"""


def remove_item(l):
    node = l.head
    d = {}
    prev = node
    while node.next is not None or node is l.tail:  # Iterate as long as there is a next item
        if d.get(node.val):
            prev.next = node.next
        else:
            d[node.val] = True
            prev = node
        node = node.next

def remove_item(head):
    # if we are not allowed to use extra datastructure. Then iterate over two pointers i and j point
    m = head
    while m.next is not None:
        y = m
        while y.next is not None:
            if m.val == y.next.val:
                y.next = y.next.next
            else:
                y = y.next
        m = m.next


if __name__ == "__main__":
    class Node(object):
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    class LinkedList(object):
        def __init__(self):
            self.head = None
            self.tail = None

        def add(self, node):
            if self.head is None:
                self.head = node
            else:
                y = self.head
                while y.next is not None:
                    y = y.next
                y.next = node
                self.tail = node

        def __repr__(self):
            return 'Node(%s, %s)' % (self.head.val, self.head.next)

    l = LinkedList()
    l.add(Node(1))
    l.add(Node(2))
    l.add(Node(3))
    l.add(Node(1))
    l.add(Node(5))
    l.add(Node(6))
    l.add(Node(1))
    #print(l)
    remove_item(l.head)
    print(l)
