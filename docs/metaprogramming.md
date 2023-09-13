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

## 3. Scope  

At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:  

1. The innermost region, which is searched first, contains local names. The scope of any nested function whose search begins with the nearest enclosing scope contains nonlocal names, but also nonglobal names.  
2. The next area after the last one contains the global names of the current module.  
3. The outermost scope (last lookup) is the namespace containing the built-in names.  
If the variable name is declared global, then all references and assignments go directly to the middle area, containing the global names of the module. If the variables are not local, then these variables are read-only. Attempting to write to such a variable will simply create a new local variable in the innermost scope, leaving the outer variable with the same name unchanged.

