# Chapter 9: Nuclear Spin and Angular Momentum

## 9.1 Intrinsic Spin

Spin is an intrinsic form of angular momentum carried by elementary particles, distinct from orbital angular momentum.
*   **Fermions:** Half-integer spin ($1/2, 3/2...$). Example: Electrons, Protons, Neutrons.
*   **Bosons:** Integer spin ($0, 1, 2...$). Example: Photons.

For a particle with spin $s=1/2$, the magnitude of the spin vector $\vec{S}$ is:
$$ |\vec{S}| = \hbar \sqrt{s(s+1)} = \hbar \frac{\sqrt{3}}{2} $$
The z-component $S_z$ is quantized:
$$ S_z = m_s \hbar $$
where $m_s = \pm 1/2$.

## 9.2 Nuclear Spin ($I$)

The nucleus acts as a single entity with total angular momentum $\vec{I}$, resulting from the sum of nucleon spins and orbital angular momenta.
*   $I$ is the **Nuclear Spin Quantum Number**.
*   Number of magnetic states: $2I + 1$.

**Rules for $I$:**
1.  Even $Z$, Even $N$: $I = 0$ (e.g., $^{12}C, ^{16}O$). No magnetic moment.
2.  Odd $A$: $I$ is half-integer (e.g., $^1H, ^{13}C, ^{31}P$). Important for NMR.
3.  Odd $Z$, Odd $N$: $I$ is integer (e.g., $^2H, ^{14}N$).

## 9.3 Magnetic Moment

A nucleus with spin $I \neq 0$ has a magnetic moment $\vec{\mu}$:
$$ \vec{\mu} = \gamma \vec{I} $$
where $\gamma$ is the **Gyromagnetic Ratio**.
*   $\gamma$ is unique to each isotope.
*   For protons ($^1H$): $\gamma/2\pi = 42.58 \, MHz/T$.

## 9.4 Energy in a Magnetic Field

In an external magnetic field $\vec{B} = B_0 \hat{k}$, the Hamiltonian is:
$$ H = - \vec{\mu} \cdot \vec{B} = - \gamma I_z B_0 $$
Energy levels:
$$ E_m = - \gamma \hbar m_I B_0 $$
For $I=1/2$ (proton), there are two levels:
*   **Lower ($m_I = +1/2$):** Aligned with field (Spin Up). $E = - \frac{1}{2}\gamma\hbar B_0$.
*   **Upper ($m_I = -1/2$):** Anti-aligned (Spin Down). $E = + \frac{1}{2}\gamma\hbar B_0$.

This energy splitting is the basis of NMR and MRI.

---

## Dictionary of Terms

*   **Angular Momentum:** A vector quantity that represents the product of a body's rotational inertia and rotational velocity.
*   **Boson:** A subatomic particle, such as a photon, which has zero or integral spin.
*   **Fermion:** A subatomic particle, such as a nucleon or electron, which has half-integral spin.
*   **Gyromagnetic Ratio ($\gamma$):** The ratio of the magnetic moment to the angular momentum of a particle.
*   **Hamiltonian:** The operator corresponding to the total energy of the system.
*   **Magnetic Moment:** A vector quantity that determines the torque a material will experience in an external magnetic field.
*   **Quantization:** The concept that a physical quantity can only have certain discrete values.
*   **Spin:** An intrinsic form of angular momentum carried by elementary particles.
*   **Zeeman Effect:** The splitting of a spectral line into several components in the presence of a static magnetic field.
