# Chapter 2: Classical Motion (Kinematics)

## 2.1 Position, Displacement, and Distance

Kinematics describes *how* objects move, without regard to the forces causing the motion.

*   **Position ($x$):** The location of a particle relative to an origin.
*   **Displacement ($\Delta x$):** The change in position. It is a vector.
    $$ \Delta \vec{x} = \vec{x}_f - \vec{x}_i $$
*   **Distance ($d$):** The total length of the path traveled. It is a scalar.

## 2.2 Velocity and Speed

### Average vs. Instantaneous Velocity
**Average Velocity** is the displacement divided by the time interval:
$$ \vec{v}_{avg} = \frac{\Delta \vec{x}}{\Delta t} $$

**Instantaneous Velocity** is the limit as the time interval approaches zero (the derivative):
$$ \vec{v}(t) = \lim_{\Delta t \to 0} \frac{\Delta \vec{x}}{\Delta t} = \frac{d\vec{x}}{dt} $$

**Speed** is the magnitude of velocity: $v = |\vec{v}|$.

## 2.3 Acceleration

Acceleration is the rate of change of velocity.
$$ \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{x}}{dt^2} $$

*   If $\vec{a}$ and $\vec{v}$ are in the same direction, the object speeds up.
*   If $\vec{a}$ and $\vec{v}$ are in opposite directions, the object slows down.
*   If $\vec{a}$ is perpendicular to $\vec{v}$, the object changes direction (e.g., circular motion).

## 2.4 Equations of Motion (Constant Acceleration)

For the specific case where acceleration $a$ is constant, we can derive the "Big Four" kinematic equations.

1.  **Velocity-Time:**
    $$ v_f = v_i + a t $$
2.  **Position-Time:**
    $$ x_f = x_i + v_i t + \frac{1}{2} a t^2 $$
3.  **Velocity-Position:**
    $$ v_f^2 = v_i^2 + 2a(x_f - x_i) $$
4.  **Average Velocity:**
    $$ x_f - x_i = \frac{1}{2}(v_i + v_f)t $$

### Derivation of Equation 2:
Start with $v(t) = v_i + at$. Integrate with respect to time:
$$ x(t) = \int (v_i + at) \, dt = v_i t + \frac{1}{2} a t^2 + C $$
At $t=0$, $x(0) = x_i$, so $C = x_i$. Thus, $x_f = x_i + v_i t + \frac{1}{2}at^2$.

## 2.5 Projectile Motion (2D Kinematics)

Projectile motion describes an object moving in two dimensions under the influence of gravity alone (ignoring air resistance). The key insight is that **horizontal and vertical motions are independent**.

*   **Horizontal ($x$):** $a_x = 0$. Velocity $v_x$ is constant.
    $$ x(t) = x_0 + v_{0x} t $$
*   **Vertical ($y$):** $a_y = -g$ (where $g \approx 9.8\, m/s^2$).
    $$ y(t) = y_0 + v_{0y} t - \frac{1}{2} g t^2 $$

**Example: Range of a Projectile**
Launched from ground ($y_0=0$) with speed $v_0$ at angle $\theta$.
1.  Flight time is determined by $y(T)=0$:
    $$ 0 = v_0 \sin\theta T - \frac{1}{2} g T^2 \implies T = \frac{2 v_0 \sin\theta}{g} $$
2.  Range $R = x(T)$:
    $$ R = (v_0 \cos\theta) T = \frac{2 v_0^2 \sin\theta \cos\theta}{g} = \frac{v_0^2 \sin(2\theta)}{g} $$
Max range occurs at $\theta = 45^\circ$.

## 2.6 Reference Frames and Relative Motion

Velocity depends on the observer. If frame $S'$ moves with velocity $\vec{v}_{S'/S}$ relative to frame $S$:
$$ \vec{v}_{obj/S} = \vec{v}_{obj/S'} + \vec{v}_{S'/S} $$

This is the **Galilean Transformation**. It holds for speeds $v \ll c$. Near the speed of light, Relativistic addition of velocities is required.

---

## Dictionary of Terms

*   **Acceleration:** The rate of change of velocity with respect to time.
*   **Displacement:** A vector quantity representing the straight-line distance and direction from an initial position to a final position.
*   **Frame of Reference:** A coordinate system used to represent and measure the position, orientation, and other properties of objects.
*   **Free Fall:** Motion under the sole influence of gravity.
*   **Instantaneous Velocity:** The velocity of an object at a specific instant in time.
*   **Kinematics:** The branch of mechanics concerned with the motion of objects without reference to the forces that cause the motion.
*   **Projectile Motion:** A form of motion where an object is thrown near the earth's surface and moves along a curved path under the action of gravity.
*   **Scalar Component:** The projection of a vector along an axis (e.g., $v_x$).
*   **Trajectory:** The path followed by a projectile flying or an object moving under the action of given forces.
*   **Vector Addition:** The operation of adding two or more vectors together into a vector sum.
