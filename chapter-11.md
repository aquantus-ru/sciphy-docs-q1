# Chapter 11: Magnetic Resonance (NMR / MR)

## 11.1 Magnetization and Precession

Consider a sample of spins (protons) in a static field $\vec{B}_0 = B_0 \hat{z}$.
1.  **Net Magnetization ($M_0$):** Excess spins align with $B_0$.
2.  **Torque:** $\vec{\tau} = \vec{M} \times \vec{B}$.
3.  **Equation of Motion:**
    $$ \frac{d\vec{M}}{dt} = \gamma \vec{M} \times \vec{B} $$
This describes **Larmor Precession** around the z-axis at angular frequency $\omega_0 = \gamma B_0$.

## 11.2 The Rotating Frame

To simplify analysis, we transform to a frame rotating at the Larmor frequency.
*   **Lab Frame:** $\vec{M}$ spirals.
*   **Rotating Frame:** $\vec{M}$ appears stationary (effectively $\vec{B}_{eff} \approx 0$).

## 11.3 RF Excitation ($B_1$ Field)

We apply an oscillating magnetic field $\vec{B}_1$ perpendicular to $B_0$. In the rotating frame, $B_1$ is constant along the x'-axis.
*   $\vec{M}$ precesses around $\vec{B}_1$.
*   **Flip Angle ($\alpha$):**
    $$ \alpha = \gamma B_1 \tau $$
    where $\tau$ is pulse duration.
*   **90° Pulse:** Tips $M_z$ fully into the transverse plane ($M_{xy}$), maximizing signal.

## 11.4 Relaxation Mechanisms

Once disturbed, the system returns to equilibrium.

### T1: Spin-Lattice Relaxation (Longitudinal)
Regrowth of $M_z$. Energy transfer to surroundings (lattice).
$$ \frac{dM_z}{dt} = \frac{M_0 - M_z}{T_1} $$
Solution: $M_z(t) = M_0 (1 - e^{-t/T_1})$ (from saturation).

### T2: Spin-Spin Relaxation (Transverse)
Decay of $M_{xy}$. Loss of phase coherence due to spin interactions.
$$ \frac{dM_{xy}}{dt} = -\frac{M_{xy}}{T_2} $$
Solution: $M_{xy}(t) = M_{xy}(0) e^{-t/T_2}$.
Always $T_2 \le T_1$.

## 11.5 The Bloch Equations

Phenomenological equations combining precession and relaxation:
$$ \frac{dM_x}{dt} = \gamma (M_y B_0 - M_z B_y) - \frac{M_x}{T_2} $$
$$ \frac{dM_y}{dt} = \gamma (M_z B_x - M_x B_0) - \frac{M_y}{T_2} $$
$$ \frac{dM_z}{dt} = \gamma (M_x B_y - M_y B_x) + \frac{M_0 - M_z}{T_1} $$

---

## Dictionary of Terms

*   **Bloch Equations:** A set of macroscopic equations that calculate the nuclear magnetization $M$ as a function of time when relaxation times $T_1$ and $T_2$ are present.
*   **Flip Angle:** The angle to which the net magnetization is rotated relative to the main magnetic field direction.
*   **Larmor Frequency:** The rate of precession of the magnetic moment of a proton around an external magnetic field.
*   **Longitudinal Magnetization ($M_z$):** The component of the magnetization vector parallel to the static magnetic field.
*   **Precession:** A change in the orientation of the rotational axis of a rotating body.
*   **Radio Frequency (RF) Pulse:** A burst of electromagnetic wave used to excite the nuclei.
*   **Rotating Frame:** A coordinate system that rotates around the z-axis at the Larmor frequency, simplifying the description of magnetic resonance.
*   **T1 Relaxation:** The time constant for the recovery of longitudinal magnetization.
*   **T2 Relaxation:** The time constant for the decay of transverse magnetization.
*   **Transverse Magnetization ($M_{xy}$):** The component of the magnetization vector perpendicular to the static magnetic field.
