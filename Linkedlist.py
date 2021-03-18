from typing import Optional 

class ListNode(object):
    def __init__(self, data =0 , next =None):
        self.data = data
        self.head = None
        self.next = next
   


# class SingleLinkedList(object,Node):
#     self.Node=Node.value
#     self.head=Node.head
#     self.head=Node.next
    
#     def add_node(self):
        
#         return Node
#     def delete_node(self):
#         return Node
#     def print_list(self):
        
#         return print(Node)
#     def insertNthPlace(self,n):
#         return Node
#     def removeduplicate(self):
#         return Node
    
    
def search_List(self,L : ListNode, key:int)->ListNode:
        while L and L.data !=key:
            L=L.next
        return L
    
def insert_after(self,node:ListNode, new_node:ListNode)->None:
        new_node.next =node.next
        node.next=new_node
        
def delete_after(self,node:ListNode) ->None:
        node.next =node.next.next
    
def merge_two_sorted_lists(self,L1:Optional[ListNode], L2:Optional[ListNode])->Optional[ListNode]:
    dummy_head=tail =ListNode()
    while L1 and L2:
        if L1.data <L2.data:
            tail.next,L1=L1, L1.next
        else:
            tail.next,L2 =L2, L2.next
            tail =tail.next
        tail.next =L1 or L2
        return dummy_head.next
            
            