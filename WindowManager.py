class Node:
   def __init__(self, id):
       self.id = id
       self.prev = None
       self.next = None




class WindowManager:
   OPEN = 1
   MINIMIZED = 2


   def __init__(self):
       self.state = {}
       self.nodes = {}
       self.head = None
       self.tail = None


   def add_front(self, node):
       node.prev = None
       node.next = self.head
       if self.head:
           self.head.prev = node
       self.head = node
       if not self.tail:
           self.tail = node


   def remove(self, node):
       if node.prev:
           node.prev.next = node.next
       else:
           self.head = node.next
       if node.next:
           node.next.prev = node.prev
       else:
           self.tail = node.prev


   def open(self, id: int):
       if id not in self.state:
           self.state[id] = self.OPEN
           node = Node(id)
           self.nodes[id] = node
           self.add_front(node)
       elif self.state[id] == self.MINIMIZED:
           self.state[id] = self.OPEN
           self.add_front(self.nodes[id])
       else:
           node = self.nodes[id]
           self.remove(node)
           self.add_front(node)


   def focus(self, id: int):
       if id in self.state:
           if self.state[id] == self.MINIMIZED:
               self.state[id] = self.OPEN
               self.add_front(self.nodes[id])
           else:
               node = self.nodes[id]
               self.remove(node)
               self.add_front(node)


   def minimize(self, id: int):
       if id in self.state and self.state[id] == self.OPEN:
           self.state[id] = self.MINIMIZED
           self.remove(self.nodes[id])


   def restore(self, id: int):
       if id in self.state and self.state[id] == self.MINIMIZED:
           self.state[id] = self.OPEN
           self.add_front(self.nodes[id])


   def close(self, id: int):
       if id in self.state:
           if self.state[id] == self.OPEN:
               self.remove(self.nodes[id])
           del self.nodes[id]
           del self.state[id]


   def top(self) -> int:
       return self.head.id if self.head else -1


   def list(self):
       res = []
       curr = self.head
       while curr:
           res.append(curr.id)
           curr = curr.next
       return res




if __name__ == "__main__":
   wm = WindowManager()
  
   wm.open(1)
   wm.open(2)
   wm.open(3)
   print(wm.top())


   wm.minimize(3)
   print(wm.top())


   wm.focus(1)
   print(wm.list())


   wm.restore(3)
   print(wm.list())


   wm.close(1)
   print(wm.list())
