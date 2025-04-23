# LawrenceEquation
“Deterministic generalization of quantum evolution with entropy-producing decoherence”
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
