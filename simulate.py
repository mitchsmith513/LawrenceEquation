
from .core import evolve_lawrence_psi
import numpy as np

def run_simulation(psi0, H, alpha=1.0, gamma=0.0, dt=0.01, steps=100):
    psi = psi0.copy()
    decoherence_mask = np.ones_like(psi0)
    for _ in range(steps):
        psi = evolve_lawrence_psi(psi, H, dt, alpha, gamma, decoherence_mask)
    return psi
