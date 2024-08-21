#더미 이중 연결 리스트

class Node:
    def __init__(self, data=None):
        self.__data=data
        self.__prev=None
        self.__next=None

    #소멸자. 삭제연산 시 확인하려고 작성

    def __del__(self):
        print("data of {} is deleted" .format(self.data))

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data=data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        self.__prev=p

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self,n):
        self.__next

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        # 리스트 맨 앞과 끝에 더미노드 두고 실제 데이터 저장 x

        self.head.next=self.tail
        self.tail.prev=self.head
        #head와 tail연결하기

        self.d_size=0
        #데이터 개수를 저장할 변수 

    def empty(self):
        if self.d_size==0:
            return True
        
        else:
            return False
        
    def size(self):
        return self.d_size
    
    def add_first(self, data):
        new_node=Node(data)

        new_node.next=self.head.next #더미 노드의 다음 노드인 첫번째 데이터를 가리키도록 함
        new_node.prev=self.head #더미노드를 가리키도록 함

        self.head.next.prev=new_node #첫번째 데이터 노드가 새로운 노드를 가리키도록 함
        self.head.next=new_node #더미노드의 next는 새로운 노드를 가리켜 새로운 노드 삽입

        self.d_size += 1 #데이터 개수 늘리기

    def add_last(self,data):
        new_node=Node(data)

        new_node.prev=self.tail.prev
        new_node.next=self.tail

        self.tail.prev.next=new_node
        self.tail.prev=new_node

        self.d_size += 1

    def insert_after(self, data, node):
        new_node=Node(data)

        new_node.next=node.next
        new_node.prev=node

        node.next.prev=new_node
        node.next=new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node=Node(data)

        new_node.prev=node.prev
        new_node.next=node

        node.prev.next=new_node
        node.prev=new_node

    #요소 탐색 연산 구현

    def search_forward(self, target):
        cur=self.head.next #데이터를 순회할 cur변수; 첫번째 노드부터 시작

        #리스트의 첫번째 데이터부터 선형적으로 순회히며 탐색하는 연산

        while cur is not self.tail:
            if cur.data == target:
                return cur
            
            cur= cur.next

        return None
    
    def search_backward(self, target):
        cur=self.tail.prev

        #리스트의 마지막 데이터부터 선형적으로 순회하며 탐색하는 연산

        while cur is not self.head:
            if cur.data == target:
                return cur
            
            cur= cur.prev

        return None
    
    def delete_first(self):
        #삭제 연산
        if self.empty():
            return
        
        self.head.next=self.head.next.next
        self.head.next.prev=self.head

        self.d_size -= 1


    def delete_last(self):
        if self.empty():
            return
        
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail

        self.d_size -= 1


    def delete_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

        self.d_size -= 1

    




    




