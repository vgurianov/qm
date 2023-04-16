# Quantum Superposition
Let us describe the method that is used to construct a frame network.
Let entity A have the same mathematical model as entity B. Then, by conducting full-scale experiments on one of these entities, one can obtain information about the other, including quantitative data.
For example, an oscillatory circuit and a pendulum have the same mathematical model. By conducting experiments on an oscillatory circuit, it is possible to calculate the characteristics of the pendulum.
This method has a disadvantage. Misjudgments are possible. For example, knowing the chemical composition of one system, nothing can be said about the chemical composition of another system.  
  
Superposition analog is multiple inheritances. If the classes have attributes or operations with an identical name then multiple inheritances have a conflict of the names, Fig.1. In this conflict, we will resolve the "quantum rule", i.e. to use an amplitude of wave function. More strictly it can be formulated as follows. The mathematical model that describes multiple inheritance with name conflicts is the Hilbert space.  


 ![Image](qbit.png)  

 Figure 1: The qbit model  

 The diagram shows two states 0 and 1. The states have an attribute with the same name Attribute. In this case, there is a naming conflict in the Leaf class. To resolve the conflict, we use the complex numbers w1 and w2. The squares of these numbers give the probability of finding a state 0 or 1. In the general case, this is an analogue of the Hilbert's space.  

 You can implement it like this (multiple inheritances emulation)
``` python
 def __init__(self):
    w = self.w1
    d = w.conjugate()*w    # or d = abs(w)**2
    rd = d.real
    r = random.random()
    if r<rd:
        self.Attribute = Class1.Attribute
    else:
        self.Attribute = Class2.Attribute
```
Note that in Python, the name conflict is resolved simply, the value of the attribute of the first class in the inheritance list is assigned. We are redefining this rule. It is also worth noting that in this case we are assigning a value to an attribute of an object, not a class.  

The complete code is here [https://github.com/vgurianov/qm/software/states.py](https://github.com/vgurianov/qm/blob/master/software/states.py).
