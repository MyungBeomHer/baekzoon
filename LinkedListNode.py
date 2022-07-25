class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_after(self,previous_node):
        data = previous_node.next.data

        if previous_node.next == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
        return data

    def insert_after(self,previos_node,data):
        new_node = Node(data)

        if previos_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else :
            new_node.next = previos_node.next
            previos_node.next = new_node

    def find_node_at(self,index):
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        return iterator

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
    def __str__(self):
        res_str = "["
        iterator = self.head

        while iterator is not None:
            res_str += f"{iterator.data}"
            if iterator != self.tail:
                res_str += ","
                
            iterator = iterator.next
        res_str += "]"
        return res_str

"""
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
"""
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)

print("---delete---")
node_2 = linked_list.find_node_at(2)
linked_list.delete_after(node_2)
print(linked_list)

