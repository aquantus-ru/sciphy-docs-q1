# Chapter 14: Statistical & Thermal Physics

## 14.1 The Statistical Basis of Thermodynamics

Thermodynamics describes macroscopic systems; Statistical Mechanics explains them via microscopic averages.

### Microstates and Macrostates
*   **Microstate:** A specific configuration of all particle positions/momenta.
*   **Macrostate:** Defined by macroscopic variables ($P, V, T, N$).
*   **Entropy ($S$):** Measure of the number of microstates ($\Omega$) accessible to a macrostate.
    $$ S = k_B \ln \Omega $$

## 14.2 The Boltzmann Distribution

For a system in thermal equilibrium at temperature $T$, the probability $P_i$ of being in a state with energy $E_i$ is:
$$ P_i = \frac{1}{Z} e^{-E_i / k_B T} $$

**Partition Function ($Z$):** Normalization factor.
$$ Z = \sum_i e^{-E_i / k_B T} $$
All thermodynamic quantities can be derived from $Z$.
*   Free Energy: $F = -k_B T \ln Z$.
*   Average Energy: $\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta}$ (where $\beta = 1/k_B T$).

## 14.3 Applications

### 1. Two-Level System (Spin 1/2 in B-field)
Energies $E_+ = -\mu B$ and $E_- = +\mu B$.
$$ Z = e^{\mu B \beta} + e^{-\mu B \beta} = 2 \cosh(\mu B \beta) $$
Population Ratio:
$$ \frac{N_-}{N_+} = e^{-(E_- - E_+)/k_B T} = e^{-2\mu B / k_B T} $$
At room temp ($T \approx 300K$) and typical fields, this ratio is $\approx 0.99999$. This tiny excess in $N_+$ provides the NMR signal.

### 2. Maxwell-Boltzmann Speed Distribution
For an ideal gas:
$$ f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 e^{-mv^2/2k_B T} $$
Average Kinetic Energy:
$$ \langle K \rangle = \frac{3}{2} k_B T $$

## 14.4 Relaxation to Equilibrium

If a system is perturbed, it relaxes back to the Boltzmann distribution.
**Linear approximation:**
$$ \frac{dP}{dt} = - \frac{P - P_{eq}}{\tau} $$
where $\tau$ is the relaxation time constant.

---

## Dictionary of Terms

*   **Boltzmann Constant ($k_B$):** A physical constant relating the average kinetic energy of particles in a gas with the temperature of the gas.
*   **Boltzmann Distribution:** A probability distribution that gives the probability that a system will be in a certain state as a function of that state's energy and the temperature of the system.
*   **Entropy:** A thermodynamic quantity representing the unavailability of a system's thermal energy for conversion into mechanical work, often interpreted as the degree of disorder or randomness in the system.
*   **Macrostate:** The state of a system defined by macroscopic properties such as temperature, pressure, and volume.
*   **Microstate:** A specific detailed microscopic configuration of a system.
*   **Partition Function:** A function that describes the statistical properties of a system in thermodynamic equilibrium.
*   **Thermal Equilibrium:** The state in which two substances in physical contact with each other exchange no heat energy.
