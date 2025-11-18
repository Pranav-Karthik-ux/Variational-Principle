# Variational Principle Applied to the Quantum Harmonic Oscillator
![Graph energy vs parameter ](graph.png)

This project demonstrates how the **variational principle** can be used to approximate the  
**ground state energy** of the **quantum harmonic oscillator (QHO)** using a Gaussian trial wavefunction.  
Symbolic integration is performed to compute the energy expectation value, and the result  
is plotted as a function of the variational parameter.

---
## 📘 Theory Overview

### 🔹 Variational Principle

The variational principle states that for any normalized trial wavefunction  
$\psi(x; a)$  
depending on a parameter $a$, the expectation value of the energy satisfies:

$$
E(a) = 
\frac{\langle \psi(a) | \hat{H} | \psi(a) \rangle}
{\langle \psi(a) | \psi(a) \rangle}
\ge E_0 ,
$$

where $E_0$ is the true ground-state energy.  
Minimizing $E(a)$ gives the closest approximation to the ground-state energy  
within the chosen trial family.

---

## 🔹 Quantum Harmonic Oscillator

The Hamiltonian of the one-dimensional harmonic oscillator is:

$$
\hat{H} = 
- \frac{\hbar^2}{2m} \frac{d^2}{dx^2}
+ \frac12 m\omega^2 x^2 .
$$

The exact ground-state energy is:

$$
E_0 = \frac12 \hbar\omega .
$$

The exact ground-state wavefunction is a Gaussian, which makes the variational method especially effective with a Gaussian trial function.

---

## 🔹 Trial Wavefunction

The chosen trial wavefunction is:

$$
\psi(x;a) = e^{-a x^2},
$$

where $a$ is the variational parameter to be optimized.

From this wavefunction, the following quantities are computed:

### **Kinetic energy**
$$
T(a) = 
- \frac{\hbar^2}{2m}
\int \psi(x;a)\, \psi''(x;a)\, dx
$$

### **Potential energy**
$$
V(a) =
\frac12 m\omega^2
\int x^2 \psi(x;a)^2 \, dx
$$

### **Normalization**
$$
N(a) = 
\int \psi(x;a)^2 dx
$$

### **Total variational energy**
$$
E(a) = 
\frac{T(a) + V(a)}{N(a)} .
$$

The value of $a$ that minimizes $E(a)$ gives the best approximation to the ground-state energy.

---

## 📊 What the Program Does

The script:

1. Defines the Gaussian trial wavefunction  
2. Computes the kinetic energy, potential energy, and normalization integrals symbolically  
3. Simplifies the full expression for the expectation value $E(a)$  
4. Evaluates $E(a)$ numerically over a range of values of $a$  
5. Produces a plot of $E(a)$ vs. $a$  
6. Shows that the minimum occurs at  
   $$
   E_{\text{min}} = \frac12
   $$  
   when $\hbar = m = \omega = 1$.

---

## 📦 Requirements

Install required packages:

```bash
pip install sympy numpy matplotlib
