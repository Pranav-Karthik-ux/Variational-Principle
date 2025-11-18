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
\[
\psi(x; a),
\]  
depending on a parameter \(a\), the energy expectation value satisfies:

\[
E(a) = 
\frac{\langle \psi(a) | \hat{H} | \psi(a) \rangle}
{\langle \psi(a) | \psi(a) \rangle}
\ge E_0,
\]

where \(E_0\) is the true ground state energy.  
By **minimizing \(E(a)\)**, we obtain the best possible approximation to the ground-state energy within the chosen trial family.

---

## 🔹 Quantum Harmonic Oscillator

The Hamiltonian of the one-dimensional QHO is:

\[
\hat{H} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}
+ \frac12 m\omega^2 x^2.
\]

Its exact ground-state energy is:

\[
E_0 = \frac12 \hbar\omega.
\]

The exact ground-state wavefunction is a Gaussian, which makes the variational method using  
a Gaussian trial function especially effective.

---

## 🔹 Trial Wavefunction

The chosen trial wavefunction is:

\[
\psi(x; a) = e^{-a x^2}, 
\]

where \( a \) is the variational parameter to be optimized. The wave function could be changed without altering the code.

From this wavefunction, the following integrals are computed:

- **Kinetic energy:**
  \[
  T(a) = -\frac{\hbar^2}{2m}
  \int \psi(x;a) \, \psi''(x;a)\, dx
  \]

- **Potential energy:**
  \[
  V(a) =
  \frac12 m\omega^2
  \int x^2 \psi(x;a)^2 \, dx
  \]

- **Normalization:**
  \[
  N(a) = \int \psi(x;a)^2 \, dx
  \]

- **Total variational energy:**
  \[
  E(a) = \frac{T(a) + V(a)}{N(a)}.
  \]

The goal is to find the value of \(a\) that minimizes \(E(a)\).

---

## 📊 What the Program Does

The script:

1. Defines the Gaussian trial wavefunction  
2. Symbolically calculates:
   - The second derivative  
   - Kinetic and potential energy integrals  
   - Normalization integral  
   - Total energy expression  
3. Evaluates the energy numerically for a range of values of the parameter \(a\)  
4. Produces a plot of the variational energy as a function of \(a\)  
5. Shows that the energy reaches a minimum at  
   \[
   E_{\text{min}} = \frac12
   \]  
   (for \( \hbar = m = \omega = 1 \)), which matches the exact ground-state energy.

---

## 📦 Requirements

Install required packages:

```bash
pip install sympy numpy matplotlib
