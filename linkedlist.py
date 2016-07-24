class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if(self.head is None):
            self.head = node
        else:
            ptr = self.head
            while(ptr.next and ptr.data <= node.data):
                ptr = ptr.next
            ptr.next = node

    def remove(self, value):
        ptr = self.head
        prev = None
        while(ptr and ptr.data != value):
            prev = ptr
            ptr = ptr.next
        if(not ptr):
            print('Not found')
        else:
            prev.next = ptr.next
            

    def printLinkedList(self):
        arr = []
        ptr = self.head
        while(ptr):
            arr.append(ptr.data)
            ptr = ptr.next
        print(arr)

    def length(self):
        count = 0
        ptr = self.head
        while(ptr):
            count += 1
            ptr = ptr.next
        return count

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


linkedlist = LinkedList()
for item in range(10):
    node = LinkedListNode(item)
    linkedlist.insert(node)
linkedlist.printLinkedList()
linkedlist.remove(4)
linkedlist.printLinkedList()
print(linkedlist.length())

