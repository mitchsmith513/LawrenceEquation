# LawrenceEquation

**A Deterministic Generalization of Quantum Evolution with Entropy-Producing Decoherence**

**File:** `evolve_lawrence_psi.py`  
**Author:** M.L. Smith (2024)

---

## Overview

The **Lawrence Equation** introduces a deterministic extension of quantum mechanics that unifies unitary evolution with entropy-producing collapse. It modifies the standard Schrödinger equation by introducing two novel parameters:

- **Alpha (α):** A complex-phase deformation of the unitary operator  
- **Gamma (γ):** A localized decoherence term that models entropy growth and wavefunction collapse

---

## Core Function

```python
def evolve_lawrence_psi(psi, H, dt, alpha=1.0, gamma=0.0, decoherence_mask=None):
    """
    Evolve a quantum state under the Lawrence Equation.

    Parameters:
    - psi: complex wavefunction (numpy array, shape [N])
    - H: Hamiltonian matrix (numpy array, shape [N, N])
    - dt: time step (float)
    - alpha: phase deformation (float, default=1.0; standard QM)
    - gamma: decoherence strength (float, default=0.0)
    - decoherence_mask: numpy array, same shape as psi, with 0 where decoherence acts and 1 where preserved

    Returns:
    - psi_new: normalized updated wavefunction (numpy array, shape [N])
    """
License
MIT License

Citation
Please cite as:
M.L. Smith (2024). The Lawrence Equation: A Deterministic Generalization of Quantum Evolution. Zenodo. https://zenodo.org/records/15268394

Contact
Email: Saint513@icloud.com
GitHub: github.com/mitchsmith513

"Determinism meets entropy. Quantum mechanics evolves."
