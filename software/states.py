# states superposition

import math
import random
import matplotlib.pyplot as plt
from scipy import stats


# H(alpha)|d> = |psi> = c1*|d> + c2*|u>

class A(object):
    state = '|d>'
    def __init__(self,d):
        pass
class B(object):
    state = '|u>'
    def __init__(self,d):
        pass

c = 1.0/math.sqrt(2.0)

class Mix(A, B):
    w1 = c*complex(math.cos(0), math.sin(0))
    w2 = c*complex(math.cos(0), math.sin(0))
    
    def __init__(self,d):
        # A conflict names is desade
        #print(self.attribut1.conjugate()*self.attribut1, self.attribut2.conjugate()*self.attribut2)       
        w = self.w1
        pp = w.conjugate()*w
        #p = pp.real
        d = abs(w)**2
        p = d.real
        #print(p, pp)
        r = random.random()
        #print(d, p, r)
        if r<p:
            self.state = A.state
        else:
            self.state = B.state

# ---------------------------------
class Plant(object):  # it is a classical object
    def __init__(self):
        pass

    def experiment1(self):

        print(A.__mro__)
        print(A.mro() )
        print('c=',c)
        a_p1 = []
        a_p2 = []
        a_pa = []
        a_er1 = []
        a_er2 = []
        a_alpha = []
        n = 50
        dfi = (2.0*math.pi-0.0)/float(n-1)
        alpha = 0.0
        si = 0.0 # integral
        while alpha <= 2.0*math.pi:
            kn = 10 # measuremnts number for alpha
            print 'alpha=',alpha, ', kn=', kn
            a_alpha.append(alpha)
            # Influence H(alpha)
            Mix.w1 = math.cos(alpha)*complex(math.cos(0.0), math.sin(0.0))
            Mix.w2 = math.sin(alpha)*complex(math.cos(0.0), math.sin(0.0))

            # --------------
            km1 = []
            km2 = []
            for k in range(0,kn):
                nn1 = 0
                nn2 = 0
                total = 0
                for i in range(0,300):
                    a = Mix(0)
                    if a.state == '|d>':
                        nn1 = nn1 + 1
                    else:
                        nn2 = nn2 + 1
                    #print(a.state)
                    total = total + 1
                        
                km1.append(float(nn1)/float(total))
                km2.append(float(nn2)/float(total))
            # --
            a = 0.0
            for k in range(0,kn):
                a = a + km1[k]
            a = a/float(kn)
            a_p1.append(a)
            
    
            s = 0
            for k in range(0,kn):
                s = s + (a - km1[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            # https://en.wikipedia.org/wiki/Confidence_interval#Confidence_interval_for_specific_distributions
            # Where X is the sample mean, and S2 is the sample variance. Then
            # has a Student's t distribution with kn − 1 degrees of freedom
            # Example: alpha = 0.95, from a student t = 3.18 for kn = 4;
            # 0.95 - confidence interval , 60-1 degrees of freedom
            # denoting ppf as the 95th percentile of this distribution
            # print 3.18, stats.t.ppf((1 + 0.95)/2, kn-1)
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            # and print stats.t.ppf(0.95, kn-1)
            a_er1.append(2.0*tna*s)

            a = 0.0
            for k in range(0,kn):
                a = a + km2[k]
            a = a/float(kn)
            a_p2.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - km2[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er2.append(2.0*tna*s)

            # -- accurate
            #cc = 0.5/math.sqrt(math.pi)
            c1 = math.cos(alpha)
            c2 = math.sin(alpha)
            pa = c1*c1
            a_pa.append(pa)
            print('fi=', round(alpha, 2), 'p=',round(a, 2), 'pa=',round(pa, 2))

            si = si + a*dfi
            alpha = alpha + dfi

        print('\n', 'Integral si = ',si)
        # graph
        (fig, ax) = plt.subplots()
        ax.plot(a_alpha, a_pa, linestyle='-', color='red'
        , label='accurate')
        # ax.plot(a_fi,a_p,marker='x', linestyle=' ', color='blue',label="experiment",)
        ax.errorbar(a_alpha,a_p1,yerr=a_er1,c='black',ls='',\
        lw=2,marker='x',mfc='k',ms=5, label='measurements |u>')
        ax.errorbar(a_alpha,a_p2,yerr=a_er2,c='black',ls='',\
        lw=2,marker='x',mfc='k',ms=5, label='measurements |d>')
        ax.legend(loc = 'best')
        ax.set_xlabel(r'Influence ($\alpha$)',
              fontsize=15)
        ax.set_ylabel(r'Probability ($p$)',
              fontsize=15);        plt.show()

# ---------------------------------------
pl = Plant()
pl.experiment1()
