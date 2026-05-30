#Membuat stack dengan menggunakan linked list
#1.kelas node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#2 kelas stack
class Stack:
    def __init__(self):
        self.head = None
#METHOD UNTUK NAMBAH STACK    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#method untuk
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")
#METHOD UNTUK MENGHAPUS STACK
    def pop(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data
#METHOD UNTUK MENGECEK APAKAH STACK KOSONG
    def is_empty(self):
        return self.head is None
#METHOD UNTUK MELIHAT STACK TERATAS
    def peek(self):
        if not self.head:
            return None
        return self.head.data
    
#PENGGUNAAN STACK
myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.display() 
myStack.pop()      
myStack.display()  
print(myStack.is_empty())  
print(myStack.peek())