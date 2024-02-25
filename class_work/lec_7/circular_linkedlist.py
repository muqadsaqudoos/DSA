class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        if self.head is None:
            self.head = node(val)
            self.head.next = self.head 
            return
        newNode = node(val)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head
        self.head = newNode

    def dispaly(self):
        if self.head is None:
            return 
        temp = self.head 
        print(temp.val, end= " ")
        temp = temp.next
        while temp != self.head:
            print(temp.val, end=" ")
            temp = temp.next

def main():
    root = CircularLinkedList()
    root.insert_at_head(20)
    root.insert_at_head(10)
    root.insert_at_head(5)
    root.dispaly()
main()