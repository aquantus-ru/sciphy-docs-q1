# Chapter 12: Water, Resonance, and Dielectric Response

## 12.1 Electric Dipoles in Water

Water ($H_2O$) is a polar molecule with a permanent electric dipole moment $p$.
*   Oxygen: $\delta-$
*   Hydrogen: $\delta+$

In an electric field $\vec{E}$, the dipole experiences a torque $\vec{\tau} = \vec{p} \times \vec{E}$, tending to align it with the field.

## 12.2 Dielectric Polarization

**Polarization ($\vec{P}$):** Dipole moment per unit volume.
$$ \vec{P} = \chi_e \epsilon_0 \vec{E} $$
**Displacement Field ($\vec{D}$):**
$$ \vec{D} = \epsilon_0 \vec{E} + \vec{P} = \epsilon \vec{E} $$
where $\epsilon = \epsilon_0 (1 + \chi_e)$ is the permittivity.

## 12.3 Frequency Dependence and Debye Relaxation

The ability of dipoles to follow an oscillating field depends on frequency.
*   **Low Freq:** Dipoles track the field perfectly. High $\epsilon$.
*   **High Freq:** Inertia/viscosity prevents tracking. Low $\epsilon$.

**Debye Relaxation Model:**
Describes complex permittivity $\epsilon(\omega)$:
$$ \epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + i\omega\tau} $$
*   $\epsilon_s$: Static permittivity (low freq).
*   $\epsilon_\infty$: High-frequency limit.
*   $\tau$: Relaxation time.

## 12.4 Complex Permittivity and Loss

Separating into real and imaginary parts: $\epsilon = \epsilon' - i\epsilon''$.
$$ \epsilon' = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + (\omega\tau)^2} \quad \text{(Storage)} $$
$$ \epsilon'' = \frac{(\epsilon_s - \epsilon_\infty)\omega\tau}{1 + (\omega\tau)^2} \quad \text{(Loss)} $$

**Dielectric Loss:**
Power dissipated as heat density ($W/m^3$):
$$ P_{loss} = \frac{1}{2} \omega \epsilon'' |E|^2 $$
This peak loss occurs when $\omega \tau = 1$ (resonance-like behavior).
*   For water at $25^\circ C$, relaxation freq $\approx 20\,GHz$.
*   Microwave ovens operate at $2.45\,GHz$ (wing of the absorption curve) to ensure penetration depth while heating.

---

## Dictionary of Terms

*   **Complex Permittivity:** A measure of how a material affects and is affected by an electric field, including both energy storage and energy dissipation.
*   **Debye Relaxation:** The dielectric relaxation response of an ideal, non-interacting population of dipoles to an alternating external electric field.
*   **Dielectric:** An electrical insulator that can be polarized by an applied electric field.
*   **Dipole Moment:** A measure of the separation of positive and negative electrical charges within a system.
*   **Loss Tangent ($\tan \delta$):** The ratio of the imaginary part to the real part of the permittivity ($\epsilon'' / \epsilon'$).
*   **Polarization:** The density of permanent or induced electric dipole moments in a dielectric material.
*   **Relaxation Time:** The time required for a system to return to equilibrium after a disturbance.
