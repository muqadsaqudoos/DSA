class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def insert_at_tail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            return

        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        
    def insert_before(self,data,key):
        
        if self.head is None:
            return
        if self.head.data == key:
            newNode = Node(data)
            newNode.next = self.head
            newNode.prev = self.head.prev
            self.head.prev = newNode
            self.head = newNode
            return
        temp = self.head
        while temp is not None:
            if temp.data == key:
                newNode = Node(data)
                newNode.next = temp
                newNode.prev = temp.prev
                temp.prev.next = newNode
                temp.prev = newNode
                return
            temp = temp.next

        

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end= " ")
            temp = temp.next

        print()

def main():
    root = DoublyLinkedList()
    root.insert_at_tail(5)
    root.insert_at_tail(10)
    root.insert_at_tail(15)
    root.insert_at_tail(20)
    
    root.display()
    root.insert_before(2,5)
    root.display()

main()
        