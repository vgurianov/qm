# -----------------------------------------------------------
# Quantum entanglement simulation, var 2
#
# (C) 2023 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/entanglement.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import random
from enum import Enum
     
class State(Enum):
        ZERO = 1
        ONE = 2

class Component(object): # <<Substance>>
    """ Concept = Physical Matter """
    def __init__(self):
        pass
    def Run(self):
        pass

class Leaf0(Component): # <<Atom>>
    """ Concept = Particle in the base state 0 """
    def __init__(self):
        self.state = State.ZERO
class Leaf1(Component): # <<Atom>>
    """ Concept = Particle in the base state 1 """
    def __init__(self):
        self.state = State.ONE


class MixOne(Leaf0, Leaf1):
    """ Concept = Quantum particle """
    w0 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    w1 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    
    def __init__(self):
        random.seed()
        p = self.w0.conjugate()*self.w0
        p = abs(self.w0.real)**2
        r = random.random()
        print (p,r)
        if r <= p.real:
            self.struc = Leaf0() #State0.attribute
        else:
            self.struc = Leaf1() #State1.attribute


# ------------------------------
class Item(object): #<<Space>>
    """ Concept = Space cell """
    def __init__(self):
        self.component = None
        self.left =None
        self.right = None
        
class Composite(Component): # <<Category>>
    """ Concept = Composite system """
    
    def __init__(self, list_l):
        # Physical space
        self.head = None  # Concept = space base
        self.tail = None  # Concept = second point,direction in space
        if list_l > 0 :
            self.head = Item()
            item = self.head
            for i in range(1,list_l):
                item.right = Item()
                item = item.right
                #print(list_l,i)
            self.tail = item
            # in addition, it is necessary to make left links

        # and shift_space, rotation_space, and itc. operations
    def add(self, p):
        self.head.component = p
    def remove(self):
        p = self.tail.component
        self.tail.component = None
        return p

# The alternatives package
class Two00(Composite): # <<System>>

    def __init__(self):
        super().__init__(3) # run __init__ from Composite
        self.head.component = Leaf0()
        self.tail.component = Leaf0()
class Two01(Composite):

    def __init__(self): # <<System>>
        super().__init__(3) # run __init__ from Composite
        self.head.component = Leaf0()
        self.tail.component = Leaf1()
class Two10(Composite): # <<System>>

    def __init__(self):
        super().__init__(3) # run __init__ from Composite
        self.head.component = Leaf1()
        self.tail.component = Leaf0()
class Two11(Composite):  # <<System>>

    def __init__(self):
        super().__init__(3) # run __init__ from Composite
        self.head.component = Leaf1()
        self.tail.component = Leaf1()
        

class Mix(Two00,Two01,Two10,Two11):  # <<System>>
    """ Concept =  Quantum system """
    # general case
    #w00 = (1.0/math.sqrt(4.0))*complex(math.cos(0.0), math.sin(0.0))
    #w01 = (1.0/math.sqrt(4.0))*complex(math.cos(0.0), math.sin(0.0))
    #w10 = (1.0/math.sqrt(4.0))*complex(math.cos(0.0), math.sin(0.0))
    #w11 = (1.0/math.sqrt(4.0))*complex(math.cos(0.0), math.sin(0.0))
    # entaglement:
    w00 = 0.0*complex(math.cos(0.0), math.sin(0.0))
    w01 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    w10 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    w11 = 0.0*complex(math.cos(0.0), math.sin(0.0))

    def __init__(self):
        
        random.seed()
        #p = self.w0.conjugate()*self.w0
        p00 = abs(self.w00)**2
        #p = self.w0.conjugate()*self.w0
        p01 = abs(self.w01)**2
        #p = self.w0.conjugate()*self.w0
        p10 = abs(self.w10)**2
        #p = self.w0.conjugate()*self.w0
        p11 = abs(self.w11)**2
        r = random.random()
        #print (p,r)
        if r <= p00:
            t = Two00()
        elif r > p00 and r <= p01+p00:
            t = Two01()
        elif r > p01+p00 and r <= p10+p01+p00:
            t = Two10()
        else:
            t = Two11()
        self.head = t.head.component
        self.tail = t.tail.component
        
PP = None  # Global variable

class A(Composite): # <<System>> 
    """ Concept =  Alice """
    def __init__(self):
        super().__init__(1) # run __init__ from Composite

    def Run(self):
        global PP
        PP = Mix() # the wave function collapse
        self.m1 = PP.head.state  # measurement
        return self.m1

    def accept(self, _m): # accept measurement
        self.m2 = _m  


class B(Composite): # <<System>>  
    """ Concept =  Bob """
    def __init__(self):
        super().__init__(1) # run __init__ from Composite
        
    def Run(self):
        # Bob
        global PP
        self.m2 = PP.tail.state # measurement
        return self.m2

    def accept(self, _m): # accept measurement
        self.m1 = _m  



class Node(Composite):  #  <<System>>, it is a classical object
    """ Concept =  Quantum entanglement experiment """

    def __init__(self):
        super().__init__(3) # run __init__ from Composite
        self.head.component = A()  # place of Alice
        self.tail.component = B()  # place of Bob


    def Run(self):  # <<Exist>>
        confirm = 0
        nonconfirm = 0

        for k in range(0,5000):
            
            # Alise 
            m1 = self.head.component.Run()
            # Bob
            m2 = self.tail.component.Run()
            
            # message from Alice to Bob and from Bob to Alice
            self.head.right.component = m1
            self.tail.component.accept(self.head.right.component)
            self.head.right.component = m2
            self.tail.component.accept(self.head.right.component)
            
            # collection and processing of data    
            if m1 != m2:
                confirm = confirm + 1
            else:
                nonconfirm = nonconfirm + 1
        count = confirm + nonconfirm
            
        print ('count = ',count, 'confirm=',confirm, 'nonconfirm=',nonconfirm)
        print ('confirm = ',float(confirm)/float(count))
        print ('nonconfirm = ',float(nonconfirm)/float(count))

 

# -------------------------
node = Node()
node.Run()
