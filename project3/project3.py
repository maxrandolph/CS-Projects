"""
Max Randolph
CS 260
Dr. Marcus Brown
Spring 2015
Programming Assignment 3
"""

class Node(object):
    def __init__(self,data,next=None,last=None):
        self.data=data
        self.next=next
        self.last=last
    def __iter__(self)
        cursor=self._
        while not cursor is None:
            yield cursor.data
            cursor=cursor.next

    def __str__(self):
        return "{"+",".join(map(str,self))+"}"
class DoubleLinkedList(object):
    def __init__(self,sourceCollection=None):
        self._size=0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
        self._items=None
    def __iter__(self):
        cursor=self._items
        while not cursor is None:
            yield cursor.data
            cursor=cursor.next

    def add(self,item):
        self._items=Node(item,self._items)
        self._size+=1

    def clear(self):
        self._size=0
        self._items=None

        
    def remove(self,item):
        if not item in self:#check precondition and raise if nec.
            raise KeyError(str(item)+" not in bag")
        probe=self._items#search for node containing target items
        #probe will point to the target node, and trailer will point to node before, if it exists.
        trailer=None
        for targetItem in self:
            if targetItem==item: #item found so stop for loop.
                break
            #unhook the node to be deleted either the first one or the one thereafter    
            trailer=probe
            probe=probe.next
        if probe == self._items:
            self._items=self._items.next
        else:
            trailer.next = probe.next
        self._size-=1
def main():
    lastNode=Node("I'm the last")
    n=0
    nodeA=Node(n,lastNode)
    for x in range(0,100):
        n+=1
        nodeA=Node(n,nodeA)
    print(nodeA)
main()