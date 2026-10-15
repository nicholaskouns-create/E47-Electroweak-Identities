"""First-principles check of the locked kernel numbers.

Builds V_2^{(x)3}, its total Casimir, and K = (C - 6I)(C - 30I) from the
spin-2 matrices, then compares with the frozen generator's constants.
The generator itself is not edited.
"""
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import e47_electroweak_identities as e47


def spin_matrices(j):
    m = np.arange(j, -j - 1, -1)
    raise_ = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1)
    return (raise_ + raise_.T) / 2, (raise_ - raise_.T) / 2j, np.diag(m)


def total(a, eye):
    return (np.kron(np.kron(a, eye), eye)
            + np.kron(np.kron(eye, a), eye)
            + np.kron(np.kron(eye, eye), a))


def test_clebsch_gordan_series():
    mult = Counter({2: 1})
    for _ in range(2):
        nxt = Counter()
        for J, n in mult.items():
            for L in range(abs(J - 2), J + 3):
                nxt[L] += n
        mult = nxt
    assert [mult[J] for J in range(7)] == [1, 3, 5, 4, 3, 2, 1]
    dims = {J: n * (2 * J + 1) for J, n in mult.items()}
    assert sum(dims.values()) == 125
    assert dims[2] + dims[5] == e47.DIM_E47


def test_kernel_from_spin_matrices():
    eye = np.eye(5)
    C = sum(total(a, eye) @ total(a, eye) for a in spin_matrices(2))
    evals = np.linalg.eigvalsh(C)
    assert np.allclose(evals, np.round(evals), atol=1e-9)
    assert dict(Counter(int(round(x)) for x in evals)) == {
        0: 1, 2: 9, 6: 25, 12: 28, 20: 27, 30: 22, 42: 13,
    }
    I = np.eye(125)
    K = (C - 6 * I) @ (C - 30 * I)
    nullity = 125 - np.linalg.matrix_rank(K, tol=1e-6)
    assert nullity == e47.DIM_E47
    assert Fraction(nullity, 125) == Fraction(*e47.OMEGA_C_FRAC)
