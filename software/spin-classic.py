# Clasic, spin 1
#
# (C) 2022 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/spin-classic.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import cmath
import random
import matplotlib.pyplot as plt
from scipy import stats
# ----------------------------------
class Item2(object):
    def __init__(self, nm):
        self.next = None
        self.marker = True
        self.number = nm

class Component(object):
    def __init__(self):
        pass
    def Run(self):
        pass
    
    
class Leaf(Component):
    def __init__(self):
        pass

        
    def Run(self):
        pass
    
    def revolve(self, d):

        h1 = self.head1
        while True:
            if d == 0:
                pass
            else:
                pass
                
            if d == 0:
                pass
            else:
                pass

            if not h1.marker:
                break
            h1 = h1.next


class Item(object):
    def __init__(self, nm):
        self.component = None
        self.left = None
        self.right = None
        self.number = nm

 
class Composite(Component):
    def __init__(self):
        self.list_head = Item(1) # Concept = Physical Space
        self.list_head.right = Item(2)
        self.list_head.right.left = self.list_head
        self.list_head.right.right = Item(3)
        self.list_head.right.right.left =self.list_head.right 
        self.list_tail = self.list_head.right.right
        
    def print_right(self):
        itm = self.list_head
        print("print_right:")
        while itm is not None:
            print(itm.number, itm.component)
            itm = itm.right
    def print_left(self):
        itm = self.list_head
        print("print_left:")
        while itm is not None:
            print(itm.number, itm.component)
            itm = itm.left
        
        
class Node(Composite): # Concept = 
    def __init__(self):
        super().__init__()
        self.list_head.component = Leaf()
        
        self.head1 = Item2(1)
        self.head1.next = Item2(2)
        self.head1.next.marker = False 
        self.head1.next.next = self.head1
        

    def Run(self):
        pass
    
    def revolve(self, d):

        h1 = self.head1
        while True:
            if d == 0:
                c1 = self.list_head.component
                c2 = self.list_tail.component
            else:
                c2 = self.list_head.component
                c1 = self.list_tail.component
                
            self.list_head.component = None
            self.list_tail.component = None
            
            if d == 0:
                self.list_tail.component = c1
                self.list_head.component = c2
            else:
                self.list_tail.component = c2
                self.list_head.component = c1

            self.print_right()
            if not h1.marker:
                break
            h1 = h1.next
            
# -------------------------------
# Concept = Laboratory
pl = Node()
pl.print_right()
pl.revolve(1)

