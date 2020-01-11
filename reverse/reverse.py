class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  # def print_helper(self, node, name):
  #   if node is None: 
  #     print(f'{name}: None')
  #   else: 
  #     print(f'{name}: {node.value}')


  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # -- -- -- MY CODE -- -- -- #
    # Empty LL
    if self.head == None:
      return f'ERROR: Empty LL'
    
    # Set prev to None => it will always start at the position BEFORE the head
    prev = None

    # Start @ head
    current = self.head

    # while current !== None
    while current is not None:
      # save next_node => that will be 'lost' when we 'flip the arrow'
      
      # V1
      # next_node = current.next_node
      # V2
      next_node = current.get_next()
      

      # CHECKING
      # self.print_helper(prev, 'PREV')
      # self.print_helper(current, 'CUR')
      # self.print_helper(next_node, 'NXT')

      # Flip the arrow for the current Node
      # V1
      # current.next = prev
      # V2
      current.set_next(prev)
      
      # tracking the previous and current nodes
      prev = current

      # Iterate current forward in the list
      current = next_node

    # update head
    self.head = prev



newList = LinkedList()
# print(newList)

newList.add_to_head(1)
newList.add_to_head(2)
newList.add_to_head(3)
newList.add_to_head(4)
newList.add_to_head(5)

newList.reverse_list()