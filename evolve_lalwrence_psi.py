"""
evolve_lawrence_psi.py

Core time-evolution function for the Lawrence Equation: a deterministic generalization
of quantum mechanics that introduces complex-phase deformation (alpha) and
localized decoherence (gamma) to the standard Schrödinger evolution.

Author: M.L. Smith (2024)
"""

import numpy as np

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
    i_alpha = (1j) ** alpha
    dpsi_unitary = -i_alpha * H @ psi
    dpsi_decoh = -gamma * (1 - decoherence_mask) * psi if (gamma > 0 and decoherence_mask is not None) else 0
    psi_new = psi + dt * (dpsi_unitary + dpsi_decoh)
    return psi_new / np.sqrt(np.sum(np.abs(psi_new)**2))
