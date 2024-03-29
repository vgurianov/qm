﻿# -----------------------------------------------------------
# Double-slit experiment simulation
#
# (C) 2023 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/software/slits.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------
#  |psi> = ca*|a> + cb*|b>
#  <a|psi> = ca*<a|a> + cb*<a|b>
#  pa(fi) = |<a|psi>|^2


import math
import random
import matplotlib.pyplot as plt
from scipy import stats

class Item(object): #<<Space>>
    """ Concept = Space cell """
    def __init__(self):
        self.component = None
        self.left =None
        self.right = None

class Component(object): # <<Substance>>
    """ Concept = Physical Matter """
    def __init__(self):
        pass

class Leaf(Component): # <<Atom>>
    """ Concept = Quantum particle """
    def __init__(self):
        pass

class Composite(Component): # <<Category>>
    """ Concept = Duble-path experiment """
    
    def __init__(self, list_l):
        # Physical space
        self.head = None  # Concept = space base
        self.tail = None  # Concept = second point,direction in space
        '''
        self.head = Item()
        self.head.right = Item()
        self.head.right.right = Item()
        self.tail = self.head.right.right
        '''
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
class A(Composite): # <<System>> 
    """ Concept = Path A """
    way_a = '|a>'  # it is control variable
    def __init__(self):
        super().__init__(1) # run __init__ from Composite
    def move_to_x1(self, p):  # it is add + Run + remove operations
        """ Concept = particle displacement A """
        self.add(p)
        self.Run()
        return self.remove()
    
    def Run(self): # <<Exist>>
        """ Concept = particle displacement A """
        self.tail = self.head
    
class B(Composite): # <<System>> 
    """ Concept = Path B """
    way_b = '|b>'  # it is control variable
    def __init__(self):
        super().__init__(1) # run __init__ from Composite
    def move_to_x1(self, p):  # <<Exist>>
        """ Concept = particle displacement B """
        self.add(p)
        self.Run()
        return self.remove()
    
    def Run(self): # <<Exist>>
        """ Concept = particle displacement B """
        self.tail.component = self.head.component
   

c = 0.5/math.sqrt(math.pi)  # probability amplitude 

class Mix(object):  # <<System>>, supposed Mix(A, B)
    """ Concept = Wave function """
    wa = c*complex(math.cos(0), math.sin(0))
    wb = c*complex(math.cos(0), math.sin(0))
    
    def __init__(self):
        # Names conflict resolution
        self.funс = None  # one of the alternatives
        #print(self.attribut1.conjugate()*self.attribut1, self.attribut2.conjugate()*self.attribut2)       
        w = self.wa + self.wb
        pp = w.conjugate()*w
        #p = pp.real
        d = abs(w)**2
        p = d.real /(4.0*c**2)   # norm 1
        #print(p, pp)
        r = random.random()
        #print(d, p, r)
        if r<p:
            rr = random.choice([0,1])
            if rr == 0:
                self.way = A.way_a  # self.way is a control variable
                self.funс = A()  # inherits the operation from A
            else:
                self.way = B.way_b  # self.way is a control variable
                self.funс = B() # inherits the operation from B
        else:
            self.way = None


            
class OneClass(Composite):  # <<System>>, instead of Mix
    """ Concept = Classical double-slit experiment """
    
    def __init__(self):
        super().__init__(1) # run __init__ from Composite
    
    def move_to_x1(self, p):  
        """ Concept = particle displacement A """
        #self.head.component = p   # point A
        return p
    def move_to_x2(self, p):  
        """ Concept = particle displacement B """
        #self.tail.component = p   # point B
        return p

    def Run(self): # <<Exist>>
        p = (c*c + c*c)/(4.0*c**2)  # norm 1
        #print(p, pp)
        r = random.random()
        if r<p:
            rr = random.choice([0,1])
            if rr == 0:
                self.tail.component = self.move_to_x1(self.head.component)  # Path A
            else:
                self.tail.component = self.move_to_x2(self.head.component)  # Path B
        else:
            self.tail.component = None

    def move(self, p):
        self.add(p)
        self.Run()
        return self.remove()
        
        
# ------- Data processing , Category = Epistemology

n = 25     # amount of points
kn = 10    # measuremnts number for phi
a_phi = [] # array phi (argument)
a_p = []   # frequency 
a_pa = []  # analytical probability density 
a_er = []  # measurement error

