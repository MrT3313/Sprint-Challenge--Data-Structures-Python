from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        print(f'Capacity: {self.capacity}')
        print(f'Storage: {self.storage.__len__()}')

        # FULL STORAGE
        if self.storage.__len__() >= self.capacity:
            print(item)
            # Remove Head => ALWAYS the oldest since we are ALWAYS adding to tail
            self.storage.delete(self.storage.head)
            # Add net item to tail
            self.storage.add_to_tail(item)

        # HUNGRY STORAGE => add to tail
        else:
            print(item)
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        current = self.storage.head
        # next_node = current.next

        for _ in range(self.storage.__len__()):
            # print('current next', current.next)
            if current is not None:
                # print('current -->', current)
                list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

newRingBuffer = RingBuffer(5)
# # [1, 3, 4, 7, 9]
# print(newRingBuffer.capacity)
newRingBuffer.append(1)
newRingBuffer.append(3)
newRingBuffer.append(4)
newRingBuffer.append(7)
newRingBuffer.append(9)
# print(f'storage.length: {newRingBuffer.storage.__len__()}')
# print(newRingBuffer.storage.head.value, newRingBuffer.storage.tail.value)
print(newRingBuffer.get())

newRingBuffer.append(10)
# print(f'storage.length: {newRingBuffer.storage.__len__()}')
# print(newRingBuffer.storage.head.value, newRingBuffer.storage.tail.value)
print(newRingBuffer.get())

newRingBuffer.append(13)
# print(f'storage.length: {newRingBuffer.storage.__len__()}')
# print(newRingBuffer.storage.head.value, newRingBuffer.storage.tail.value)
print(newRingBuffer.get())

newRingBuffer.append(99)
# print(f'storage.length: {newRingBuffer.storage.__len__()}')
# print(newRingBuffer.storage.head.value, newRingBuffer.storage.tail.value)
print(newRingBuffer.get())




# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
