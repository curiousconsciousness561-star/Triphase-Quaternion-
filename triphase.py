import numpy as np

def triphase_quaternion(theta, phi, psi):
    """Return a unit quaternion from three phases (triphase quaternion)."""
    vi = np.array([np.cos(theta), np.sin(theta), 0, 0])
    vj = np.array([np.cos(phi),   0, np.sin(phi), 0])
    vk = np.array([np.cos(psi),   0, 0, np.sin(psi)])
    v = vi + vj + vk
    norm = np.sqrt(3 + 2*(np.cos(theta-phi) + np.cos(theta-psi) + np.cos(phi-psi)))
    return v / norm

def random_triphase(n=1):
    """Generate n random triphase unit quaternions (uniform phases)."""
    phases = np.random.uniform(0, 2*np.pi, size=(n, 3))
    return np.array([triphase_quaternion(*p) for p in phases])

# Example
if __name__ == "__main__":
    q = random_triphase(5)
    print("5 random triphase quaternions:\n", q)
    print("Norms:", np.linalg.norm(q, axis=1))
