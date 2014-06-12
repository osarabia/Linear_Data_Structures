#!/usr/bin/python

class Stack:

  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)

##

stack = Stack()

stack.push(5)
stack.push(6)

print stack.peek()

print stack.pop()
print stack.pop()

print "isEmpty:"
print stack.isEmpty()
