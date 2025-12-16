# Chapter 10: Quantum Mechanics Fundamentals

## 10.1 Wave-Particle Duality

Matter exhibits both wave-like and particle-like properties.
*   **De Broglie Wavelength:** Associated with a particle of momentum $p$.
    $$ \lambda = \frac{h}{p} $$
*   **Heisenberg Uncertainty Principle:** Fundamental limit to precision.
    $$ \Delta x \Delta p \ge \frac{\hbar}{2} $$
    $$ \Delta E \Delta t \ge \frac{\hbar}{2} $$

## 10.2 The Wavefunction ($\Psi$)

The state of a system is described by $\Psi(x,t)$.
*   **Born Rule:** The probability density is $|\Psi|^2$.
    $$ P(a < x < b) = \int_a^b \Psi^* \Psi \, dx $$
*   **Normalization:** Total probability is 1. $\int_{-\infty}^\infty |\Psi|^2 dx = 1$.

## 10.3 The Schrödinger Equation

Describes the time evolution of the wavefunction.

**Time-Dependent:**
$$ i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi $$
where $\hat{H}$ is the Hamiltonian operator ($\hat{H} = \hat{K} + \hat{V}$).

**Time-Independent (Stationary States):**
$$ \hat{H} \psi = E \psi $$
$$ -\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + V(x)\psi = E\psi $$

## 10.4 Particle in a Box (Infinite Potential Well)

A particle confined to $0 < x < L$ with $V(x)=0$ inside and $V(x)=\infty$ outside.
*   Boundary conditions: $\psi(0) = \psi(L) = 0$.
*   Solutions:
    $$ \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) $$
*   Energy Levels:
    $$ E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2} $$
    $n = 1, 2, 3...$. Energy is quantized and non-zero (Zero Point Energy).

## 10.5 Operators and Observables

In Quantum Mechanics, physical quantities are operators acting on $\Psi$.

| Observable | Operator |
| :--- | :--- |
| Position | $\hat{x} = x$ |
| Momentum | $\hat{p} = -i\hbar \frac{\partial}{\partial x}$ |
| Energy | $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V$ |

**Expectation Value:** The average of many measurements.
$$ \langle A \rangle = \int \Psi^* \hat{A} \Psi \, dx $$

---

## Dictionary of Terms

*   **Born Rule:** A postulate stating that probability density is proportional to the square of the magnitude of the wavefunction.
*   **De Broglie Wavelength:** The wavelength associated with a massive particle, inversely proportional to its momentum.
*   **Eigenstate:** A state vector that is unchanged by a transformation (operator), except by a scalar multiplication.
*   **Eigenvalue:** The scalar multiplier associated with an eigenstate.
*   **Hamiltonian:** The operator corresponding to the total energy of the system.
*   **Heisenberg Uncertainty Principle:** A limit on the precision with which certain pairs of physical properties, such as position and momentum, can be known.
*   **Operator:** A mathematical instruction to perform an operation (like differentiation) on a function.
*   **Wavefunction:** A mathematical description of the quantum state of an isolated quantum system.
*   **Zero-Point Energy:** The lowest possible energy that a quantum mechanical physical system may have.
