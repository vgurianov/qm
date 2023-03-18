# -----------------------------------------------------------
# Bell's test
#
# (C) 2023 Vasyliy I. Gurianov
# Github: https://github.com/vgurianov/qm/bell.py
# Released under MIT License
# email: vg2007sns@rambler.ru
# -----------------------------------------------------------

import math
import random
import matplotlib.pyplot as plt
from scipy import stats

class State0(object):
    attribute = 0
    def __init__(self):
        self.attr = State0.attribute
class State1(object):
    attribute = 1
    def __init__(self):
        self.attr = State1.attribute

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


class Node(object):  # it is a classical object
    # ! Space-Time ordering

    def __init__(self):
        pass

    def table(self):
        for ab in range(0,360,45):
            for bc in range(0,360,45):
                for ac in range(0,360,45):
                    s1 = math.sin((2.0*math.pi/360.0)*float(ab)/2.0)*math.sin((2.0*math.pi/360.0)*float(ab)/2.0)
                    s2 = math.sin((2.0*math.pi/360.0)*float(bc)/2.0)*math.sin((2.0*math.pi/360.0)*float(bc)/2.0)
                    s3 = math.sin((2.0*math.pi/360.0)*float(ac)/2.0)*math.sin((2.0*math.pi/360.0)*float(ac)/2.0)
                    if s1 <= s2+s3:
                        print(ab,bc,ac,round(s1,2),round(s2,2),round(s3,2),'inequality is holds')
                    else:
                        print(ab,bc,ac,round(s1,2),round(s2,2),round(s3,2),'inequality is broken')
                  

        # Table
        # 270 45 45 0.5 0.15 0.15 inequality is broken
        # 270 45 90 0.5 0.15 0.5 inequality is holds
        # 45 135 180 0.15 0.85 1.0 inequality is holds
        # 270 315 315 0.5 0.15 0.15 inequality is broken
        # 90 315 45 0.5 0.15 0.15 inequality is broken
 
    def experiment1(self): # Bell's test
        aU_bU = 0  # Up and Down
        #bD_cD = 0  # Other variant the Bell
        bU_cU = 0
        aU_cU = 0
        a_aU_bU = []  
        a_bU_cU = []
        a_aU_cU = []

        # AB = 240° BC = 60° AC = 300°  /315 225 135
        AB = 90.0
        BC = 315.0
        AC = 48.0
        ab = AB*(2.0*math.pi/360.0)
        bc = BC*(2.0*math.pi/360.0)
        ac = AC*(2.0*math.pi/360.0)
        angle = [ab, bc, ac]

        kn = 10  # number measurement
        for j in range(0,kn):
            _aU_bU = 0.0  
            _bU_cU = 0.0
            _aU_cU = 0.0
            for k in range(0,100):
                random.seed()

                r = random.choice([0,1,2])
                alpha = angle[r]
                # Influence H(alpha)
                Two.w00 = (1.0/math.sqrt(2.0))*math.sin(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
                Two.w01 = (1.0/math.sqrt(2.0))*math.cos(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
                Two.w10 = (1.0/math.sqrt(2.0))*math.cos(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
                Two.w11 = (1.0/math.sqrt(2.0))*math.sin(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
                two_p = Two()

                if r == 0 and two_p.one.attribute == 0 and two_p.two.attribute == 0 :
                    aU_bU = aU_bU + 1
                    _aU_bU = _aU_bU + 1.0
                #if r == 1 and two_p.one.attribute == 1 and two_p.two.attribute == 1 :
                #    bD_cD = bD_cD + 1
                if r == 1 and two_p.one.attribute == 0 and two_p.two.attribute == 0 :
                    bU_cU = bU_cU + 1
                    _bU_cU = _bU_cU + 1.0
                if r == 2 and two_p.one.attribute == 0 and two_p.two.attribute == 0 :
                    aU_cU = aU_cU + 1
                    _aU_cU = _aU_cU + 1.0
                
            a_aU_bU.append(_aU_bU)  
            a_bU_cU.append(_bU_cU)
            a_aU_cU.append(_aU_cU)

        # errors calculate ---------------
        # average
        av_aU_bU = 0.0 
        #av_bU_cU = 0.0 
        #av_aU_cU = 0.0
        av_sum = 0.0
        for k in range(0,kn):
            av_aU_bU = av_aU_bU + a_aU_bU[k] 
            #av_bU_cU = av_bU_cU + a_bU_cU[k] 
            #av_aU_cU = av_aU_cU + a_aU_cU[k]
            av_sum = av_sum + a_bU_cU[k] + a_aU_cU[k]

        av_aU_bU = av_aU_bU/float(kn) 
        #av_bU_cU = av_bU_cU/float(kn) 
        #av_aU_cU = av_aU_cU/float(kn)
        av_sum = av_sum/float(kn)
            
        # sigma^2
        s_aU_bU = 0.0
        #s_bU_cU = 0.0
        #s_aU_cU = 0.0
        s_sum = 0.0
        for k in range(0,kn):
            s_aU_bU = s_aU_bU + (av_aU_bU - a_aU_bU[k])**2
            #s_bU_cU = s_bU_cU + (av_bU_cU - a_bU_cU[k])**2
            #s_aU_cU = s_aU_cU + (av_aU_cU - a_aU_cU[k])**2
            s_sum = s_sum + (av_sum - (a_bU_cU[k]+a_aU_cU[k]))**2
            
        tna = stats.t.ppf((1.0 + 0.95)/2, kn-1)
        # and print stats.t.ppf(0.95, kn-1)
        s_aU_bU = math.sqrt(s_aU_bU/(float(kn)*float(kn-1)))
        s_aU_bU = tna*s_aU_bU # Delta
        #s_bU_cU = math.sqrt(s_bU_cU/(float(kn)*float(kn-1)))
        #s_aU_cU = math.sqrt(s_aU_cU/(float(kn)*float(kn-1)))
        s_sum = math.sqrt(s_sum/(float(kn)*float(kn-1)))
        s_sum = tna*s_sum  # Delta
        
        # results ------------------------
        #print ('aU_bU = ',aU_bU, ', bD_cD=',bD_cD, ', aU_cU=',aU_cU)
        #print (aU_bU,' <= ',bD_cD+aU_cU)
        print ('aU_bU = ',aU_bU, ', bU_cU=',bU_cU, ', aU_cU=',aU_cU)
        print (aU_bU,' <= ',bU_cU+aU_cU)
        #print ('Err is ', round(s_aU_bU,2),round(s_bU_cU,2),round(s_aU_cU,2))
        print ('Err is ', round(s_aU_bU,2),round(s_sum,2))

        # analitic
        s1 = math.sin((2.0*math.pi/360.0)*AB/2.0)*math.sin((2.0*math.pi/360.0)*AB/2.0)
        s2 = math.sin((2.0*math.pi/360.0)*BC/2.0)*math.sin((2.0*math.pi/360.0)*BC/2.0)
        s3 = math.sin((2.0*math.pi/360.0)*AC/2.0)*math.sin((2.0*math.pi/360.0)*AC/2.0)
        print('should be')
        if s1 <= s2+s3:
            print(AB,BC,AC,round(s1,2),round(s2,2),round(s3,2),'inequality is holds')
        else:
            print(AB,BC,AC,round(s1,2),round(s2,2),round(s3,2),'inequality is broken')
        
    def experiment0(self): # Rotation devices
        # rotation
        a_p00 = []
        a_p01 = []
        a_p10 = []
        a_p11 = []
        a_conf = []
        a_nonconf = []
        a_pa = []
        a_confa = []
        a_er00 = []
        a_er01 = []
        a_er10 = []
        a_er11 = []
        a_er_conf = []
        a_er_nonconf = []
        a_alpha = []
        n = 50
        dfi = (2.0*math.pi-0.0)/float(n-1)
        alpha = 0.0
        si = 0.0 # integral
        while alpha <= 2.0*math.pi:
            kn = 10 # measuremnts number for alpha
            print ('alpha=',alpha, ', kn=', kn)
            a_alpha.append(alpha)
            # Influence H(alpha)
            Two.w00 = (1.0/math.sqrt(2.0))*math.sin(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
            Two.w01 = (1.0/math.sqrt(2.0))*math.cos(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
            Two.w10 = (1.0/math.sqrt(2.0))*math.cos(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))
            Two.w11 = (1.0/math.sqrt(2.0))*math.sin(alpha/2.0)*complex(math.cos(0.0), math.sin(0.0))

            # --------------
            km00 = []
            km01 = []
            km10 = []
            km11 = []
            conf = []
            nonconf = []
            for k in range(0,kn):
                nn00 = 0
                nn01 = 0
                nn10 = 0
                nn11 = 0
                total = 0
                lost = 0
                confirm = 0
                nonconfirm = 0
                for i in range(0,300):
                    two = Two()
                    if two.one.attribute == 0 and two.two.attribute == 0:
                        nn00 = nn00 + 1
                        confirm = confirm +1
                    elif two.one.attribute == 0 and two.two.attribute == 1: 
                        nn01 = nn01 + 1
                        nonconfirm = nonconfirm +1
                    elif two.one.attribute == 1 and two.two.attribute == 0: 
                        nn10 = nn10 + 1
                        nonconfirm = nonconfirm +1
                    elif two.one.attribute == 1 and two.two.attribute == 1: 
                        nn11 = nn11 + 1
                        confirm = confirm +1
                    else: 
                        lost = lost + 1
                    #print(a.state)
                    total = total + 1
                        
                km00.append(float(nn00)/float(total))
                km01.append(float(nn01)/float(total))
                km10.append(float(nn10)/float(total))
                km11.append(float(nn11)/float(total))
                conf.append(float(confirm)/float(total))
                nonconf.append(float(nonconfirm)/float(total))
            # --
            a = 0.0
            for k in range(0,kn):
                a = a + km00[k]
            a = a/float(kn)
            a_p00.append(a)
            
    
            s = 0
            for k in range(0,kn):
                s = s + (a - km00[k])**2
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
            a_er00.append(2.0*tna*s)

            a = 0.0
            for k in range(0,kn):
                a = a + km01[k]
            a = a/float(kn)
            a_p01.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - km01[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er01.append(2.0*tna*s)

            a = 0.0
            for k in range(0,kn):
                a = a + km10[k]
            a = a/float(kn)
            a_p10.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - km10[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er10.append(2.0*tna*s)

            a = 0.0
            for k in range(0,kn):
                a = a + km11[k]
            a = a/float(kn)
            a_p11.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - km11[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er11.append(2.0*tna*s)

            a = 0.0
            for k in range(0,kn):
                a = a + conf[k]
            a = a/float(kn)
            a_conf.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - conf[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er_conf.append(2.0*tna*s)
            a = 0.0
            for k in range(0,kn):
                a = a + nonconf[k]
            a = a/float(kn)
            a_nonconf.append(a)
            s = 0
            for k in range(0,kn):
                s = s + (a - nonconf[k])**2
            s = math.sqrt(s/(float(kn)*float(kn-1)))
            tna = stats.t.ppf((1 + 0.95)/2, kn-1)
            a_er_nonconf.append(2.0*tna*s)

            # -- accurate
            #cc = 0.5/math.sqrt(math.pi)
            pa = 0.5*math.sin(alpha/2.0)**2
            c2 = 0.5*math.cos(alpha/2.0)
            #pa = c1*c1
            a_pa.append(pa)
            print('phi=', round(alpha, 2), 'p=',round(a, 2), 'pa=',round(pa, 2), 'lost=',round(lost, 2))
            pa = math.sin(alpha/2.0)**2
            a_confa.append(pa)

            si = si + a*dfi
            alpha = alpha + dfi

        print('\n', 'Integral si = ',si)
        # graph
        (fig, ax) = plt.subplots()
        #ax.plot(a_alpha, a_pa, linestyle='-', color='red'
        #, label='accurate')
        # ax.plot(a_fi,a_p,marker='x', linestyle=' ', color='blue',label="experiment",)
        #ax.errorbar(a_alpha,a_p00,yerr=a_er00,c='black',ls='',\
        #lw=1,marker='x',mfc='k',ms=3, label='measurements 00')
        #ax.errorbar(a_alpha,a_p01,yerr=a_er01,c='black',ls='',\
        #lw=1,marker='o',mfc='k',ms=2, label='measurements 01')
        #ax.errorbar(a_alpha,a_p10,yerr=a_er10,c='black',ls='',\
        #lw=1,marker='o',mfc='k',ms=2, label='measurements 10')
        #ax.errorbar(a_alpha,a_p11,yerr=a_er11,c='black',ls='',\
        #lw=1,marker='o',mfc='k',ms=2, label='measurements 11')
        ax.errorbar(a_alpha,a_conf,yerr=a_er_conf,c='green',ls='',\
        lw=1,marker='o',mfc='k',ms=2, label='agree')
        ax.plot(a_alpha, a_confa, linestyle='-', color='red'
        , label='agree(accurate)')
        ax.errorbar(a_alpha,a_nonconf,yerr=a_er_nonconf,c='blue',ls='',\
        lw=1,marker='o',mfc='k',ms=2, label='disagree')
        ax.legend(loc = 'best')
        ax.set_xlabel(r'Angle ($\alpha$),radian',
              fontsize=15)
        ax.set_ylabel(r'Рrobability density ($p$)',
              fontsize=15);        plt.show()

# -------------------------
node = Node()
#node.table()
#node.experiment0() # device rotation
node.experiment1()  # Bell's test

