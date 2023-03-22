# Clasic collision
# All particles is detection, All classes
# -----------------------------------------------------------
# Clasic collision
#
# (C) 2022 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import cmath
import random
import matplotlib.pyplot as plt
from scipy import stats
# ----------------------------------
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

class Item(object):
    def __init__(self):
        self.component = None
        self.left = None
        self.right = None

 
class Composite(Component):
    def __init__(self):
        self.init_position = None  # Concept = Particle Source
        self.list_head = Item() # Concept = Healf Shere, i.e. Physical Space
        self.section_number = 18 # Concept = Space Resolution
        il = self.list_head
        for i in range(0,self.section_number):
            il.right = Item()
            il = il.right
        print(self.list_head)    

class Result:
    # c.470
    e = 4.65e-10 # SGSE
    # The atom
    Z = 100 #79.0
    gamma = 1.0
    a0 = 1.0e-15 
    a = gamma*a0/math.pow(Z,1.0/3.0) # nucliu
    a = 1.4e-8 # cm, R atom
    # The alpha-particle
    mu = 6.64e-24 # g, mass alpha-particle
    v = 2.09e+9 # cm/s, velosity alpha-particle
    q = 2.0*e  # q alfa-particle
    b = 0.1*2.0*Z*e*q/(mu*v*v) # 3.4e-13 cm
    
    def angle(self, pp): # formula (1), p.470
        # impact parametr
        p =self.a*pp
        #print ('a=',a,p,'b=',b, 'p/b=', p/b) 
        theta = 2.0*math.atan(self.b/(2.0*p))
        return theta
    
    def draw(self):
        a_theta_grad = []
        a_pa = []

        d = 1.0e-5  # teta ~ 90 grad
        p = 0.0e+1
        while p <= d*10.0:
            p = p + d
            a_pa.append(p)
            theta = self.angle(p)
            a_theta_grad.append(theta*180/math.pi)
            #print('p= ',p,', theta= ',theta, 'or ', theta*180/math.pi)

        (fig, ax) = plt.subplots()
        ax.plot(a_pa, a_theta_grad,  linestyle='-', color='red'
        , label='accurate')
        ax.set_ylabel(r'Angle ($\vartheta$, grad)', fontsize=15)
        ax.set_xlabel(r'Parametr ($p$)',
              fontsize=15);        plt.show()

        plt.show()

class Result_Sort(Composite): # Concept = Particle Scattering
    def __init__(self):
        self.angle = []
        self.angle.append(0.0)
        self.result = []
        self.result.append(0.0)
        agl = 0.0
        for i in range(1,18+1):
            self.result.append(0.0)
            agl = agl + 10.0   # 10 grad
            self.angle.append(agl)

    def sortIt(self, ang, _init_position,_list_head): # ang in grad
        il = _list_head
        done = True
        i = 0
        while done:
            i = i +1
            if ang>self.angle[i-1] and ang<=self.angle[i]:
                self.result[i-1] = self.result[i-1]+1.0
                il.component = _init_position  # particle move to ended 
                done = False
            il = il.right
        

class GetData: # Concept = Detector
    def __init__(self):
        self.angle = []
        self.angle.append(0.0)
        self.result = []
        self.result.append(0.0)
        agl = 0.0
        for i in range(1,18+1):
            self.result.append(0.0)
            agl = agl + 10.0   # 10 grad
            self.angle.append(agl)

    def scaning(self, _list_head):
        il = _list_head
        #print(il)
        done = True
        i = 0
        while done:
            i = i +1
            if il.component is not None:
                self.result[i-1] = self.result[i-1]+1.0
                il.component = None 
                done = False
            il = il.right
            if il is None:
                done = False
                #print('list tail')
        
