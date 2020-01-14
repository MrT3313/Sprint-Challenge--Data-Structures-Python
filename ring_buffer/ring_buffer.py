from doubly_linked_list import DoublyLinkedList

#  - ! - ! - ! - #
#  - ! - ! - ! - #
#  - ! - ! - ! - #

# This is from the ReadMe:
    # "A ring buffer is a non-growable buffer with a fixed size. 
    # When the ring buffer is full and a new element is inserted, 
    # the oldest element in the ring buffer is overwritten with the newest element."

    # BUT that is not exactly what the tests & examples loop like...

    # If it is simple 'First In First Out' => Queue 
        # ALWAYS add to TAIL
        # ALWAYS remove from HEAD 
    
# Interpreted Goal:
    # Input: [a,b,c,d,e,f]
    # Capacity: 3

    # Output: 
    # [a, b, c]    
    # [d, b, c]     {index: 0} is removed --> oldest pointer needs up update to {index: 1}
    # [d, e, c]     {index: 1} is removed --> oldest pointer needs up update to {index: 2}
    # [d, e, f]     {index: 2} is removed --> oldest pointer needs up update BACK TO {index: 0}

# ALOT EASIER => no pointers or tracking just using the build in data structure
    # Output:
    # [a, b, c]    
    # [   b, c, d]          # Remove from Head & Add To Tail    
    # [      c, d, e]       # Remove from Head & Add To Tail
    # [         d, e, f]    # Remove from Head & Add To Tail

# ACTUAL!!
## Input
    # [1,3,4,7,9,10,13,99]
## Output
    # Capacity: 5
    # Storage: 0
    # 1
    # Capacity: 5
    # Storage: 1
    # 3
    # Capacity: 5
    # Storage: 2
    # 4
    # Capacity: 5
    # Storage: 3
    # 7
    # Capacity: 5
    # Storage: 4
    # 9
    # [1, 3, 4, 7, 9]
    # Capacity: 5
    # Storage: 5
    # 10
    # [3, 4, 7, 9, 10]
    # Capacity: 5
    # Storage: 5
    # 13
    # [4, 7, 9, 10, 13]
    # Capacity: 5
    # Storage: 5
    # 99
    # [7, 9, 10, 13, 99]

#  - ! - ! - ! - #
#  - ! - ! - ! - #
#  - ! - ! - ! - #
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
