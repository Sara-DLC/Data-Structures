from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('queue_and_stack/doubly_linked_list.py')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size is 0:
            None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
