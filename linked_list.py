
class LinkedList:
  def __init__(self, *args):
    def generate_list(args):
      if args == ():
        return None
      else:
        return Node(args[0], generate_list(args[1:]))
        
    if args == ():
      self.head = None
    else:
      self.head = generate_list(args)

  def __str__(self):
    if self.head == None:
      return '[]'
    return '[' + str(self.head) + ']'

  def __eq__(self, other):
    pass

  def __contains__(self, val):
    pass

  def __iter__(self):
    pass

  def __next__(self):
    pass

  def append(self, val):
    if self.head == None:
      self.head = Node(val, None)
    else:
      self.head.append(val)

  def extend(self, ll):
    if type(ll) != LinkedList and ll != None:
      raise TypeError('ll is not a LinkedList')
    if self.head == None:
      self.head = ll
    else:
      self.head.extend(ll)



class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __str__(self):
    ret_val = ''
    it = self
    while it != None:
      ret_val = ret_val + f'{it.val}, '
      it = it.next
    ret_val = ret_val[0:-2]
    return ret_val

  def append(self, val):
    if self.next == None:
      self.next = Node(val, None)
    else:
      return self.next.append(val)

  def extend(self, ll):
    if self.next != None:
      self.next.extend(ll)
    else:
      self.next = ll.head

L1 = LinkedList(100, 10)
L2 = LinkedList(200, 20)
print(L1)
L1.append(1)
print(L1)
L1.extend(L2)
print(L1)
