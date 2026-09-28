#!/usr/bin/env python3
"""
E47 mass-ladder parameter/dependency/look-elsewhere audit
=========================================================

Reproduces:
  1) displayed residual statistics;
  2) exact-formula residual statistics;
  3) descriptive parameter/dependency counts;
  4) a conservative per-target template-search Monte Carlo null;
  5) a global dependency-graph random-slot Monte Carlo null.

The Monte Carlo p-values are conditional on the grammar and null measure
defined explicitly below. They are not universal probabilities for "E47".
"""

import numpy as np
import math
import json

# ---------------------------------------------------------------------
# Observed ladder
# ---------------------------------------------------------------------
rows = [
    ("H",     125.0,       125.20),
    ("t",     172.0,       172.57),
    ("Z",      92.496,      91.188),
    ("W",      81.124,      80.369),
    ("b",       4.273,       4.200),
    ("tau",     1.767,       1.777),
    ("c(mc)",   1.270,       1.273),
    ("c(3)",    0.986,       0.989),
    ("mu",      0.105,       0.10566),
    ("s",       0.0940,      0.09346),
    ("d",       0.00470,     0.00470),
    ("u",       0.002136,    0.00214),
    ("e",       5.113e-4,    5.110e-4),
    ("nu2",     8.570,       8.678),   # meV
    ("nu3",    50.133,      50.10),    # meV
]

targets = {n:t for n,_,t in rows}
err_frac = np.array([p/t - 1 for n,p,t in rows], dtype=float)

display_stats = {
    "median_abs_pct": float(np.median(np.abs(err_frac))*100),
    "mean_abs_pct": float(np.mean(np.abs(err_frac))*100),
    "rms_pct": float(np.sqrt(np.mean(err_frac**2))*100),
    "max_abs_pct": float(np.max(np.abs(err_frac))*100),
    "T_obs": float(np.sqrt(np.mean(err_frac**2))),
}

# ---------------------------------------------------------------------
# Exact formulas
# ---------------------------------------------------------------------
Z = 246 * 47 / 125
W = Z * math.sqrt(10/13)

pred_exact = {
    "H": 125.0,
    "t": 125.0 + 47.0,
    "Z": Z,
    "W": W,
    "b": 47/11,
    "tau": 47**2/(125*10),
    "c(mc)": 47/37,
    "c(3)": 0.98607,                   # displayed RG-evolved value
    "mu": (78+27)*1e-3,
    "s": 2*47*1e-3,
    "d": 47/10*1e-3,
    "u": 47/22*1e-3,
    "e": 47**2/(432*10)*1e-3,
    "nu2": math.sqrt(47)*5/4,
    "nu3": 47*16/15,
}

e15 = np.array([pred_exact[n]/targets[n]-1 for n,_,_ in rows])
e14 = np.array([pred_exact[n]/targets[n]-1 for n,_,_ in rows if n != "c(3)"])

exact_stats = {
    "rms_15_pct": float(np.sqrt(np.mean(e15**2))*100),
    "rms_14_direct_pct": float(np.sqrt(np.mean(e14**2))*100),
    "median_abs_15_pct": float(np.median(np.abs(e15))*100),
    "mean_abs_15_pct": float(np.mean(np.abs(e15))*100),
    "max_abs_15_pct": float(np.max(np.abs(e15))*100),
}

# ---------------------------------------------------------------------
# Parameter/dependency inventory
# ---------------------------------------------------------------------
primitive_symbols = {
    "D":125, "E":47, "two":2, "four":4, "three":3, "thirteen":13,
    "kappa":16, "five":5, "six":6, "C42":42, "rank":78,
    "d27":27, "d22":22, "K432":432, "fifteen":15,
}

parameter_audit = {
    "continuous_fitted_parameters": 0,
    "direct_algebraic_outputs": 14,
    "rg_derived_outputs": 1,
    "unique_structural_integer_symbols_used": len(primitive_symbols),
    "direct_algebraic_operator_nodes": 30,
    "external_deterministic_maps": ["QCD RG map for c(mc) -> c(3 GeV)"],
    "note": "The 15 structural integers are fixed symbols if the E47 lock table and formula map are preregistered; otherwise their selection contributes discrete look-elsewhere freedom."
}

dependencies = {
    "H": ["D"],
    "t": ["D","E"],
    "v": ["two","D","four"],
    "Z": ["v","E","D"],
    "W": ["Z","three","thirteen"],
    "b": ["E","kappa","five"],
    "tau": ["E","D","kappa","six"],
    "c(mc)": ["E","C42","five"],
    "c(3)": ["c(mc)","QCD_RG"],
    "mu": ["rank","d27"],
    "s": ["two","E"],
    "d": ["E","kappa","six"],
    "u": ["E","d22"],
    "e": ["E","K432","kappa","six"],
    "nu2": ["E","five","four"],
    "nu3": ["E","kappa","fifteen"],
}

