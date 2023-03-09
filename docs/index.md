# Ontological description of quantum mechanics
This resource contains software for the article [Simulation of Some Quantum Effects](https://vgurianov.github.io/uml-sp/) by Vasily I. Guryanov. The software implemented in Python.    



## 1.Key points description
Quantum effects may be described as follows.

 * Wave function analog is a class.
 * Wave function collapse analog is to run constructor of the class and create an object, i.e. instance of the class.
 * Superposition analog is multiple inheritances. If the classes have attributes or operations with an identical name then multiple inheritances have a conflict of the names. In this conflict, we will resolve the "quantum rule", i.e. to use an amplitude of wave function.  

 ## 2. Simulation language  

 To describe scientific models, we will use the language of object-oriented simulation UML2 SP [1]. This language is a profile of UML and is an object-oriented version of the well-known IDEF0 methodology. The semantic network is built from frames, which are the "class" UML-element. Each frame is labeled "Concept". This labeled value is assigned a concept, which allows you to build a conceptual model of the subject area.  

 Following the tradition of programming languages such as Smalltalk and Python, we will treat both the classes themselves and class instances as objects. We will rely on the interpretation of quantum mechanics was proposed by Werner Heisenberg (Fock, R.Harre). Class instances will be interpreted as objects of reality in the classical sense, and classes will be interpreted as objects that exist in possibility.

 ## 3. Annotation of the site
