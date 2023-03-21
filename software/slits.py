# -----------------------------------------------------------
# Double-slit experiment simulation
#
# (C) 2023 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/slits.py
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

class Leaf(object):
    """ Concept = Quantum particle """
    def __init__(self):
        pass

class Item(object):
    """ Concept = Space cell """
    def __init__(self):
        self.component = None
        self.left =None
        self.right = None

# The alternatives pakage
class A(object):
    """ Concept = Path A """
    way_a = '|a>'
    def __init__(self):
        pass
    def move_to_x1(self, p):
        """ Concept = particle displacement (transfer) """
        return p
class B(object):
    """ Concept = Path B """
    way_b = '|b>'
    def __init__(self):
        pass
    def move_to_x1(self, p):
        """ Concept = particle displacement (transfer) """
        return p

c = 0.5/math.sqrt(math.pi)  # probability amplitude 

class Mix():  # supposed Mix(A, B)
    """ Concept = Wave function """
    wa = c*complex(math.cos(0), math.sin(0))
    wb = c*complex(math.cos(0), math.sin(0))
    
    def __init__(self):
        # Name conflict resolution
        self.fun = None
        #print(self.attribut1.conjugate()*self.attribut1, self.attribut2.conjugate()*self.attribut2)       
        w = self.wa + self.wb
        pp = w.conjugate()*w
        #p = pp.real
        d = abs(w)**2
        p = d.real /(4.0*c**2)
        #print(p, pp)
        r = random.random()
        #print(d, p, r)
        if r<p:
            rr = random.choice([0,1])
            if rr == 0:
                self.way = A.way_a
                self.fun = A()
                #self.move_to_x1 = A.move_to_x1  # inherits the operation from A
            else:
                self.way = B.way_b
                self.fun = B()
                #self.move_to_x1 = B.move_to_x1  # inherits the operation from B
        else:
            self.way = None

# ---------------------------------
class Node(object):  # it is a classical object
    """ Concept = Experimental device """
    def __init__(self):
        self.x0 = None    # source
        self.x1 = None    # screen point
        # Physical space (from 3 cells)
        self.head = Item() #space base
        self.head.right = Item()
        self.head.right.right = Item()
        self.tail = self.head.right.right # direction in space

    def one_tick(self): 
        self.x0 = Leaf()  # create particle
        # self.head.component = Leaf() is more correctly
        self.x1 = None    # clear detector
        a = Mix()   # name conflict resolved
        #print(a.way)
        if a.way is not None:
            self.x1 = a.fun.move_to_x1(self.x0)  # jump to point x1
            # self.tail.component = a.fun.move_to_x1(self.x0) is more correctly


    def Run(self): # tag "Exist"
        """  Concept = Experiment """

        #print(A.__mro__)
        #print(A.mro() )
        print('c=',c)
        a_p = []   # frequency 
        a_pa = []  # analytical probability density 
        a_er = []  # measurement error
        a_phi = [] # array phi (argument)
        n = 25     # amount of points
        dfi = (2.0*math.pi-0.0)/float(n-1)  # step
        phi = 0.0
        si = 0.0 # integral (control value)
        while phi <= 2.0*math.pi:
            kn = 10 # measuremnts number for phi
            print ('phi=',phi, ', kn=', kn)
            a_phi.append(phi)
            # prepare the quantum system in the desired state
            Mix.wa = c*complex(math.cos(phi), math.sin(phi))
            Mix.wb = c*complex(math.cos(0.0), math.sin(0.0))

            # --------------
            km = [] # array for statistics
            for k in range(0,kn):
                nn = 0
                total = 0
                for i in range(0,300): # 300 is the number of particles in one pulse of the source
                    self.one_tick()
                    total = total + 1
                    if self.x1 is not None: # particle detect
                        nn = nn + 1
                km.append((4.0*c**2)*float(nn)/float(total))
                
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
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            # and print stats.t.ppf(0.95, kn-1)
            a_er.append(2.0*tna*s)
            
            # -- accurate value
            ca = c
            cb = c
            pa = ca*ca + cb*cb +2.0*ca*cb*math.cos(phi)
            a_pa.append(pa)
            print('fi=', round(phi, 2), 'p=',round(a, 2), 'pa=',round(pa, 2))

            si = si + a*dfi
            phi = phi + dfi

        print('\n', 'Integral si = ',si)
        # graph
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


# ---------------------------------------
""" Concept = Laboratory """
node = Node()
node.Run()
