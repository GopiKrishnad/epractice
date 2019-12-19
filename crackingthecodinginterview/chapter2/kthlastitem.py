"""
Implement an algorithm to find the kth to last element of a singly linked list
"""


def kthlast_item(linkedm, k):
    head = linkedm
    if head is None or head.next is None:
        return 0
    index = kthlast_item(head.next, k) + 1
    if index == k:
        print('==', head.val)
    return index


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
    l.add(Node(4))
    l.add(Node(5))
    l.add(Node(6))
    l.add(Node(1))
    #print(l)
    print(kthlast_item(l.head, 2))
