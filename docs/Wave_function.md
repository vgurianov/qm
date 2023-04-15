## Wavefunction and wavefunction collapse
A number of scientists have developed the idea that algorithms can be used to describe physical phenomena. In greatest detail this idea is described in books by Stefan Wolfram \cite{Wolfram2002,Wolfram2020}. In these books, using graphs (networks) as a basis for representing nature and then deriving the laws of physics from algorithms using the graphs has been proposed. A similar point of view is stated in G. Hooft's book \cite{Hooft2015}.  
  
Our approach develops this idea further on the basis of an object-oriented paradigm. Instead of algorithms, we propose considering the exchange of messages between objects. Since objects are instances of classes, and links (communications) are instances of associations, the scientific model can be described as a frame semantic network, in particular it can be seen as an ontological description.  

The choice of concepts for models of quantum effects is based on one or another interpretation of quantum mechanics. At present, there are at least eleven interpretations of quantum mechanics. In this paper, we propose a description of quantum effects based on the concept of ''affordances'' \cite{Harre1990}. This interpretation of quantum mechanics was first advanced by Werner Heisenberg and then developed by Vladimir A. Fock. According to this interpretation, quantum reality includes both objects in the classical sense and objects that exist only in the form of possibility or probability. This view is supported by both physicists and philosophers. A fairly detailed exposition of this interpretation is given in book \cite{Sevalnikov2009}.  

Following the tradition of programming languages such as the Smalltalk and  Python, we will treat both the classes themselves and class instances as objects. Class instances will be interpreted as objects of reality in the classical sense, and classes will be interpreted as objects that exist in possibility. Classes can also create new objects-class, so there won't be an endless chain of metaclasses.  
  
Wave function analog is a class, Fig.1.  This figure shows a frame named Frame1, which is rendered as a "Class" UML-element. The Frame1 is assigned the concept "Wave function". This concept has the designation ID (ID may not match Frame1).  
Wave function collapse analog is to run constructor of the class and create an object, i.e. instance of the class.  

![Image](colapse1.png)  

Figure 1: Quantum and classical description of a point particle


We separate wave function collapse and measurement over a quantum system. In our opinion, the collapse of the wave function can occur in nature without any measurements.
The measurement procedure is shown in Fig.2  

![Image](colapse2.png)  
Figure 2: The wavefunction collapse  


The measurement results upon collapse of the wave function can vary, but the outcome after collapse will remain the same. If we were to repeat the measurement, we would obtain the same value every time for the measured property.
