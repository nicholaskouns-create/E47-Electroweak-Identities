# Supplemental Monte Carlo note

Registered 28 September 2026.

**This note is not the headline claim.**
The claim remains

$$
\mathcal I_{\mathrm{EW}}
=
\left(
 v\Omega_c,\ 
 \sqrt{10/13},\ 
 172/125
\right).
$$

The fifteen-row ladder is audit. The statistic

$$
T_{\mathrm{obs}}
=
\mathrm{RMS}(\delta)/100
=
0.007692169
$$

is an audit RMS. It is not itself a $p$-value.

---

## What was run

Matched-form searches on the recovered audit ladder, certified by the instrument author as executed in a separate audit from the frozen generator `src/e47_electroweak_identities.py`.

Estimator used:

$$
\hat p
=
\frac{
1+\#\{T_{\mathrm{null}}\le T_{\mathrm{obs}}\}
}{
N_{\mathrm{MC}}+1
}.
$$

| Null | Reported $\hat p$ | Role |
|---|---:|---|
| local factor $\times 3$ | $0.00714$ | supplemental |
| same-decade | $0.001575$ | supplemental |

## Null names, as certified

1. **Local factor $\times 3$ null.** Matched-form constructions that keep the local integer-factor grammar of a displayed entry and vary the comparison target inside a $\times 3$ neighborhood of the observed scale.
2. **Same-decade null.** Matched-form constructions restricted to the same order of magnitude as the observed target.

These are not the two design nulls written into the earlier look-elsewhere scaffold (target-randomization of the full ladder; grammar-flexibility over the full expression DAG). They are a narrower matched-form audit of the recovered ladder.

## What is not deposited here

- $N_{\mathrm{MC}}$
- raw $T_{\mathrm{null}}$ draws
- the matched-form generator source
- a claim that either $\hat p$ is a global look-elsewhere probability for $\mathcal I_{\mathrm{EW}}$

Those artifacts can be appended later without touching $I_1,I_2,I_3$.

## Logical placement

```text
I_EW                 = headline identities
A_246                = audit ladder
T_obs                = audit RMS of A_246
this note            = supplemental matched-form pressure on A_246
```

Mutation of this note does not mutate $\mathcal I_{\mathrm{EW}}$.
