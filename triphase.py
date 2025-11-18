import numpy as np

def triphase_quaternion(theta, phi, psi):
    """Triphase quaternion (normalized sum of three phase exponentials)."""
    ci, si = np.cos(theta), np.sin(theta)
    cj, sj = np.cos(phi),   np.sin(phi)
    ck, sk = np.cos(psi),   np.sin(psi)
    v = np.array([ci + cj + ck, si, sj, sk])
    norm_sq = 3 + 2*(np.cos(theta-phi) + np.cos(theta-psi) + np.cos(phi-psi))
    return v / np.sqrt(norm_sq)

def random_triphase(n=1):
    phases = np.random.uniform(0, 2*np.pi, (n, 3))
    return np.array([triphase_quaternion(*p) for p in phases])