# ---------------------------------------------------------------------
# Full locked integer atom pool used by the null grammar
# ---------------------------------------------------------------------
pool = np.array(
    [1,2,3,4,5,6,9,12,13,15,16,17,20,22,25,27,28,30,42,47,
     78,108,112,125,140,180,432,11664],
    dtype=float
)

def pos_unique(a, lo=1e-15, hi=1e15):
    a = np.asarray(a, dtype=float).ravel()
    a = a[np.isfinite(a) & (a > lo) & (a < hi)]
    return np.unique(a)

ident = pos_unique(pool)
sumc = pos_unique(pool[:,None] + pool[None,:])
prodc = pos_unique(pool[:,None] * pool[None,:])
ratioc = pos_unique(pool[:,None] / pool[None,:])

diff = (pool[:,None]-pool[None,:]).ravel()
diffpos = diff[diff > 0]
qdiff = pos_unique(pool[:,None] / diffpos[None,:])                          # a/(b-c)

den2 = (pool[:,None]*diffpos[None,:]).ravel()
tau_cands = pos_unique((pool[:,None]**2) / den2[None,:])                   # a^2/[b(c-d)]

sqrt_ratio = pos_unique(
    np.sqrt(pool)[:,None,None] * pool[None,:,None] / pool[None,None,:]
)                                                                          # sqrt(a)b/c

ab_over_c = pos_unique(
    pool[:,None,None] * pool[None,:,None] / pool[None,None,:]
)                                                                          # ab/c

# Z-template: (ab-c)d/e
ab = (pool[:,None]*pool[None,:]).ravel()
x = (ab[:,None]-pool[None,:]).ravel()
x = np.unique(x[x > 0])
rat = np.unique((pool[:,None]/pool[None,:]).ravel())
z_cands = (x[:,None]*rat[None,:]).ravel()
z_cands = np.unique(z_cands[(z_cands > 0) & (z_cands < 1e5)])

# W correction: sqrt(1-a/b)
rr = (pool[:,None]/pool[None,:]).ravel()
rr = rr[(rr > 0) & (rr < 1)]
corr = np.unique(np.sqrt(1-rr))

candidate_counts = {
    "atom_pool": int(len(pool)),
    "identity": int(len(ident)),
    "sum": int(len(sumc)),
    "product": int(len(prodc)),
    "ratio": int(len(ratioc)),
    "quotient_difference": int(len(qdiff)),
    "square_over_product_difference": int(len(tau_cands)),
    "sqrt_ratio": int(len(sqrt_ratio)),
    "product_ratio": int(len(ab_over_c)),
    "Z_affine_ratio": int(len(z_cands)),
    "W_correction": int(len(corr)),
}

def nearest_rel_batch(arr, t):
    t = np.asarray(t, dtype=float)
    idx = np.searchsorted(arr, t)
    i0 = np.clip(idx-1, 0, len(arr)-1)
    i1 = np.clip(idx,   0, len(arr)-1)
    v0, v1 = arr[i0], arr[i1]
    return np.minimum(np.abs(v0/t-1), np.abs(v1/t-1))

def nearest_w_batch(t):
    t = np.asarray(t, dtype=float)
    q = t[:,None]/corr[None,:]
    idx = np.searchsorted(z_cands, q)
    i0 = np.clip(idx-1,0,len(z_cands)-1)
    i1 = np.clip(idx,0,len(z_cands)-1)
    v0 = z_cands[i0]*corr[None,:]
    v1 = z_cands[i1]*corr[None,:]
    return np.min(
        np.minimum(np.abs(v0/t[:,None]-1), np.abs(v1/t[:,None]-1)),
        axis=1
    )

# ---------------------------------------------------------------------
# Conservative flexible-expression null
#
# Each of the 14 direct targets gets the best expression from the
# formula topology actually used for that target. Shared constants are
# NOT forced to agree across targets. This gives the null more freedom
# than the displayed construction and therefore is deliberately
# conservative with respect to look-elsewhere effects.
# ---------------------------------------------------------------------
targets_display = {
    "H":125.20, "t":172.57, "Z":91.188, "W":80.369,
    "b":4.200, "tau":1.777, "c(mc)":1.273,
    "mu":105.66, "s":93.46, "d":4.70, "u":2.14, "e":0.5110,
    "nu2":8.678, "nu3":50.10,
}
names14 = list(targets_display)
exps = np.array(
    [math.floor(math.log10(targets_display[n])) for n in names14],
    dtype=int
)
arr_map = {
    "H":ident, "t":sumc, "Z":z_cands, "b":qdiff, "tau":tau_cands,
    "c(mc)":qdiff, "mu":sumc, "s":prodc, "d":qdiff, "u":ratioc,
    "e":tau_cands, "nu2":sqrt_ratio, "nu3":ab_over_c
}

Tobs14 = math.sqrt(np.mean(e14**2))

