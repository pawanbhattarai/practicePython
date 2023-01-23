class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init_(self):
        self.head=None

    def printList(self):
            temp=self.head
            while(temp):
                print(temp.data)
                temp=temp.next

if __name__=='__main__':

    lists=LinkedList()

    lists.head=Node(4)
    second=Node(6)
    third=Node(7) 
    fourth=Node(8)
    fifth=Node(9)
    Second=Node(6)
    Third=Node(7) 
    Fourth=Node(8)
    Fifth=Node(9)
    lists.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=Second
    Second.next=Third
    Third.next=Fourth
    Fourth.next=Fifth

    lists.printList()
