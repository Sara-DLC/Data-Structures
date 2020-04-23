import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('queue_and_stack/doubly_linked_list.py')

'''
: enqueue should add an item to the back of the queue.
: dequeue should remove and return an item from the front   of the queue.
: len returns the number of items in the queue.'''


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size is 0:
            None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
