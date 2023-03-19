
# Calculation of measurement errors.    
Let n is count of measurements then the standard deviation is  
\begin{equation}  
\sigma = \sqrt{\frac{1}{n(n-1)}\sum\limits_{i=1}^{n}(\Delta x_{i})^2 },  
\end{equation}  
where  $$\Delta x_{i}=x_{i}-\overline{x}$$, $$\overline{x}$$ is the sample mean. The confidence interval is $$\Delta_{\sigma}x = t_{n,\alpha}\sigma$$, where  $$t_{n,\alpha}$$ is a Student's t distribution with n − 1 degrees of freedom, $$\alpha=0.95$$ (the 95th percentile). We use the function  stats.t.ppf((1.0 + 0.95)/2, n-1) from the 'stats' package.  
Then $$x = \overline{x} \pm \Delta_{s}x$$.
<!---
https://en.wikipedia.org/wiki/Confidence_interval#Confidence_interval_for_specific_distributions
--->  

In other denotes, the standard deviation is

$$\sigma = \sqrt{\operatorname {Var}(x_{ar}) / (n-1)}$$,  
where $$\operatorname {Var}(x_{ar})$$  is  variance and n is count of measurements.  
The confidence interval is   
$$\Delta_{\sigma}x = \sigma\overline{x}/\sqrt{n}$$ 
(for examle, see [wiki]([https://en.wikipedia.org/wiki/Confidence_interval])

Where X is the sample mean, and S2 is the sample variance. Then
has a Student's t distribution with kn − 1 degrees of freedom
Example: alfa = 0.95, from a student t = 3.18 for kn = 4; 0.95 - confidence interval , 60-1 degrees of freedom
denoting ppf as the 95th percentile of this distribution
We usage function stats.t.ppf((1 + 0.95)/2, kn-1) from scipy package (from scipy import stats)


====================
Formula

The mass-energy equivalence is described by the famous equation
$$ E=mc^2 $$
discovered in 1905 by Albert Einstein.  
In natural units ($$c = 1$$), the formula expresses the identity  

\begin{equation}
E=m
\end{equation}
Subscripts in math mode are written as $$a_b$$ and superscripts are written as $$a^b$$. These can be combined an nested to write expressions such as  

\begin{equation}
 T^{i_1 i_2 \dots i_p}{j_1 j_2 \dots j_q} = T(x^{i_1},\dots,x^{i_p},e_{j_1},\dots,e_{j_q})
\end{equation}  

We write integrals using $\int$ and fractions using $$\frac{a}{b}$$. Limits are placed on integrals using superscripts and subscripts:
\begin{equation}
\int_0^1 \frac{dx}{e^x} =  \frac{e-1}{e}
\end{equation}
Lower case Greek letters are written as $$\omega$$, $$\delta$$ etc. while upper case Greek letters are written as $$\Omega$$, $$\Delta$$.

Mathematical operators are prefixed with a backslash as $$\sin(\beta), \cos(\alpha), \log(x)$$ etc.

A quantum superposition of the "basis states"  
\begin{equation}
 |\psi\rangle = c_1|0\rangle   + c_2|1\rangle ,
\end{equation}
here $$|0\rangle$$ and $$|1\rangle$$ are the Dirac notation for the quantum state that will always give the result 0 or 1 when make a measurement.


<p><img src="qbit.png" alt="" /></p>
Figure 1: A general structure UML2 SP <br/>
----

![Image](qbit.png)
Figure 1: A general structure UML2 SP <br/>
  
  
  
Experiment result is depicted in table 2

| №   | $$AB$$   | $$BC$$  | $$AC$$   | $$N[A^+,B^+] < $$ | $$N[B^-,C^-]+N[A^+,C^+]$$ |
| --- | ---- | --- | ---- | ---------- | --------------------- |
| 1   | 240° | 60° | 300° | 15         | 11                    |
| 2   | 240° | 60° | 300° | 15         | 11                    |  

xperiment result is depicted in table

| №   | $$\mid m_1\rangle$$   |$$\mid m_2\rangle$$  | $$\mid l_1\rangle$$   | $$\mid l_1\rangle$$ | 
| --- | ---- | --- | ---- | :----------: |
| 1   | 1.0 | 0.0 | 0.497 | 0.503         | 
| 2   | 0.499 | 0.501 | 1.0 | 0.0         |  

