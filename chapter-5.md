# Chapter 5: Oscillations and Waves

## 5.1 Simple Harmonic Motion (SHM)

SHM occurs whenever a restoring force is proportional to the displacement from equilibrium.
$$ F = -kx $$
Using Newton's Second Law ($F=ma$):
$$ m \frac{d^2x}{dt^2} = -kx \implies \frac{d^2x}{dt^2} + \frac{k}{m}x = 0 $$
Defining natural frequency $\omega = \sqrt{k/m}$, the solution is:
$$ x(t) = A \cos(\omega t + \phi) $$

*   $A$: Amplitude (max displacement).
*   $\omega$: Angular frequency (rad/s).
*   $\phi$: Phase constant (determined by $x(0)$ and $v(0)$).

### Energy in SHM
Energy oscillates between kinetic and potential, but total energy is constant.
$$ E = K + U = \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = \frac{1}{2}kA^2 $$

## 5.2 Damped and Driven Oscillations

### Damping
Real systems lose energy to friction/drag.
$$ F_{damp} = -b v $$
Equation: $m \ddot{x} + b \dot{x} + kx = 0$.
Solutions decay exponentially: $x(t) \approx A e^{-bt/2m} \cos(\omega' t)$.

### Resonance
When a driving force $F(t) = F_0 \cos(\omega_d t)$ is applied, the system oscillates at $\omega_d$.
Amplitude is maximized when $\omega_d \approx \omega_{natural}$.

## 5.3 Waves

A wave is a disturbance that propagates through space, transporting energy but not matter.

**Wave Equation:**
$$ \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} $$
Solution for a traveling wave:
$$ y(x,t) = A \cos(kx - \omega t) $$
*   Wave number $k = 2\pi/\lambda$.
*   Speed $v = \omega/k = \lambda f$.

## 5.4 Standing Waves

Formed by the superposition of two waves traveling in opposite directions.
$$ y = A\cos(kx - \omega t) + A\cos(kx + \omega t) = 2A \sin(kx) \cos(\omega t) $$

*   **Nodes:** Points of zero amplitude ($\sin(kx) = 0$).
*   **Antinodes:** Points of max amplitude.

**String Fixed at Both Ends:**
Boundary conditions require nodes at $x=0$ and $x=L$.
$$ kL = n\pi \implies \lambda_n = \frac{2L}{n} $$
Frequencies: $f_n = n \frac{v}{2L}$. ($n=1$ is the fundamental).

## 5.5 Doppler Effect

The change in frequency observed when source or observer is moving.
$$ f_{obs} = f_s \left( \frac{v \pm v_{obs}}{v \mp v_s} \right) $$
*   Top signs: moving towards each other (frequency increases).
*   Bottom signs: moving away (frequency decreases).

---

## Dictionary of Terms

*   **Amplitude:** The maximum extent of a vibration or oscillation, measured from the position of equilibrium.
*   **Damping:** The reduction in the amplitude of an oscillation as a result of energy being drained from the system (e.g., friction).
*   **Frequency ($f$):** The number of occurrences of a repeating event per unit of time.
*   **Period ($T$):** The time taken for one complete cycle of vibration.
*   **Phase:** The position of a point in time on a waveform cycle.
*   **Resonance:** The tendency of a system to oscillate with greater amplitude at some frequencies than at others.
*   **Simple Harmonic Motion:** Repetitive movement back and forth through an equilibrium, or central, position, so that the maximum displacement on one side of this position equals the maximum displacement on the other side.
*   **Standing Wave:** A wave that remains in a constant position (does not propagate), often formed by interference.
*   **Wavelength ($\lambda$):** The distance between successive crests of a wave.
*   **Wave Number ($k$):** The spatial frequency of a wave ($2\pi/\lambda$).
