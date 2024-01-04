class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class DNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = DNode(data=data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            return
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insertAtIndex(self, index: int, data):
        new_node = Node(data=data)
        current_node = self.head
        position = 0
        if index == position:
            self.insertAtBegin(data=data)
        else:
            while current_node and position < index - 1:
                current_node.next
                position += 1

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index out of range")

    def updateNode(self, data, index: int):
        position = 0
        current_node = self.head

        while current_node and position < index:
            current_node = current_node.next
            position += 1

        if current_node != None:
            current_node.data = data
        else:
            print("Index not pressent")

    def remove_first_node(self):
        self.head = self.head.next

    def delete(self, index: int):  # todo
        current_node = self.head
        position = 0
        while current_node and position < index - 1:
            current_node = current_node.next
            position += 1

        if current_node:
            current_node.next = current_node.next.next

    def getDataIndex(self, data):
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == data:
                return str(position) + "found"
            else:
                current_node = current_node.next
                position += 1
        return "not found"

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next  # Save the next node
            current_node.next = prev_node  # Reverse the pointer
            prev_node = current_node  # Move one step forward
            current_node = next_node  # Move one step forward

        self.head = prev_node  # The last node becomes the new head

    def merge(self, linked_list):
        self.tail.next = linked_list.head

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


l1 = LinkedList()
l1.append(20)
l1.append(2)
l1.append(29)
l1.insertAtBegin(data=90)
l1.updateNode("hello", 1)
# l1.insertAtIndex(40, 0)  # todo adjust bug here
l1.traverse()
l2 = LinkedList()
l2.append(20)
l2.append(2)
l2.append(29)
l2.insertAtBegin(data=90)
l2.updateNode("hello", 1)
l1.merge(l2)
print(".........................")
l1.traverse()