# ---------------------------------------------
class DataProcessing:
    def __init__(self, _ang, _a_r, _kn):
        self.ang = _ang
        self.a_r = _a_r
        self.kn = _kn

    def mean(self):
        self.a_rr = [] # sample mean
        self.a_ss = [] # sample variance sigma^2
        for j in range(0,len(self.ang)):

            a = 0.0
            for k in range(0,self.kn):
                km = self.a_r[k]
                a = a + km[j]
            a = a/float(self.kn)
            self.a_rr.append(a)
            #print(theta_grad, a, Mix.w)

            s = 0
            for k in range(0,self.kn):
                km =self. a_r[k]
                s = s + (a - km[j])**2

            self.a_ss.append(math.sqrt(s/(float(self.kn)*float(self.kn-1))) )

        print('a_rr=',self.a_rr)
        print('a_ss=',self.a_ss)

    def err_calculation(self):
        # Error calculation
        self.r_er = []
        for j in range(0,len(self.ang)):
        # https://en.wikipedia.org/wiki/Confidence_interval#Confidence_interval_for_specific_distributions
        # Where X is the sample mean, and S2 is the sample variance. Then
        # has a Student's t distribution with kn − 1 degrees of freedom
        # Example: alfa = 0.95, from a student t = 3.18 for kn = 4;
        # 0.95 - confidence interval , 60-1 degrees of freedom
        # denoting ppf as the 95th percentile of this distribution
        # print 3.18, stats.t.ppf((1 + 0.95)/2, kn-1)
            tna = stats.t.ppf((1 + 0.95)/2, self.kn-1)
            #print(tna)
            # and print stats.t.ppf(0.95, kn-1)
            s =self.a_ss[j]
            self.r_er.append(2.0*2.0*tna*s)  # 2- 2 line  
        print('r_er=',self.r_er)

    def analitic_data(self): # formula (4), p.470
        n = 0.6e+26 # 5.0*1000.0 # particles count
        t = 1.0 #
        b = Result.b  #1.0e-13 # cm, stop distance
        self.a_rr_a = []
        ro_total = 0.0
        for j in range(0,len(self.ang)):
            fi1 = ang[j]+10.0
            fi2 = fi1 + 10.0
            g = math.pi/180
            ctg1 = 1.0/math.tan(g*fi1/2.0)
            ctg2 = 1.0/math.tan(g*fi2/2.0)
            ro = (math.pi/4.0)*n*t*b*b*(ctg1*ctg1 - ctg2*ctg2)
            ro_total = ro_total + ro
            self.a_rr_a.append(ro)
        for j in range(0,len(self.ang)): # normalization
            self.a_rr_a[j] = self.a_rr_a[j]/ro_total 

    def draw(self):
        self.analitic_data()
        a_aa = []
        for j in range(0,len(self.ang)):
            a_aa.append(self.ang[j]+5.0)
        (fig, ax) = plt.subplots()
        ax.plot(a_aa,self.a_rr_a, marker='x',linestyle='-', color='blue'
                , label=r'analitic')
        a_a = []
        for j in range(0,len(self.ang)):
            a_a.append(self.ang[j]+5.0)
        ax.errorbar(a_a,self.a_rr,yerr=self.r_er,c='black',ls='',
        lw=2,marker='o',mfc='k',ms=5, label=r'measurement')
        ax.legend(loc = 'best')
        ax.set_xlabel(r'Angle ($\vartheta$, grad)', fontsize=15)
        ax.set_ylabel(r'N($\vartheta$)', fontsize=15);

        plt.show()
        
# --------------------------------------------------------------

class Node(Composite): # Concept = Elastic Particle Scattering
    def __init__(self):
        super().__init__()

    def Run(self):
        
        d = 1.0e-5  # teta ~ 90 grad, aton size 1e-8 sm, nuclio 1.0e-15 sm
        d = 1.0e-5
        rez = Result()
        
        # We see d for information
        print('search d')
        a_theta_grad = []
        a_pa = []
        p = 0.0e+1
        while p <= d*100.0:
            p = p + d
            a_pa.append(p)
            theta = rez.angle(p)
            a_theta_grad.append(theta*180/math.pi)
            #print('p= ',p,', theta= ',theta, 'or ',  theta*180/math.pi)
        print('--------------')
            
        a_r = []
        self.kn = 5
        for i in range(0,self.kn):
            total = 0.0

            random.seed()
            #rs = Result_Sort()
            dat = GetData()
            for i in range(0,1000):
                self.init_position = Leaf() 
                p = 50.0*d*random.random() 
                tht = rez.angle(p)
                rs = Result_Sort()
                rs.sortIt(tht*180.0/math.pi, self.init_position, self.list_head )
                dat.scaning(self.list_head)
                self.init_position = None
                total = total + 1.0
            #print(rs.angle)
            #print(rs.result)
            #print(dat.result)
    
            ang = dat.angle[0:len(dat.angle)-1] 
            r = dat.result[0:len(dat.angle)-1] #enclude end point, it is interval
            for i in range(0,len(r)):  # normalization
                r[i] = r[i]/total

            a_r.append(r)
            
        print('ang= ',ang)
        print('a_r= ',a_r)
        return ang, a_r 





# -------------------------------
# Concept = Laboratory
r = Result()
r.draw()

pl = Node()
ang, a_r = pl.Run()
dp = DataProcessing(ang, a_r,pl.kn)
dp.mean()
dp.err_calculation()
dp.draw()


