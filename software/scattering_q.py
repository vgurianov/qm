# Quantum collision
# All particles is detection, All classes
# -----------------------------------------------------------
# Quantum scatering
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
    
    def scattering_amplitude(self, theta): # theta in rad
        # Blohincev1976ru.djvu, p.331
        # CGSE
        hbar = 1.05e-27 # erg/s = h/(2pi)
        e = 4.8e-10 # qulon
        # The atom
        Z = 79.0
        gamma = 1.0
        a0 = 1.0e-15 
        a = gamma*a0/math.pow(Z,1.0/3.0) # nucliu
        a = 1.0e-8 # size, diametr
        # The alpha-particle
        mu = 6.64e-24 # g, mass alpha-particle
        v = 1.0e+9 # c/s, velosity alpha-particle
        E = mu*v*v/2.0
        #E = 4.05*1e+6*1.602e-12  # erg, or 4.05 MeV
        #print('E, erg=', E)
        #v = math.sqrt(2.0*E/mu)
        #k = math.sqrt(2.0*mu*E)/hbar
        k = mu*v/hbar
        #print('v,c/s=', v ,'k, c-1=',k,'k*a=',k*a)
    
        K= 2.0*k*math.sin(theta/2.0) # (79.17)
        e1 = 2.0*e # for alpha-particle
        F = Z/math.pow(1.0 + K*K*a*a,2) #(79.17) atom-factor
        A = - (e*e1/(2.0*mu*v*v))*(Z-F)*math.pow(1.0/math.sin(theta/2.0),2) #(79.12)
        #print ('A=',A)
        return A
        
    
    def draw(self):
        a_theta_grad = []
        a_pa = []

        theta = 0.0e+1
        while theta <= math.pi:
            theta = theta + 10.0*math.pi/180.0
            a_theta_grad.append(theta*180.0/math.pi)
            p = abs(self.scattering_amplitude(theta))**2
            a_pa.append(p)
            #print('p= ',p,', theta= ',theta, 'or ', theta*180/math.pi)

        (fig, ax) = plt.subplots()
        ax.plot(a_theta_grad, a_pa,   linestyle='-', color='red'
        , label='accurate')
        ax.set_ylabel(r'Density ($p$)', fontsize=15)
        ax.set_xlabel(r'Angle ($\vartheta$, grad)',
              fontsize=15);        plt.show()

        plt.show()

class Result_Sort(Composite): # Concept = Particle Scattering

    def __init__(self,_init_position,_list_head):
        self.angle = []
        self.angle.append(0.0)
        self.result = []
        self.result.append(0.0)
        self.amplitude2 = []
        self.amplitude2.append(0.0)
        self.ampl2 = []
        self.ampl2.append(0.0)
        rez = Result()
        a2sum = 0.0
        agl = 0.0
        for i in range(1,18+1):
            self.result.append(0.0)
            agl = agl + 10.0   # 10 grad
            self.angle.append(agl)
            a = rez.scattering_amplitude((agl-5.0)*math.pi/180.0)
            aa = a.conjugate()*a
            aa = abs(a)**2
            self.ampl2.append(aa)
            da = 10.0*aa
            int_a2 = self.amplitude2[i-1]+ da
            self.amplitude2.append(int_a2)
            a2sum = a2sum + da
        for i in range(1,18+1):
            aa = self.ampl2[i]
            self.amplitude2[i] = self.amplitude2[i]/a2sum
            #print(i,aa, self.amplitude2[i])
            
        self.Run(_init_position,_list_head)
    
    def Run(self, _init_position,_list_head): # ang in grad
        random.seed()
        r = random.random()
        il = _list_head
        done = True
        i = 0
        while done:
            i = i +1
            if i>18 :
                break
            if r>self.amplitude2[i-1] and r<=self.amplitude2[i]:
                self.result[i-1] = self.result[i-1]+1.0
                il.component = _init_position()  # particle move to ended 
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
            tna = stats.t.ppf((1.0 + 0.95)/2.0, self.kn-1)
            #print(tna)
            # and print stats.t.ppf(0.95, kn-1)
            s = self.a_ss[j]
            self.r_er.append(2.0*2.0*tna*s)  # 2- 2 line  
        print('r_er=',self.r_er)

    def analitic_data_classic(self): # formula (4), p.470
        n = 0.6e+26 # 5.0*1000.0 # particles count
        t = 1.0 #
        b = 1.0e-13 # cm, stop distance
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
            
    def analitic_data(self): # formula (4), p.470
        self.a_angle_ad = []
        self.a_rr_b = []
        a2sum = 0.0
        
        rez = Result()
        d_agl = 2.5
        agl = 5.0
        while (agl <= 180.0):
            self.a_angle_ad.append(agl)
            a = rez.scattering_amplitude(agl*math.pi/180.0)
            aa = a.conjugate()*a
            #aa = abs(a)**2
            da = d_agl*aa
            self.a_rr_b.append(da)
            a2sum = a2sum + da
            agl = agl + d_agl   # 10 grad
        for i in range(0,len(self.a_angle_ad)):
            self.a_rr_b[i] = self.a_rr_b[i]/a2sum
        #print(self.a_angle_ad)
        #print(self.a_rr_b)

    def draw(self):
        # Analitic
        self.analitic_data()
        (fig, ax) = plt.subplots()
        ax.plot(self.a_angle_ad,self.a_rr_b, marker=' ',linestyle='-', color='blue'
                , label=r'analitic')
        # Experiment
        a_a = []
        for j in range(0,len(self.ang)):
            a_a.append(self.ang[j]+5.0)
        #print(a_a)
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
           
        a_r = []
        self.kn = 5
        for i in range(0,self.kn):
            total = 0.0

            dat = GetData()
            for i in range(0,1000):
                self.init_position = Leaf 
                rs = Result_Sort(self.init_position, self.list_head)
                #rs.sortIt(self.init_position, self.list_head )
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
#r = Result()
#r.draw()

# rs = Result_Sort()

pl = Node()
ang, a_r = pl.Run()
dp = DataProcessing(ang, a_r,pl.kn)
dp.mean()
dp.err_calculation()
dp.draw()



