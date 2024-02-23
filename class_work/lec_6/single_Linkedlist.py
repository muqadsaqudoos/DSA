class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    #insertion
    def insert_at_head(self,val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode 

    def insert_at_tail(self,val):
        newNode = node(val)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode


    def insert_before(self,val,key):
        
        if self.head is None:
            return
        if self.head.val == key:
            newNode = node(val)
            newNode.next = self.head
            self.head = newNode
            return
        temp =  self.head
        temp2 = self.head
        while temp is not None:
            if key == temp.val :
                newNode = node(val)
                newNode.next = temp
                temp2.next = newNode
                return
            temp2 = temp
            temp = temp.next

    def insert_after(self,val,key):
        if self.head is None:
            return 
        temp1 = self.head
        temp2 = self.head.next
        while temp2 is not None:
            if temp1.val == key and temp2 is None:
                del temp2
                temp1.next = None
                return 
            elif temp1.val == key:
                temp1.next = temp2.next
                del temp2




    #Remove
    def remove_at_head(self):
        if self.head is None:
            return
        temp = self.head
        self.head = temp.next
        del temp

    def remove_at_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            del self.head
        temp = self.head 
        temp2 = self.head
        while temp.next is not None:
            temp2 = temp
            temp = temp.next 
        del temp
        temp2.next = None

    def remove_before(self,key):
        if self.head is None or self.head.val == key:
            return 
        elif self.head.next.val == key:
            temp = self.head
            self.head = temp.next
            del temp
            return

        else:
            temp1 = self.head
            temp2 = self.head.next
            while temp2.next is not None:
                if temp2.next.val == key:
                    temp1.next = temp2.next
                    del temp2
                    return 
                
                temp1 = temp1.next
                temp2 = temp2.next

            
        
    def remove_after(self,key):
        if self.head is None and self.head.val == key:
            return
        temp1 = self.head
        temp2 = self.head.next
        while temp2 is not None:
            if temp1.val == key:
                temp1.next = temp2.next
                del temp2
                return 
            temp1 = temp1.next
            temp2 = temp2.next 
        if temp1.val == key :
            del temp2
            temp1.next = None
 
        
    #transversing
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val,end = " ")
            temp = temp.next

    def search(self,key):
        
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            if key == temp.val:
                return True
            temp = temp.next
        return False
    
    def update(self,key,val):
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            if temp.val == key:
                temp.val = val
                return
            temp = temp.next

    

    def count(self):
        if self.head is None:
            return 0
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    def get_middle(self):
        if self.head is None:
            return None
        temp1 = self.head
        temp2 = self.head
        while temp2 is not None and temp2.next is not None:
            temp1 = temp1.next
            temp2 = temp2.next.next

        return temp1.val

def main():
    root = linkedList()
    """
    root.insert_at_head(5)
    root.insert_at_head(10)
    root.insert_at_head(15)
    root.insert_at_head(20)
    root.insert_at_head(25)
    """
    root.insert_at_tail(5)    
    root.insert_at_tail(10)    
    root.insert_at_tail(20)    
    root.insert_at_tail(23)    
    root.insert_at_tail(25)    
    #root.insert_after(17,5)
    root.display()
    #print(root.count())
    print()
    print(root.get_middle())
    """
    a = root.search(2)
    if a:
        print("\nElelement in linked List")
    else:
        print("\nElelement not in linked List")

    root.update(5,2)
    root.display()
    """

 
main()

