class Node:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_element_into_head(self,val):
        node = Node(val,self.head)
        self.head = node

    def insert_element_into_tail(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        else:
            itr = self.head 
            while itr.next is not None:
                itr = itr.next

            itr.next = node

    def print(self):
        itr = self.head
        lstr = ""
        while itr:
            lstr += f"{itr.val} "
            itr = itr.next

        print(lstr) 
    def get_lenght(self):
        itr = self.head 
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count
    def index_at(self,index,data):
        if index < 0 and index > self.get_lenght():
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_element_into_head(data)
            return 
        else:
            count = 0
            itr = self.head 
            while itr:
                if count == index-1:
                    node = Node(data,itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1


    def remove_at(self,index):
        if index < 0 and index > self.get_lenght():
            raise Exception("invalid syntax")
        elif index == 0 :
            self.head = self.head.next
            return 
        
        else:
            itr = self.head 
            count = 0
            while itr :
                if count == index -1:
                    itr.next = itr.next.next

                itr = itr.next
                count+= 1

            

root = Linked_list()
"""
root.insert_element_into_head(5)
root.insert_element_into_head(10)
root.insert_element_into_head(15)
"""
root.insert_element_into_tail(599)
root.insert_element_into_tail(999)
root.insert_element_into_tail(799)
root.index_at(1,677)
root.remove_at(2)
root.print()
print(root.get_lenght())



        