class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
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


my_list =LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)
print(my_list.head.data)