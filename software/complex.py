# complex numbers
import math

sqr = 0
def act():
    global sqr
    sqr = sqr + 1

class Item:
    def __init__(self, n, sn):
        self.num = n
        self.left = None
        self.right = None
        self.sign = sn
            
def sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1
    
def create_loop(n):
    z = Item(0, 0)
    zz = z
    t = 1
    while t<=abs(n) :
        zz.right = Item(t, sign(n))
        zz = zz.right
        t = t + 1
    zz.right = z
    return z

def loop_print(z):
    zz = z
    print(zz.num, ', sgn=', zz.sign)
    zz = zz.right
    while zz.sign != 0 :
        print(zz.num, ', sgn=', zz.sign)
        zz = zz.right

# --------------------

def add(z1, z2):
    #z1 = zz1
    #z2 = zz2
    i = 0
    z0 = Item(i, 0)
    z = z0
    while True:
        #print(z1.num, z2.num)
        if z1.sign == 0  and z2.sign != 0 :
            act()
            i = i + 1
            z.right = Item(i, z2.sign)
            z = z.right
            z2 = z2.right
        elif z1.sign != 0  and z2.sign == 0  :
            act()
            i = i + 1
            z.right = Item(i, z1.sign)
            z = z.right
            z1 = z1.right
        else:
            if z1.sign == z2.sign and z1.sign != 0  and z2.sign != 0 :
                act()
                i = i + 1
                z.right = Item(i, z1.sign)
                z = z.right
                act()
                i = i + 1
                z.right = Item(i, z2.sign)
                z = z.right
            z1 = z1.right
            z2 = z2.right

        if z1.sign == 0 and z2.sign == 0:
            break
    z.right = z0
    return z0

def multiplication(z1, zz2):
    z2 = zz2
    i = 0
    z0 = Item(i, 0)
    z = z0
    z1 = z1.right
    z2 = z2.right
    if (z1.sign == 1 and z2.sign == 1) or (z1.sign == -1 and z2.sign == -1) :
        sign = 1
    elif (z1.sign == 1 and z2.sign == -1) or (z1.sign == -1 and z2.sign == 1) :
        sign = -1
    
    else:
        sign = 0
        
    while sign != 0:
        #z2 = z2.right
        while True:
            #print(z1.num, z2.num)
            act()
            i = i + 1
            z.right = Item(i, sign)
            z = z.right
            z2 = z2.right
            if z2.sign == 0:
                z2 = z2.right
                break

        z1 = z1.right
        if z1.sign == 0 :
            break
    z.right = z0
    return z0

def change_sign(zz):
    z = zz.right
    i = 0
    z0 = Item(i,0)
    t = z0
    while True:
        i = i + 1
        if z.sign == 1:
            t.right = Item(i, -1)
        elif z.sign == -1:
            t.right = Item(i, 1)
        else:
            pass
        t = t.right
        z = z.right
        if z.sign == 0:
            break
    t.right = z0
    return z0
    
# --------------------------------------------------

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

def cadd(cz1, cz2):
    r = add(cz1.real, cz2.real)
    i = add(cz1.imag, cz2.imag)
    z = ComplexNumber(r,i)
    return z

def cmultiplication(cz1, cz2):
    r1 = multiplication(cz1.real, cz2.real)
    r2 = multiplication(cz1.imag, cz2.imag)
    r2 = change_sign(r2)
    r = add(r1,r2)
    i1 = multiplication(cz1.imag, cz2.real)
    i2 = multiplication(cz1.real, cz2.imag)
    i = add(i1,i2)
    z = ComplexNumber(r,i)
    return z

def complex_print(z):
    print('Real:')
    loop_print(z.real)
    print('Imag:')
    loop_print(z.imag)


def amplitude_squared(z):
    i = 0
    z0 = Item(i,0)
    t = z0
    x = z.real.right
    while True:
        y = z.real.right
        while True:
            i = i + 1
            act()
            t.right = Item(i, 1)
            t = t.right
            y = y.right
            if y.sign == 0:
                break
        x = x.right
        if x.sign == 0:
            break

    x = z.imag.right
    while True:
        y = z.imag.right
        while True:
            i = i + 1
            act()
            t.right = Item(i, 1)
            t = t.right
            y = y.right
            if y.sign == 0:
                break
        x = x.right
        if x.sign == 0:
            break
    t.right = z0
    return z0
    
    
    
# --------------------------------------------------
    
n1 = 2
n2 = 1
print(n1,',',n2)

x1 = create_loop(n1)
loop_print(x1)
print('--')

x2 = create_loop(n2)
loop_print(x2)
z1 = ComplexNumber(x1,x2)
c1 = complex(n1,n2)
print(c1)

n3 = 0
n4 = 1
print(n3,',',n4)

x3 = create_loop(n3)
loop_print(x3)

print('--')

x4 = create_loop(n4)
loop_print(x4)
z2 = ComplexNumber(x3,x4)
#print(z2)
c2 = complex(n3,n4)
print(c2)


print('++++++')
print('z1', 'z2')
sqr = 0
#z = cadd(z1,z2)
#z = cmultiplication(z1,z2)
print('can be: ',n1*n1+n2*n2, ', fact: ')
#complex_print(z)
cc = amplitude_squared(z1)
loop_print(cc)   
        