def run_flexible_null(N=100_000, seed=20260928, log_uniform=True, batch=2500):
    rng = np.random.default_rng(seed)
    hits = 0
    saved = []
    done = 0

    while done < N:
        n = min(batch, N-done)
        if log_uniform:
            u = rng.random((n,len(names14)))
            targ = 10.0**(exps[None,:] + u)
        else:
            mant = 1.0 + 9.0*rng.random((n,len(names14)))
            targ = (10.0**exps)[None,:] * mant

        e2 = np.zeros(n)
        for j,name in enumerate(names14):
            if name == "W":
                er = nearest_w_batch(targ[:,j])
            else:
                er = nearest_rel_batch(arr_map[name], targ[:,j])
            e2 += er*er

        score = np.sqrt(e2/len(names14))
        hits += int(np.count_nonzero(score <= Tobs14))
        if len(saved) < 20:
            saved.append(score)
        done += n

    sample = np.concatenate(saved)
    return {
        "N": N,
        "hits": hits,
        "p_add_one": (hits+1)/(N+1),
        "sample_quantiles": {
            "q01": float(np.quantile(sample,.01)),
            "q05": float(np.quantile(sample,.05)),
            "q50": float(np.quantile(sample,.50)),
            "q95": float(np.quantile(sample,.95)),
            "q99": float(np.quantile(sample,.99)),
        }
    }

flex_log = run_flexible_null(seed=20260928, log_uniform=True)
flex_linear = run_flexible_null(seed=20260929, log_uniform=False)

# Best fit to the real targets if the same template grammar is allowed
# to reselect atom values independently for each target.
best_actual_errors = {}
for name,t in targets_display.items():
    if name == "W":
        er = nearest_w_batch(np.array([t]))[0]
    else:
        er = nearest_rel_batch(arr_map[name], np.array([t]))[0]
    best_actual_errors[name] = float(er)

best_actual_template_rms = float(
    np.sqrt(np.mean(np.array(list(best_actual_errors.values()))**2))
)

# ---------------------------------------------------------------------
# Global-DAG random-slot null
#
# Here the dependency graph and global reuse are preserved. The 15
# primitive symbol slots are assigned random members of the same locked
# atom pool. No per-target re-selection is allowed.
# ---------------------------------------------------------------------
rg_factor = 0.98607/(47/37)
targets_arr = np.array([t for _,_,t in rows], dtype=float)

def run_global_dag_null(N=2_000_000, seed=20260930, batch=50_000):
    rng = np.random.default_rng(seed)
    valid = 0
    hits = 0

    for off in range(0,N,batch):
        n = min(batch,N-off)
        X = rng.choice(pool,size=(n,15),replace=True)
        D,E,two,four,three,thirteen,k,five,six,C42,R,d27,d22,K432,fifteen = X.T

        db = k-five
        dt = k-six
        dc = C42-five

        vm = (thirteen > three) & (db != 0) & (dt != 0) & (dc != 0)
        if not np.any(vm):
            continue

        D,E,two,four,three,thirteen,k,five,six,C42,R,d27,d22,K432,fifteen = [
            a[vm] for a in
            (D,E,two,four,three,thirteen,k,five,six,C42,R,d27,d22,K432,fifteen)
        ]

        v = two*D-four
        Z = v*E/D
        W = Z*np.sqrt(1-three/thirteen)
        c = E/(C42-five)

        pred = np.column_stack([
            D,
            D+E,
            Z,
            W,
            E/(k-five),
            E**2/(D*(k-six)),
            c,
            c*rg_factor,
            (R+d27)*1e-3,
            two*E*1e-3,
            E/(k-six)*1e-3,
            E/d22*1e-3,
            E**2/(K432*(k-six))*1e-3,
            np.sqrt(E)*five/four,
            E*k/fifteen,
        ])

        pm = np.all(np.isfinite(pred) & (pred > 0), axis=1)
        pred = pred[pm]
        if len(pred) == 0:
            continue

        score = np.sqrt(np.mean((pred/targets_arr - 1)**2,axis=1))
        valid += len(score)
        hits += int(np.count_nonzero(score <= math.sqrt(np.mean(e15**2))))

    # add-one empirical estimator; also give the 95% zero-hit upper bound
    p_add_one = (hits+1)/(valid+1)
    upper95_zero_hit = None if hits else 1 - 0.05**(1/valid)

    return {
        "N_draws": N,
        "valid_draws": valid,
        "hits": hits,
        "p_add_one_conditional_valid": p_add_one,
        "zero_hit_95pct_upper_bound": upper95_zero_hit,
    }

dag_null = run_global_dag_null()

out = {
    "display_stats": display_stats,
    "exact_formula_stats": exact_stats,
    "parameter_audit": parameter_audit,
    "primitive_symbols": primitive_symbols,
    "dependencies": dependencies,
    "candidate_counts": candidate_counts,
    "best_actual_template_rms_pct": best_actual_template_rms*100,
    "best_actual_template_errors_pct": {k:v*100 for k,v in best_actual_errors.items()},
    "flexible_null_log_uniform_mantissa": flex_log,
    "flexible_null_linear_mantissa": flex_linear,
    "global_DAG_random_slot_null": dag_null,
}

print(json.dumps(out, indent=2))