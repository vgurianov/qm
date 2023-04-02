# Ontological description of quantum mechanics
This resource contains software for the work [Gurianov, V.I. (2023). Simulation of Certain Quantum Effects. Cambridge Open Engage. doi:10.33774/coe-2023-v5sc8 ](https://www.cambridge.org/engage/coe/article-details/6401b76a37e01856dc125cda).This content is a preprint and has not been peer-reviewed.    

## 1. Description key points 
An ontological description of quantum mechanics is necessary to build a conceptual model of Multi-Agent Systems (MAS) in the field of nanotechnology. This resource provides a description of the basic principles for constructing such ontologies.  
Quantum effects may be described as follows.

 * Wave function analog is a class.
 * A wave function collapse analog is to run constructor of the class and create instance of the class.
 * A quantum superposition analog is multiple inheritance. If the classes have attributes or operations with an identical name then multiple inheritance have a conflict of names. In this conflict, we will resolve the ”quantum rule”, i.e. using an amplitude of wave function. We note right away that complex numbers can be eliminated by replacing them with objects constructions. 

## 2. Simulation language  

To describe scientific models, we will use the language of object-oriented simulation [UML2 SP](https://vgurianov.github.io/uml-sp/). This language is a profile of UML and is an object oriented version of the well-known IDEF0 (SADT) methodology. The semantic network is built from frames, which are the ”class” UML-element. Each frame is tagged ”Concept”. This tagged value is assigned a specific concept, which allows the building of a conceptual model of the problem domain. 


## 3. Site Overview
In sections "1.Key points" and "2. Main quantum effects", an extended description of the quantum effects is given, documentation for the software is presented, and experimental results are presented. The simulation software is implemented in Python 3.  

The resource also discusses some additional issues of quantum theory in section "3. Other quantum models".  

An ontology for the Reseford scattering for the quantum and classical cases is considered. Both ontologies are compared. It is shown how the transition from the quantum case to the classical case occurs. The definition of spin by means of semantic networks is given. For this purpose, an analogue of the fibred space for spin 1/2 is used.  

R.Feynman showed that a classical Turing machine would not be able to simulate a quantum effect. In subsection "Turing machine", we considered this issue.  

In subsection  "Non-numerical model" is proposed and considered model without complex numbers. An ordered pair of looped lists is used to eliminate complex numbers. The main processes with this data structure are defined. Based on this construction, a Hilbert’s space model is constructed. A model for the collapse of the wave function is proposed. The processes that are described by the time-independent and time-dependent Schrodinger equations are considered.The problem of space
and time in quantum mechanics is considered.  
This model gives an idea of what a more detailed quantum mechanics model might look like. In particular, this model answers the question "What happens in the quantum world when we do not observe it?". 
