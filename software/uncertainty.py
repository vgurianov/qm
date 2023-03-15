# -----------------------------------------------------------
# The Uncertainty Principle
#
# (C) 2023 Vasyliy I. Gurianov, Russia
# Github: https://github.com/vgurianov/qm/uncertainty.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import random
from scipy import stats

class StateM0(object):
    """ Concept = Base state m0 """
    M = 0
    def __init__(self):
        self.m = StateM0.M

class StateM1(object):
    """ Concept = Base state m1 """
    M = 1
    def __init__(self):
        self.m = StateM0.M
        

class StateL0(StateM0,StateM1):
    """ Concept = Base state l0 """
    # M = 0
    w00 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    # M = 1
    w10 = -(1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    L = 0

    def __init__(self):
        pass

class StateL1(StateM0,StateM1):
    """ Concept = Base state l1 """
    # M = 0
    w01 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    # M = 1
    w11 = (1.0/math.sqrt(2.0))*complex(math.cos(0.0), math.sin(0.0))
    L = 1

    def __init__(self):
        pass


class Mix(StateL0,StateL1):
    """ Concept = Wave function """
    c1 = 1.0/math.sqrt(2.0)
    #c2 = math.sqrt(1.0 - c1*c1)
    c2 = -1.0/math.sqrt(2.0)
    # L = 0
    v0 = c1*complex(math.cos(0.0), math.sin(0.0))
    # L = 1
    v1 = c2*complex(math.cos(0.0), math.sin(0.0))
    
    def __init__(self):
        random.seed()
        pl = self.v0.conjugate()*self.v0 
        r = random.random()
        if r <= pl.real:
            self.l = 0 #StateL0.L
        else:
            self.l = 1 #StateL1.L
        am = self.w00.conjugate()*self.v0 + self.w01.conjugate()*self.v1
        pm = am.conjugate()*am
        #print(pm)
        r = random.random()
        if r <= pm.real:
            self.m = 0 #StateM0.M
        else:
            self.m = 1 #StateM1.M
        
class Node(object):  # it is a classical object
    """ Concept = Experimental device """
    def __init__(self):
        pass

    def experiment(self):

        count_m0 = 0.0
        count_m1 = 0.0
        count_l0 = 0.0
        count_l1 = 0.0
        arr_m0 = []
        arr_m1 = []
        arr_l0 = []
        arr_l1 = []

        kn = 10  # number measurement
        for k in range(0,kn):
            _count_m0 = 0.0
            _count_m1 = 0.0
            _count_l0 = 0.0
            _count_l1 = 0.0
            for i in range(0,10):  #10 - number of observed events in a single experiment
                p = Mix()
                #p.ini()  # this measurement
                #print('a=',p.a,'b=',p.b)
                if p.m == 0:
                    count_m0 = count_m0 + 1.0
                    _count_m0 = _count_m0 + 1.0
                else:
                    count_m1 = count_m1 + 1.0
                    _count_m1 = _count_m1 + 1.0
                if p.l == 0:
                    count_l0 = count_l0 + 1.0
                    _count_l0 = _count_l0 + 1.0
                else:
                    count_l1 = count_l1 + 1.0
                    _count_l1 = _count_l1 + 1.0
            arr_m0.append(_count_m0/(_count_m0 + _count_m1))
            arr_m1.append(_count_m1/(_count_m0 + _count_m1))
            arr_l0.append(_count_l0/(_count_l0 + _count_l1))
            arr_l1.append(_count_l1/(_count_l0 + _count_l1))
            print(_count_m0,_count_m1,_count_l0,_count_l1)
            
                        
        # errors calculate ---------------
        av_m0 = 0.0 
        av_m1 = 0.0 
        av_l0 = 0.0 
        av_l1 = 0.0 
        for k in range(0,kn):
            av_m0 = av_m0 +arr_m0[k]  
            av_m1 = av_m1 +arr_m1[k] 
            av_l0 = av_l0 +arr_l0[k] 
            av_l1 = av_l1 +arr_l1[k] 
        av_m0 = av_m0/float(kn) 
        av_m1 = av_m1/float(kn) 
        av_l0 = av_l0/float(kn) 
        av_l1 = av_l1/float(kn) 

        s_m0 = 0.0 
        s_m1 = 0.0 
        s_l0 = 0.0 
        s_l1 = 0.0 
        for k in range(0,kn):
            s_m0 = s_m0 + (av_m0 - arr_m0[k])**2
            s_m1 = s_m1 + (av_m1 - arr_m1[k])**2 
            s_l0 = s_l0 + (av_l0 - arr_l0[k])**2 
            s_l1 = s_l1 + (av_l1 - arr_l1[k])**2 

        tha = stats.t.ppf((1.0 + 0.95)/2, kn-1)
        # print stats.t.ppf(0.95, kn-1)
        print('tha=',tha)
        s_m0 = tha*math.sqrt(s_m0/(float(kn)*float(kn-1)))
        s_m1 = tha*math.sqrt(s_m1/(float(kn)*float(kn-1)))
        s_l0 = tha*math.sqrt(s_l0/(float(kn)*float(kn-1)))
        s_l1 = tha*math.sqrt(s_l1/(float(kn)*float(kn-1)))
        
        # -------------------------------------------------------    
        print('For m')
        count_m = count_m0 + count_m1
        print(count_m, count_m0, count_m1)
        print(count_m0/count_m, count_m1/count_m)
        print('Err:',round(s_m0,2),round(s_m1,2))
            
        print('For l')
        count_l = count_l0 + count_l1
        print(count_l, count_l0, count_l1)
        print(count_l0/count_l, count_l1/count_l)
        print('Err:',round(s_l0,2), round(s_l1,2))

        

# ---------------------------------------
""" Concept = Laboratory """
node = Node()
#node.printParticles()
node.experiment()