def data_processing(phi, km):


    # -- measurement 
    a = 0.0
    for k in range(0,kn):
        a = a + km[k]
    a = a/float(kn)
    a_p.append(a)
    
    # -- measurement error calculation
    s = 0
    for k in range(0,kn):
        s = s + (a - km[k])**2

    s = math.sqrt(s/(float(kn)*float(kn-1)))
    # https://en.wikipedia.org/wiki/Confidence_interval#Confidence_interval_for_specific_distributions
    # Where X is the sample mean, and S2 is the sample variance. Then
    # has a Student's t distribution with kn − 1 degrees of freedom
    # Example: alfa = 0.95, from a student t = 3.18 for kn = 4;
    # 0.95 - confidence interval , 60-1 degrees of freedom
    # denoting ppf as the 95th percentile of this distribution
    # print 3.18, stats.t.ppf((1 + 0.95)/2, kn-1)
    tna = stats.t.ppf((1 + 0.95)/2.0, kn-1)
    # and print stats.t.ppf(0.95, kn-1)
    a_er.append(2.0*tna*s)
            
    # -- accurate value
    ca = c
    cb = c
    pa = ca*ca + cb*cb +2.0*ca*cb*math.cos(phi)
    a_pa.append(pa)
    print('fi=', round(phi, 2), 'p=',round(a, 2), 'pa=',round(pa, 2))

    return a

# ---------------------------------
class Node(Composite):  # <<System>>, it is a classical system
    """ Concept = Experimental device for double-slit experiment """
    def __init__(self):
        super().__init__(3)  # run __init__ from Composite
            
    def one_tick(self): 
        #self.head.component = Leaf() # create particle
        self.add(Leaf())
        #self.tail.component = None   # clear detector
        self.remove()
        self.head.right.component = Mix()   # name conflict resolved
        # self.head.right.component = OneClass()   # classical case
        if self.head.right.component.funс is not None:
            self.tail.component = self.head.right.component.funс.move_to_x1(self.head.component) # jump to point x1
        # classical case
        #self.tail.component = self.head.right.component.move(self.head.component) # jump to point x1
            #print(a.way)


    def Run(self): # <<Exist>>
        """  Concept = Experiment """

        #print(A.__mro__)
        #print(A.mro() )
        print('c=',c)
        dfi = (2.0*math.pi-0.0)/float(n-1)  # step
        phi = 0.0
        si = 0.0 # integral (control value)
        while phi <= 2.0*math.pi:
            print ('phi=',phi, ', kn=', kn)
            a_phi.append(phi)
            # prepare the quantum system in the desired state
            Mix.wa = c*complex(math.cos(phi), math.sin(phi))
            Mix.wb = c*complex(math.cos(0.0), math.sin(0.0))

            # --------------
            km = [] # array for statistics, Category = Epistemology
            for k in range(0,kn):
                nn = 0
                total = 0
                for i in range(0,300): # 300 is the number of particles in one pulse of the source
                    self.one_tick()
                    total = total + 1
                    if self.tail.component is not None: # particle detect
                        nn = nn + 1   # counter, Category = Epistemology
                km.append((4.0*c**2)*float(nn)/float(total)) # norm (2*c)**2
                
            a = data_processing(phi, km)
            
            si = si + a*dfi
            phi = phi + dfi

        return si
# ---------------------------------------
class Root(Composite):  # <<Context>>
    """ Concept = Laboratory """
    def __init__(self):
        super().__init__(1)  # run __init__ from Composite
        #self.head.component = Node()
        self.add(Node())

    def Run(self):
        si = self.head.component.Run()
        print('\n', 'Control, integral si = ',si)

# ---------------------------------------

root = Root()
root.Run()

# ------- Data visualization , Category = Epistemology
(fig, ax) = plt.subplots()
ax.plot(a_phi, a_pa, linestyle='-', color='red'
    , label='accurate value')
# ax.plot(a_fi,a_p,marker='x', linestyle=' ', color='blue',label="experiment",)
ax.errorbar(a_phi,a_p,yerr=a_er,c='black',ls='',\
    lw=2,marker='x',mfc='k',ms=5, label='measurements')
ax.legend(loc = 'best')
ax.set_xlabel(r'Phase ($\varphi$),radian',
        fontsize=15)
ax.set_ylabel(r'Probability density ($f$)',
        fontsize=15);        plt.show()

