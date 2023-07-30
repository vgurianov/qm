In the publication of [Sevalnikov A. Review of reports of the Round Table "Fundamental Problems of Modern Quantum Mechanics"](https://vox-journal.org/html/issues/480)  
a group of questions related to the problem of the existence (reality) of quantum objects is considered.

1. Are there quantum objects (state vectors) between measurements
(psi-ontic point of view)? Or the wave function only describes our knowledge
(psy-epistemological point of view)?
2. What are the advantages of the two-modus model of existence "potential actual" for describing quantum phenomena?
3. What parts of the formalism of quantum theory most adequately describe the existence of quantum objects (state vector, field operators, complex phase, possible paths in the formalism of path integrals)?
4. Does the classical world emerge from the quantum world, and if so, how?
5. In what space do state vectors exist (superposition)?
6. At what time do state vectors (superposition) exist?

Our ontological description of quantum effects is based on the two-modus model developed by A. Yu. Sevalnikov (Institute of Philosophy, Russian Academy of Sciences) and V. E. Terekhovich (St. Petersburg State University). Therefore, we will consider the listed questions in the following order: first, we will give the answer of A. Yu. Sevalnikov and V. E. Terekhovich, in the form of quotations, and then we will give a description in UML SP.  
We emphasize that many statements are in the nature of assumptions.

Answers.
### 1. Are there quantum objects (state vectors) between measurements (psi-ontic point of view)? Or the wave function only describes our knowledge (psy-epistemological point of view)?  
"Quantum objects exist both before the measurement (observation) procedure and after. But before observation, these objects exist in a fundamentally different way than after the act of registration." A. Y. Sevalnikov  
"... the wave function is closely connected with the potential mode of being, objectively
existing, although it is beyond the bounds of the manifest (“other being”,"pregeomeotry"). "A. Yu. Sevalnikov  
"Between dimensions, quantum objects are in a potential mode of being
in the form of a set of many possible states that are incompatible in the current
mode." V. E. Terekhovich
  
Quantum objects (class-objects) exist whether we observe them or not. The class-object (potential modus of being) spawns an instance-object (actual modus of existence) after it receives the «create» message. The constructor call simulates the collapse of the wave function. The collapse of the wave function occurs in nature regardless of measurements.
The wave function is a mathematical model of an class-object.  
When it comes to dimensions, the constructor is called first, and then a message that simulates the dimension is sent to the instance-object. The returned value will be the result of the measurement. Thus, the measurement is a composite message.

### 2. What are the advantages of the two-modus model of existence "potential actual" for describing quantum phenomena?  
Giving legitimacy to physical existence in a potential modus removes the ontological uncertainty around quantum paradoxes that have arisen from attempts to reconcile the properties of quantum systems with the properties of classical phenomena.
V. E. Terekhovich  

The two-mode model is a philosophical basis for choosing concepts and constructing frame networks that describe quantum effects.

### 3. What parts of the formalism of quantum theory most adequately describe the existence of quantum objects (state vector, field operators, complex phase, possible paths in the formalism of path integrals)?  
"these are the Heisenberg matrix formalism, the Schrödinger formalism associated with the concept of the wave function, and the Feynman method of path integration. In my opinion, only the first two methods are related to reality. Both the wave function and the operators have referents in being, in contrast to the concept of a path, if we consider QM, and not classical physics. "A. Y. Sevalnikov  
The probability amplitude and its complex phase can be considered as a numerical measure of the propensity of each possible state or event of history to go into actuality. This measure does not have an independent ontological
status that only predisposition possesses. V. E. Terekhovich  
  
The state vector most adequately describes the existence of quantum objects. A package of alternatives is used to describe the basic states. Each class object in this package has attributes/operations with the same name. A mixing class (state vector) that is a descendant of all alternatives package classes (multiple inheritance) resolves name conflicts according to the "quantum rule", i.e. by means of the squared modulus of the amplitudes of the basic states.  
The description of E. Schrödinger (wave function) corresponds attributes  with the same name in a package of alternatives.  
The description of W. Heisenberg (transition matrix) corresponds  operations with the same name in a package of alternatives.  
The formalism of the Feynman integral corresponds to another way of describing the effects - the coincidence of the pattern of the "Decorator" construction.
  
### 4. Does the classical world emerge from the quantum world, and if so, how?  
"Yes, the classical world emerges from the quantum..."
In this item I am in opposition to the positive attitude of many physicists, which most clearly
expressed by Feynman. He argued: "There is one world, and it is quantum!" This
wrong. A. Yu. Sevalnikov  
Perhaps the potential modus of existence is the area where something (actual) is born out of nothing. V. E. Terekhovich  
  
The classical world emerges from the quantum world. Frame networks for both classical and quantum systems are very similar. The classic models do not have a package of alternatives. Quantum effects appear only where there are name conflicts in multiple inheritance. In classical models, the collapse of the wave function is usually left behind the scenes, in the <<Context>> constructor.  
  
However, you can conduct such an experiment - take one qubit (this is a quantum system of one qubit), and then gradually add qubits. The qubits themselves are instance-objects, the alternatives are combinations of an instance-object states.  At some point, the system becomes clasical object, and we must work with an instance-object. Where this border lies and what the nature of this border is is not clear.
Note that if a system has a classical object, then all its elements are also classical objects. But if we try to extract one of the elements, it will become a quantum object.  
  
It is wrong to say that a quantum particle is located at all points in space. We can say that a quantum particle is outside the physical space. Yes, one can agree that particles arise in space.  
Moreover, the very space for particles (systems) appears at the moment of collapse. This is because the alternative classes have <<Category>> as their superclass.  
Consider an experiment with entangled particles. The experimental device has its own space. Alice and Bob are in this space. Once Alice makes a measurement, the Mix class produces an instance that has its own space. Particles are localized at the extreme points of this space. There is nothing strange here, because and in the classical case is modeled by the space of a hierarchical structure, where subsystems has their space.  
Nonlocality is modeled globally, to what is available to Alice and Bob. This point is not entirely clear - the global variable does not belong to US space either. Perhaps there are other solutions.  
Note that the solution of natural space is at the next level of abstraction, in the Composite class (<<Category>>).
So, we assume that part of reality is outside the physical space.  
Nevertheless, it is really worth separating the quantum world and the classical world, since the models work with class objects and instance objects.  
  
### 5. In what space do state vectors exist (superposition)?  
One can imagine how space-time, while remaining a metric background for
objects and events exclusively in the actual mode of existence, itself arises
as a result of summing up a set of possible events (relationships, interactions),
occurring in the potential mode. At the same time, the emerging actual
space-time does not become any substance at all. V. E. Terekhovich   
  
In our opinion, here it is necessary to talk about ways to access the object, and only then, about space.  
Our models use a dynamic list in the <<Category>>Composite  class to model the physical space. We will understand the physical space as a container for objects. To get access to an instance object, it is enough to look through all the cells of this container. In general, the physical space is a hierarchical structure that unites the own spaces of the context, system and subsystems. There is access between all elements of this structure.  
The momentum space also exists and is defined in the <<Substance>> abstract class as a dynamic list, but no longer as a container.
The quantum object is accessed through the device (<<System>>). Double-slit experiment, Heisenberg box. Thus, we can talk about a pair of quantum object-classical object. In practice, this means that a special fixture-level attribute must be introduced containing a pointer to the mixing class. The mixing class has access to superclasses (package of alternatives), references to which are stored in a "Set", possibly a "List".  
Those. we claim that Hilbert space exists, but not in physical space.  
  
Note that pair container are well known: they are a "Map" or "Dictonary" structure. Note that in Python, classes are also stored in "Dictonary" because they are called by name.    
  
### 6. At what time do state vectors (superposition) exist?  
Metric time is used to synchronize events, determine their order
and measuring the intervals between them. Development time, on the contrary, is used as a measure of the variability of complex systems (quantum, classical, biological, and others), regardless of their relative motion in space.  
"Given the use of a two-mode model of existence, it is possible that one more aspect of time will have to be introduced. ... The time of change of the potential states themselves. V. E. Terekhovich"  
  
UML SP uses development time - the <<Exist>> Run() operation. This operation is performed sequentially (using the Single Threaded Execution pattern) starting from the context to atomic objects and back to the context. Metric time is used to record results, as needed.  
In quantum models, for this purpose we introduce a class operation with the <<Exist>> cRun(), which however is called from the run time of the device evolution. That is, if class objects are outside the physical space, then time goes the same for both class-objects and instance-objects.  
