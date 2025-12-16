# Chapter 4: Energy, Work, and Conservation

## 4.1 Work

In physics, **Work** is a measure of energy transfer that occurs when an object is moved over a distance by an external force.

### Definition
For a constant force $\vec{F}$ and displacement $\vec{d}$:
$$ W = \vec{F} \cdot \vec{d} = F d \cos \theta $$
For a variable force, work is the line integral:
$$ W = \int_{\vec{x}_i}^{\vec{x}_f} \vec{F}(\vec{x}) \cdot d\vec{x} $$

*   $W > 0$: Force adds energy (speeds up).
*   $W < 0$: Force removes energy (slows down, e.g., friction).
*   $W = 0$: Force is perpendicular to displacement (e.g., centripetal force).

## 4.2 Kinetic Energy and the Work-Energy Theorem

**Kinetic Energy ($K$)** is the energy of motion:
$$ K = \frac{1}{2} m v^2 $$

**Work-Energy Theorem:**
The net work done on an object equals the change in its kinetic energy.
$$ W_{net} = \Delta K = K_f - K_i $$

*Proof (1D):*
$$ W = \int F dx = \int m a dx = \int m \frac{dv}{dt} dx = \int m \frac{dv}{dx} \frac{dx}{dt} dx = \int m v dv $$
$$ W = \left[ \frac{1}{2} m v^2 \right]_{v_i}^{v_f} = \Delta K $$

## 4.3 Potential Energy

**Potential Energy ($U$)** is stored energy associated with the configuration of a system involving conservative forces.

*   **Conservative Forces:** Work done depends only on endpoints, not the path (e.g., Gravity, Electrostatics, Springs).
*   **Relation to Force:**
    $$ F(x) = - \frac{dU}{dx} $$

### Forms of Potential Energy
1.  **Gravitational ($U_g$):** Near Earth's surface ($h \ll R_E$).
    $$ U_g = mgh $$
2.  **Elastic ($U_s$):** Hooke's Law spring ($F = -kx$).
    $$ U_s = \frac{1}{2} k x^2 $$

## 4.4 Conservation of Energy

**Law of Conservation of Mechanical Energy:**
If only conservative forces do work, the total mechanical energy $E_{mech} = K + U$ remains constant.
$$ \Delta E_{mech} = 0 \implies K_i + U_i = K_f + U_f $$

**General Energy Conservation:**
If non-conservative forces (like friction) are present, they do work $W_{nc}$:
$$ W_{nc} = \Delta E_{mech} = (K_f + U_f) - (K_i + U_i) $$
Usually $W_{nc}$ is negative, converting mechanical energy into internal thermal energy ($Q$).

## 4.5 Power

Power is the rate at which work is done.
$$ P = \frac{dW}{dt} $$
Using $dW = \vec{F} \cdot d\vec{x}$:
$$ P = \vec{F} \cdot \frac{d\vec{x}}{dt} = \vec{F} \cdot \vec{v} $$
Unit: Watt ($1\,W = 1\,J/s$).

---

## Dictionary of Terms

*   **Conservative Force:** A force with the property that the total work done in moving a particle between two points is independent of the path taken.
*   **Elastic Potential Energy:** Potential energy stored as a result of deformation of an elastic object, such as the stretching of a spring.
*   **Energy:** A scalar physical quantity that describes the amount of work that can be performed by a force.
*   **Gravitational Potential Energy:** Energy an object possesses because of its position in a gravitational field.
*   **Joule:** The SI unit of work or energy.
*   **Kinetic Energy:** The energy that it possesses due to its motion.
*   **Mechanical Energy:** The sum of potential energy and kinetic energy.
*   **Power:** The rate at which work is performed or energy is converted.
*   **Watt:** The SI unit of power.
*   **Work:** The product of force and displacement.
