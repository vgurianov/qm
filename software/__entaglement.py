# -----------------------------------------------------------
# Quantum entanglement
#
# (C) 2023 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/entanglement.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import random

class State0(object):
    attribute = 0
    def __init__(self):
        self.attr = State0.attribute
class State1(object):
    attribute = 1
    def __init__(self):
        self.attr = State1.attribute
class Leaf(State0, State1):
    w0 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    w1 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    
    def __init__(self):
        random.seed()
        p = self.w0.conjugate()*self.w0
        p = abs(self.w0.real)**2
        r = random.random()
        print (p,r)
        if r <= p.real:
            self.attr = 0 #State0.attribute
        else:
            self.attr = 1 #State1.attribute

class Two00(object):
    one = State0()
    two = State0()

    def __init__(self):
        self.one = State0()
        self.two = State0()
        
class Two01(object):
    one = State0()
    two = State1()

    def __init__(self):
        pass
class Two10(object):
    one = State1()
    two = State0()

    def __init__(self):
        pass
class Two11(object):
    one = State1()
    two = State1()

    def __init__(self):
        pass

class Two(Two00,Two01,Two10,Two11):
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
        self.one = t.one
        self.two = t.two
        
PP = None  # Global variable

class A(object): # Alice
    def __init__(self):
        #self._pp = None
        pass

    def run(self):
        global PP
        PP = Two() # the wave function collapse
        m = PP.one.attr  # measure and send m
        return m

class B(object): # Bob
    def __init__(self):
        #self._pp = None
        pass
        
    def run(self, _m):
        # Bob
        global PP
        m2 = PP.two.attr # measure
        m1 = _m  # receipt m
        return m2

class Cell(object):
    def __init__(self):
        pass
        
    def __init__(self):
        self.content = None
        self.right = None
        self.left = None

class Times(object):  # it is a process or a change
    def __init__(self):
        self.next = None



class Node(object):  # it is a classical object
    # ! Space-Time ordering

    def __init__(self):
        self.tmp = None
        self.space = Cell()
        self.space.right = Cell()
        self.space.right.right = Cell()
        self.space.content = A()
        self.space.right.right.content = B()
        #self.pp = None


    def experiment(self):  # <<Exist>>
        confirm = 0
        nonconfirm = 0

        for k in range(0,5000):
            
            self.tmp = Times()
            # Alise 
            m1 = self.space.content.run()
            #self.pp = self.space.content._pp
            self.tmp.next = Times()
            # message
            self.space.right.content = m1
            self.tmp.next.next = Times()
            # Bob
            #self.space.right.right.content._pp = self.pp
            m2 = self.space.right.right.content.run(self.space.right.content)
            self.space.right.content = None
            self.tmp.next.next.next = Times()
            
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
node.experiment()
