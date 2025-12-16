# Chapter 3: Forces and Classical Dynamics

## 3.1 Newton's Laws of Motion

Dynamics connects motion to its causes (forces).

### 1. Newton's First Law (Inertia)
A body continues in its state of rest or uniform motion in a straight line unless acted upon by a net external force.
*   **Inertia:** The resistance of an object to changes in its motion. Mass is the quantitative measure of inertia.

### 2. Newton's Second Law
The rate of change of momentum is proportional to the applied force.
$$ \vec{F}_{net} = \frac{d\vec{p}}{dt} $$
For constant mass, $\vec{p} = m\vec{v}$, so:
$$ \vec{F}_{net} = m \vec{a} $$
This is a vector equation: $\sum F_x = ma_x$, $\sum F_y = ma_y$.

### 3. Newton's Third Law
For every action, there is an equal and opposite reaction.
$$ \vec{F}_{AB} = - \vec{F}_{BA} $$
*   Forces always exist in pairs.
*   Action and reaction forces act on **different** objects.

## 3.2 Types of Forces

1.  **Gravity ($F_g$):** $F_g = mg$ (near Earth).
2.  **Normal Force ($N$):** A contact force perpendicular to the surface. It prevents objects from passing through each other. It is not a fixed value but adjusts to balance other forces (up to the breaking point).
3.  **Tension ($T$):** The force transmitted through a string, rope, or cable. Ideally, tension is uniform throughout the string.
4.  **Friction ($f$):** Opposes relative motion between surfaces.

### Friction Details
*   **Static Friction ($f_s$):** Prevents motion from starting. Acts in direction opposite to potential motion.
    $$ f_s \le \mu_s N $$
    where $\mu_s$ is the coefficient of static friction.
*   **Kinetic Friction ($f_k$):** Opposes motion while moving.
    $$ f_k = \mu_k N $$
    Typically, $\mu_k < \mu_s$.

## 3.3 Free-Body Diagrams (FBD)

Solving dynamics problems requires isolating the object of interest and drawing all external forces acting *on* it.

**Steps:**
1.  Draw the object as a dot or box.
2.  Identify all forces (Gravity, Normal, Friction, Applied).
3.  Draw vectors originating from the object.
4.  Define a coordinate system (often aligning one axis with the acceleration).
5.  Apply $\sum \vec{F} = m\vec{a}$.

## 3.4 Circular Motion Dynamics

For an object moving in a circle of radius $r$ at speed $v$, the acceleration is **centripetal** (directed toward the center):
$$ a_c = \frac{v^2}{r} $$
Thus, a net force must point toward the center:
$$ \sum F_{radial} = m \frac{v^2}{r} $$

*   *Example:* A car turning on a flat road. Friction provides the centripetal force: $f_s = mv^2/r$.
*   *Example:* A banked curve. The normal force component provides the centripetal force.

## 3.5 Connected Bodies

When two masses are connected (e.g., by a pulley), they often share kinematic constraints.
*   **Atwood Machine:** Two masses $m_1, m_2$ hanging over a pulley.
    *   Constraint: magnitude of acceleration $a$ is same for both.
    *   Equations:
        1.  $T - m_1 g = m_1 a$
        2.  $m_2 g - T = m_2 a$
    *   Solution: $a = g \frac{m_2 - m_1}{m_1 + m_2}$.

---

## Dictionary of Terms

*   **Action-Reaction Pair:** Two forces that are equal in magnitude and opposite in direction, acting on two different interacting objects.
*   **Coefficient of Friction:** A scalar value ($\mu$) describing the ratio of the force of friction between two bodies and the force pressing them together.
*   **Dynamics:** The branch of mechanics concerned with the forces that cause or affect motion.
*   **Equilibrium:** A state in which the net force on an object is zero ($\vec{a} = 0$).
*   **Force:** An interaction that, when unopposed, will change the motion of an object.
*   **Free-Body Diagram:** A graphical illustration used to visualize the applied forces and moments on a body.
*   **Inertia:** The tendency of an object to resist changes in its state of motion.
*   **Net Force:** The vector sum of all forces acting on an object.
*   **Normal Force:** The support force exerted upon an object that is in contact with another stable object.
*   **Weight:** The force of gravity on an object ($W = mg$).
