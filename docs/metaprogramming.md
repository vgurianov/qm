class Dog:

    # data attribute (class variable),
    # common to all instances of the class
    kind = 'canine'

    def __init__(self, name):
        # class instance variable
        # unique for each instance
        self.name = name

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
