# Chapter 1: Foundations of Physical Description

## 1.1 Physical Quantities and Measurement

Physics is the empirical study of the universe, relying on the measurement of physical quantities to formulate laws. A **physical quantity** is a property of a material or system that can be quantified by measurement.

### Base vs. Derived Quantities

The International System of Units (SI) is built on seven **base quantities**, which are assumed to be independent:

| Base Quantity | SI Unit | Symbol |
| :--- | :--- | :--- |
| Length | meter | $m$ |
| Mass | kilogram | $kg$ |
| Time | second | $s$ |
| Electric Current | ampere | $A$ |
| Thermodynamic Temperature | kelvin | $K$ |
| Amount of Substance | mole | $mol$ |
| Luminous Intensity | candela | $cd$ |

**Derived quantities** are constructed from these base units. For example:
*   **Force ($F$):** Defined by Newton's Second Law. $F = ma \implies [M][L][T]^{-2}$. Unit: Newton ($N = kg \cdot m/s^2$).
*   **Energy ($E$):** Capacity to do work. $E = Fd \implies [M][L]^2[T]^{-2}$. Unit: Joule ($J = N \cdot m$).

## 1.2 Units and Dimensional Analysis

**Dimensional Analysis** is a method used to understand the relationships between physical quantities and to verify the consistency of equations. An equation is only physically valid if it is **dimensionally homogeneous**, meaning the dimensions on both sides of the equality are identical.

### Example: The Period of a Pendulum
Let us verify the formula for the period $T$ of a simple pendulum:
$$ T = 2\pi \sqrt{\frac{L}{g}} $$

*   Dimension of Time ($T$): $[T]$
*   Dimension of Length ($L$): $[L]$
*   Dimension of Acceleration ($g$): $[L][T]^{-2}$

Substituting into the RHS:
$$ \sqrt{\frac{[L]}{[L][T]^{-2}}} = \sqrt{\frac{1}{[T]^{-2}}} = \sqrt{[T]^2} = [T] $$
The dimensions match, confirming the equation's structural validity.

## 1.3 Scalars and Vectors

Physical quantities are divided into two categories based on directionality.

### Scalars
Scalars are quantities fully described by a magnitude (and unit) alone.
*   *Examples:* Mass, temperature, time, density, volume.
*   *Arithmetic:* Follow standard algebraic rules (e.g., $5\,s + 2\,s = 7\,s$).

### Vectors
Vectors possess both **magnitude** and **direction**.
*   *Examples:* Displacement, velocity, force, momentum, electric field.
*   *Notation:* $\vec{v}$ or $\mathbf{v}$. Magnitude is denoted $|\vec{v}|$ or $v$.

### Vector Algebra

**1. Vector Addition:**
Vectors add geometrically (tip-to-tail method). In component form:
$$ \vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} + (A_z + B_z)\hat{k} $$

**2. Dot Product (Scalar Product):**
Measures how much one vector goes in the direction of another.
$$ \vec{A} \cdot \vec{B} = |\vec{A}| |\vec{B}| \cos \theta $$
Result is a scalar. Used in calculating Work ($W = \vec{F} \cdot \vec{d}$).

**3. Cross Product (Vector Product):**
Produces a vector perpendicular to the plane formed by two vectors.
$$ |\vec{A} \times \vec{B}| = |\vec{A}| |\vec{B}| \sin \theta $$
Direction is determined by the right-hand rule. Used in Torque ($\vec{\tau} = \vec{r} \times \vec{F}$) and Magnetic Force.

## 1.4 Measurement Limits and Uncertainty

No experiment yields a "perfect" value. All measurements have an associated **uncertainty**.

### Precision vs. Accuracy
*   **Accuracy:** Closeness to the true or theoretical value.
*   **Precision:** Reproducibility of the measurement (spread of values).

### Propagation of Uncertainty
If $x = A \pm \delta A$ and $y = B \pm \delta B$:
*   **Addition ($z = x + y$):** $\delta z = \sqrt{(\delta A)^2 + (\delta B)^2}$ (assuming independent errors).
*   **Multiplication ($z = x \cdot y$):** Fractional uncertainties add in quadrature:
    $$ \frac{\delta z}{z} = \sqrt{\left(\frac{\delta A}{A}\right)^2 + \left(\frac{\delta B}{B}\right)^2} $$

## 1.5 Models and Idealizations

Physics uses **models** to approximate reality. A model captures the essential features of a system while ignoring negligible factors.

*   **Point Mass:** Ignores shape and rotation, treating an object as a single point at its center of mass.
*   **Ideal Gas:** Ignores intermolecular forces and particle volume. Valid at high temperatures and low pressures.
*   **Inextensible String:** Assumes a string has constant length (does not stretch), simplifying tension problems.

Understanding the *regime of validity* is crucial. For instance, Ohm's Law ($V=IR$) is a model for conduction that fails in semiconductors or at high temperatures.

---

## Dictionary of Terms

*   **Dimensional Analysis:** A mathematical technique used to check the consistency of equations by comparing the physical dimensions of the terms.
*   **Dot Product:** An algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number.
*   **Inertial Frame:** A reference frame in which an object stays at rest or moves at a constant velocity unless acted upon by a force.
*   **Magnitude:** The size or quantity of a physical property, ignoring direction.
*   **Precision:** The degree to which repeated measurements under unchanged conditions show the same results.
*   **Scalar:** A quantity that is fully described by a magnitude alone.
*   **Significant Figures:** Digits in a number that carry meaningful information about its precision.
*   **Systematic Error:** A consistent, repeatable error associated with faulty equipment or a flawed experiment design.
*   **Unit Vector:** A vector of length 1, used to specify a spatial direction (e.g., $\hat{i}, \hat{j}, \hat{k}$).
*   **Vector:** A quantity that has both magnitude and direction.
