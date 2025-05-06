
import numpy as np

def evolve_lawrence_psi(psi, H, dt, alpha=1.0, gamma=0.0, decoherence_mask=None):
    i_alpha = (1j) ** alpha
    dpsi_unitary = -i_alpha * H @ psi
    dpsi_decoh = -gamma * (1 - decoherence_mask) * psi if (gamma > 0 and decoherence_mask is not None) else 0
    psi_new = psi + dt * (dpsi_unitary + dpsi_decoh)
    return psi_new / np.sqrt(np.sum(np.abs(psi_new)**2))
