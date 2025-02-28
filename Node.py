

class Node: 
    
    def __init__(self, data  , next   ) -> None:
        self.data = data 
        self.next = next 
        

n1 = Node(10,None)
n2 = Node(20,None) 
n3 = Node(30,None)

n1.next = n2 
n2.next = n3 

print('hello')