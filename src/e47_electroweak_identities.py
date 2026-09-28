#!/usr/bin/env python3
"""E47 Electroweak Identities — frozen generator.

Kernel lock
    K = (C - 6 I)(C - 30 I)
    dim E47 = 47
    Omega_c = 47/125

Headline identities (CERN-facing; only dimensionful input is G_F)
    m_Z^(0)  = v * Omega_c
    m_W/m_Z  = sqrt(10/13)
    m_t/m_H  = 1 + Omega_c = 172/125

    v = (sqrt(2) * G_F)^(-1/2)

The 15-row mass ladder is an AUDIT object, not the claim.
Integer 246 appearing in the recovered audit is the integer stand-in
for v. Headline evaluation uses G_F, not that integer.

This file is the canonical generator. Hash it. Do not edit in place
to change a headline identity; freeze a new version instead.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

KERNEL = "(C - 6I)(C - 30I)"
DIM_E47 = 47
OMEGA_C = 47 / 125
OMEGA_C_FRAC = (47, 125)
G_F = 1.1663788e-5

AUDIT_TARGETS = {
    "H": 125.20,
    "t": 172.57,
    "Z": 91.188,
    "W": 80.369,
    "b": 4.200,
    "tau": 1.777,
    "c(mc)": 1.273,
    "c(3)": 0.989,
    "mu": 0.10566,
    "s": 0.09346,
    "d": 0.00470,
    "u": 0.00214,
    "e": 5.110e-4,
    "nu2_mev": 8.678,
    "nu3_mev": 50.10,
}

PDG_2025 = {
    "G_F": G_F,
    "m_Z": 91.1880,
    "m_W": 80.3692,
    "m_W_over_m_Z": 0.88136,
    "m_H_audit": 125.20,
    "m_t_audit": 172.57,
}


def vev_from_gf(g_f: float = G_F) -> float:
    return 1.0 / math.sqrt(math.sqrt(2.0) * g_f)


def headline_identities(g_f: float = G_F) -> dict:
    v = vev_from_gf(g_f)
    m_z0 = v * OMEGA_C
    ratio_wz = math.sqrt(10.0 / 13.0)
    m_w0 = m_z0 * ratio_wz
    ratio_th = 1.0 + OMEGA_C
    return {
        "kernel": KERNEL,
        "dim_E47": DIM_E47,
        "Omega_c": OMEGA_C,
        "Omega_c_frac": "47/125",
        "G_F_GeV_m2": g_f,
        "v_GeV": v,
        "m_Z0_GeV": m_z0,
        "m_W0_GeV": m_w0,
        "m_W_over_m_Z": ratio_wz,
        "m_t_over_m_H": ratio_th,
        "m_H_algebraic_GeV": 125.0,
        "m_t_algebraic_GeV": 172.0,
        "identities": {
            "I1": "m_Z^(0) = v * Omega_c",
            "I2": "m_W / m_Z = sqrt(10/13)",
            "I3": "m_t / m_H = 1 + Omega_c = 172/125",
        },
    }


def identity_residuals(g_f: float = G_F) -> dict:
    h = headline_identities(g_f)
    z_over_v_meas = PDG_2025["m_Z"] / h["v_GeV"]
    wz_meas = PDG_2025["m_W"] / PDG_2025["m_Z"]
    th_meas = PDG_2025["m_t_audit"] / PDG_2025["m_H_audit"]

    def rel_pct(pred, meas):
        return (pred - meas) / meas * 100.0

    return {
        "m_Z_over_v": {
            "predicted": OMEGA_C,
            "measured": z_over_v_meas,
            "residual_pct": rel_pct(OMEGA_C, z_over_v_meas),
        },
        "m_W_over_m_Z": {
            "predicted": h["m_W_over_m_Z"],
            "measured": wz_meas,
            "pdg_listed": PDG_2025["m_W_over_m_Z"],
            "residual_pct": rel_pct(h["m_W_over_m_Z"], wz_meas),
        },
        "m_t_over_m_H": {
            "predicted": h["m_t_over_m_H"],
            "measured_audit": th_meas,
            "residual_pct": rel_pct(h["m_t_over_m_H"], th_meas),
        },
    }


def audit_ladder_integer_v() -> dict:
    Z = 246 * 47 / 125
    W = Z * math.sqrt(10 / 13)
    return {
        "H": 125.0,
        "t": 125.0 + 47.0,
        "Z": Z,
        "W": W,
        "b": 47 / 11,
        "tau": 47**2 / (125 * 10),
        "c(mc)": 47 / 37,
        "mu": (78 + 27) * 1e-3,
        "s": 2 * 47 * 1e-3,
        "d": 47 / 10 * 1e-3,
        "u": 47 / 22 * 1e-3,
        "e": 47**2 / (432 * 10) * 1e-3,
        "nu2_mev": math.sqrt(47) * 5 / 4,
        "nu3_mev": 47 * 16 / 15,
    }


def audit_residuals():
    vals = audit_ladder_integer_v()
    rows = [
        ("H", vals["H"], AUDIT_TARGETS["H"]),
        ("t", vals["t"], AUDIT_TARGETS["t"]),
        ("Z", 92.496, AUDIT_TARGETS["Z"]),
        ("W", 81.124, AUDIT_TARGETS["W"]),
        ("b", 4.273, AUDIT_TARGETS["b"]),
        ("tau", 1.767, AUDIT_TARGETS["tau"]),
        ("c(mc)", 1.270, AUDIT_TARGETS["c(mc)"]),
        ("c(3)", 0.986, AUDIT_TARGETS["c(3)"]),
        ("mu", 0.105, AUDIT_TARGETS["mu"]),
        ("s", 0.0940, AUDIT_TARGETS["s"]),
        ("d", 0.00470, AUDIT_TARGETS["d"]),
        ("u", 0.002136, AUDIT_TARGETS["u"]),
        ("e", 5.113e-4, AUDIT_TARGETS["e"]),
        ("nu2", 8.570, AUDIT_TARGETS["nu2_mev"]),
        ("nu3", 50.133, AUDIT_TARGETS["nu3_mev"]),
    ]
    out = []
    for name, pred, targ in rows:
        res = (pred - targ) / targ * 100.0
        out.append((name, pred, targ, res))
    return out


def audit_stats() -> dict:
    res = [r[3] for r in audit_residuals()]
    absr = [abs(x) for x in res]
    rms = math.sqrt(sum(x * x for x in res) / len(res))
    return {
        "n": len(res),
        "median_abs_pct": sorted(absr)[len(absr) // 2],
        "mean_abs_pct": sum(absr) / len(absr),
        "rms_pct": rms,
        "max_abs_pct": max(absr),
        "T_obs": rms / 100.0,
        "note": "AUDIT statistic. Not a look-elsewhere p-value.",
    }


def file_sha256(path=None) -> str:
    p = Path(path) if path is not None else Path(__file__)
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump_lock(path="e47_electroweak_lock.json") -> dict:
    payload = {
        "instrument": "E47 Electroweak Identities",
        "status": "FROZEN",
        "date_utc": "2026-09-28",
        "author": "Nicholas S. Kouns",
        "affiliation": "AIMS Research Institute",
        "kernel": KERNEL,
        "dim_E47": DIM_E47,
        "Omega_c": "47/125",
        "headline": headline_identities(),
        "identity_residuals": identity_residuals(),
        "audit_stats": audit_stats(),
        "look_elsewhere": "NOT COMPUTED. Not claimed.",
    }
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


if __name__ == "__main__":
    h = headline_identities()
    r = identity_residuals()
    s = audit_stats()
    print("KERNEL", KERNEL)
    print("dim E47", DIM_E47)
    print("Omega_c", OMEGA_C)
    print("G_F", G_F)
    print("v / GeV", h["v_GeV"])
    print("m_Z^(0) / GeV", h["m_Z0_GeV"])
    print("m_W^(0) / GeV", h["m_W0_GeV"])
    print("m_W/m_Z", h["m_W_over_m_Z"])
    print("m_t/m_H", h["m_t_over_m_H"])
    print("--- identity residuals (percent) ---")
    for k, val in r.items():
        print(k, val)
    print("--- audit stats ---")
    print(s)
    print("SHA256", file_sha256(Path(__file__).resolve()))
