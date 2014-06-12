#!/usr/bin/python

class Node:

  def __init__(self,value):
    self.val = value
    self.next = None

  def getval(self):
    return self.val

  def setval(self,value):
    self.val = value

node = Node(3)

print node.getval()
node.setval(5)
print node.getval()

