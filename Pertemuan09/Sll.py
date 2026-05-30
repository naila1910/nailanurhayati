class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_list(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

    def delete_list(self, data):
        temp = self.head
        while temp: 
            if temp.data == data:
                if temp == self.head:
                    self.head = temp.next
                else:
                    temp.next = temp.next,next
                print("Data Berhasil Dhapus")
                break
            temp = temp.next
            print("Data Tidak Ditemukan")
    
    def search_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("Data Ditemukan")
                break
            temp = temp.next
            print("Data Tidak Ditemukan")

ll = LinkedList()
ll.add_list(30)
print("cetak LinkedList")
ll.display()
ll.add_list(20)
ll.add_list(10)
print("cetak LinkedList")
ll.display()
ll.delete_list(10)
print("cetak LinkedList")
ll.display()
ll.search_list(20)
ll.display()