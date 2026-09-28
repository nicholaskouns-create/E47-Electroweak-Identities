import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import e47_electroweak_identities as e47


def test_kernel_lock():
    assert e47.KERNEL == "(C - 6I)(C - 30I)"
    assert e47.DIM_E47 == 47
    assert e47.OMEGA_C == 47 / 125


def test_headline_identities():
    h = e47.headline_identities()
    assert math.isclose(h["m_W_over_m_Z"], math.sqrt(10 / 13), rel_tol=0, abs_tol=1e-15)
    assert math.isclose(h["m_t_over_m_H"], 172 / 125, rel_tol=0, abs_tol=1e-15)
    assert math.isclose(h["m_Z0_GeV"], h["v_GeV"] * 47 / 125, rel_tol=0, abs_tol=1e-12)


def test_audit_shape_and_stats():
    rows = e47.audit_residuals()
    stats = e47.audit_stats()
    assert len(rows) == 15
    assert stats["n"] == 15
    assert 0 < stats["rms_pct"] < 1.0


def test_frozen_lock_payload(tmp_path):
    p = tmp_path / "lock.json"
    payload = e47.dump_lock(p)
    assert payload["status"] == "FROZEN"
    assert payload["Omega_c"] == "47/125"
    assert p.exists()
