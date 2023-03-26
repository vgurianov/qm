# Complex numbers

## 1. Integer arithmetic

Our problem is to find a data structure and an addition algorithm for these structures, so that the mathematical model of this process is described by integer arithmetic. This problem has several solutions. We will consider one of the possible options.  

Consider the following data structure  
``` python  
class Item:
    def __init__(self, n, sn):
        self.num = n  # it is control field
        self.right = None
        self.sign = sn
```  
where *sn* is the enumeration {zero, plus, minus}.  

Consider a looped one-way list.  
The elected list is *zero = Item(0)*.
This list is modeled as null.
Every other list necessarily contains this object in its basis. For example list
```
0 , sign= 0
1 , sign= -1
2 , sign= -1
3 , sign= -1
```
modeled as number -3.

Let's create two looped lists *z1* and *z2*. For addition (superposition), we define the following algorithm   
``` python
def add(z1, z2):
    i = 0
    z0 = Item(i, 0)
    z = z0
    while True:
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
```  
where *act()* is some action. Note that after the process ends, *z1* and *z2* will be in their initial state, i.e. looped list is invariant of the addition operation.  

It is not difficult to make sure that this situation is modeled by integer arithmetic. Full code is here [adding.py](adding.py).

We can also define a multiplication algorithm. This will be two nested loops
``` python    
def multiplication(zz1, zz2):
    i = 0
    z0 = Item(i, 0)
    z = z0
    z1 = zz1.right
    z2 = zz2.right
    if (z1.sign == 1 and z2.sign == 1) or (z1.sign == -1 and z2.sign == -1) :
        sign = 1
    elif (z1.sign == 1 and z2.sign == -1) or (z1.sign == -1 and z2.sign == 1) :
        sign = -1

    else:
        sign = 0

    while sign != 0:
        z2 = zz2.right
        while True:
            act()
            i = i + 1
            z.right = Item(i, sign)
            z = z.right
            z2 = z2.right
            if z2.sign == 0:
                break

        z1 = z1.right
        if z1.sign == 0 :
            break
    z.right = z0
    return z0

```   
After the process ends, *zz1* and *zz2* will be in their initial state, i.e. looped list is invariant of the multiplication operation.   
Full code is here [multiplication.py](multiplication.py).  

Algorithm for multiplying by -1 (sign change)  
``` python    
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
```  

## 2. Complex number structure
Consider an ordered pair of looped lists.  
``` python    
class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i
```  
and define the following processes.

A process that is modeled by the addition of complex numbers.
``` python    
def cadd(cz1, cz2):
    r = add(cz1.real, cz2.real)
    i = add(cz1.imag, cz2.imag)
    z = ComplexNumber(r,i)
    return z
```  
A process that is modeled by the multiplication of complex numbers.
``` python    
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
```  
A process that is modeled by the square of the modulus of the amplitude.
``` python    
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
```  
 
The complete code is here [https://github.com/vgurianov/qm/software/complex.py](https://github.com/vgurianov/qm/blob/master/software/complex.py).  

From a physical point of view, the following processes are of particular interest:  
- cadd(z1,z2) are the process superposition z1 and z2
- amplitude_squared(z) is a chose of alternative.  
