class Dnode:
    def __init__(self,elem,prev=None,next=None):
        self.data=elem
        self.next=next #다음노드
        self.prev=prev #이전노드
    
    def append(self,node):
        if node is not None:
            node.next=self.next
            node.prev=self
            if node.next is not None:
                node.next.prev=node
            self.next=node

    def popNext(self):
        node=self.next
        if node is not None:
            self.next=node.next
            if self.next is not None:
                self.next.prev=self
            return node
        
class DblLinkedList:
    def __init__(self):
        self.head=None
    
    def display(self,msg='DblLinkedlist:'):
        print(msg,end='')
        ptr=self.head
        while ptr is not None:
            print(ptr.data,end='')
            ptr=ptr.print
        print('None')

    def insert(self,pos,e):
        node=Dnode(e)
        before=self.getnode(pos-1)
        if before==None:
            node.next=self.head
            if node.next is not None:
                node.next.prev=node
            self.head=node
        else: before.append(node)

    def delete(self,pos):
        before=self.getNode(pos-1)
        if before==None:
            before=self.head
            if self.head is not None:
                self.head=self.head.next
            if self.head is not None:
                self.head.prev=None
            return before
        else: before.popNext()

        