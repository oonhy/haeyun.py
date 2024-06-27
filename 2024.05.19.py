class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

    def append(self,node):
        if node is not None:
            node.link=self.link
            self.link=node

    def popNext(self):
        next=self.link
        if next is not None:
            self.link=next.link
        return next
    
class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None
    
    def isFull(self):
        return False
    
    def getNode(self,pos):
        if pos<0: return None
        ptr=self.head
        for i in range(pos):
            if ptr==None:
                return None
            ptr=ptr.link
        return ptr
    
    def getEntry(self,pos):
        node=self.getNode(pos)
        if node==None: return None
        else: return node.data
    
    def insert(self,pos,e):
        node=Node(e,None)
        before=self.getNode(pos-1)
        if before==None:
            node.link=self.head
            self.head=node
        else: before.append(node)

    def delete(Self,pos):
        before=self.getNode(pos-1)
        if before==None:
            before=self.head
            if self.head is not None:
                self.head=self.head.link
            return before
        else: return before.popNext()

    def size(self):
        ptr=self.head
        count=0
        while ptr is not None:
            ptr=ptr.link
            count+=1
        return count
    
    def dispaly(self,msg='Linkedlist:'):
        print(msg,end='')
        ptr=self.head
        while ptr is not Node:
            print(ptr.data,end='->')
            ptr=ptr.link
        print('None')
