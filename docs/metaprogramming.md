# Some necessary information from Python 3

## 1. Class attributes and class instance variables
``` python
class Dog:

    # data attribute (class variable),
    # common to all instances of the class
    kind = 'canine'

    def __init__(self, name):
        # class instance variable
        # unique for each instance
        self.name = name
```
The rezult is  
```  
>>> d = Dog('Fido')
>>> e = Dog('Buddy')

# the `kind` variable will be common to 
# all instances of the `Dog` object
>>> d.kind
# 'canine'
>>> e.kind    
# 'canine'

# the `name` variable will be unique 
# for each instance
>>> d.name
# 'Fido'
>>> e.name    
# 'Buddy'
```
If the same attribute name occurs both in a class instance and in the class itself, then the attribute lookup determines the priority of the class instance.  

## 2. Class method  

``` python
class MyClass:
    tick = 0
    def Run(self):
        return 'instance method called', self, self.tick

    @classmethod
    def cRun(cls):
        cls.tick = cls.tick + 1
        return 'class method called', cls, cls.tick

print(MyClass.cRun())
p = MyClass()
print(p.Run())
```  
The rezult is  
```
======= RESTART: 
('class method called', <class '__main__.MyClass'>, 1)
('instance method called', <__main__.MyClass object at 0x000001F13D0E7070>, 1)

```  
Instance methods can also access the class itself through the self.__class__ attribute.
