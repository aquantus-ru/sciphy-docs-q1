# Chapter 13: Scattering and Interaction Types

## 13.1 Scattering Cross-Section

The probability of scattering is quantified by the **Cross-Section ($\sigma$)**.
*   Unit: Barn ($1\,b = 10^{-28} \, m^2$).
*   Total cross-section $\sigma_{total} = \sigma_{elastic} + \sigma_{inelastic} + \sigma_{absorption}$.

**Beer-Lambert Law:**
Intensity attenuation through a medium of density $n$:
$$ I(x) = I_0 e^{-n \sigma x} $$

## 13.2 Elastic Scattering

Energy is conserved; only direction changes.

### Rayleigh Scattering
Scattering of light by particles much smaller than the wavelength ($d \ll \lambda$).
$$ \sigma \propto \frac{d^6}{\lambda^4} $$
*   Explains blue sky (short $\lambda$ blue light scattered more than red).

### Thomson Scattering
Low-energy photon scattering off a free charged particle (electron).
$$ \sigma_T = \frac{8\pi}{3} r_e^2 $$
where $r_e$ is the classical electron radius. Independent of frequency.

## 13.3 Inelastic Scattering

Energy is exchanged between incident particle and target.

### Compton Scattering
Photon scatters off an electron, transferring momentum and energy. The photon wavelength shifts (redshifts):
$$ \Delta \lambda = \lambda' - \lambda = \frac{h}{m_e c} (1 - \cos\theta) $$
*   $\frac{h}{m_e c} = 0.00243 \, nm$ (Compton wavelength).

### Raman Scattering
Inelastic scattering of photons by molecules.
*   **Stokes shift:** Photon loses energy (excites molecule).
*   **Anti-Stokes shift:** Photon gains energy (molecule de-excites).

## 13.4 Radar and Absorption

Radar detects objects via backscattering (Reflection).
**Radar Equation:**
$$ P_r = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4} $$
*   $P_r$: Received power.
*   $\sigma$: Radar Cross Section (RCS).
*   $R$: Distance.

**Stealth:** Minimizes $P_r$ by reducing $\sigma$.
1.  **Geometry:** Reflect waves away from source.
2.  **Absorption:** Use materials with high dielectric/magnetic loss to convert wave energy to heat.

---

## Dictionary of Terms

*   **Attenuation:** The reduction in amplitude or intensity of a signal as it travels through a medium.
*   **Compton Scattering:** The scattering of a photon by a charged particle, usually an electron, resulting in a decrease in energy (increase in wavelength) of the photon.
*   **Cross-Section ($\sigma$):** A measure of the probability that a specific process will take place in a collision of two particles.
*   **Elastic Scattering:** Scattering in which the kinetic energy of the incident particles is conserved.
*   **Inelastic Scattering:** Scattering in which the kinetic energy of the incident particles is not conserved.
*   **Radar Cross Section (RCS):** A measure of how detectable an object is by radar.
*   **Rayleigh Scattering:** Elastic scattering of light or other electromagnetic radiation by particles much smaller than the wavelength of the radiation.
