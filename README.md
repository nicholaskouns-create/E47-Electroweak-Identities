# E47 Electroweak Identities

> **Mathematical City:** [Networked Atlas](https://nicholaskouns-create.github.io/E47-Kartekeya/) · verified by the E47-Kartekeya Pages deployment.


**Three identities. One external scale. No fit.**

From the finite kernel

$$
K=(C-6I)(C-30I)
\quad\text{on}\quad
\mathcal H=V_2^{\otimes 3},\ \dim\mathcal H=125
$$

comes

$$
\dim E_{47}=47,
\qquad
\Omega_c=\frac{47}{125}=0.376.
$$

The only dimensionful input is the Fermi constant from the muon lifetime.
Everything else is a ratio.

$$
G_F=1.1663788\times 10^{-5}\,\mathrm{GeV}^{-2}
\quad\Longrightarrow\quad
v=(\sqrt{2}\,G_F)^{-1/2}=246.21964024\,\mathrm{GeV}
$$

| | Identity | Value | Measured | Residual |
|---|---|---:|---:|---:|
| **I₁** | $m_Z^{(0)}=v\,\Omega_c$ | 92.5786 GeV | $m_Z/v=0.370352$ | **+1.525%** |
| **I₂** | $m_W/m_Z=\sqrt{10/13}$ | 0.877058 | 0.881357 | **−0.488%** |
| **I₃** | $m_t/m_H=1+\Omega_c=172/125$ | 1.376 | 1.378355 | **−0.171%** |

Skeleton masses from $G_F$ alone:

$$
m_Z^{(0)}=92.57858473\,\mathrm{GeV},
\qquad
m_W^{(0)}=81.19679015\,\mathrm{GeV}.
$$

Status: **UNFROZEN** · 28 September 2026 · Nicholas S. Kouns · AIMS Research Institute

[Live page](https://nicholaskouns-create.github.io/electroweak/) · [How to read](docs/HOW_TO_READ.md) · [Symbolic proof](docs/E47_Electroweak_and_Mass_Ladder_Recovery.md) · [Audit table](docs/audit_ladder.md) · [Look-elsewhere audit source](audit/e47_mass_ladder_look_elsewhere_audit.py) · [Supplemental MC](docs/SUPPLEMENTAL_MONTE_CARLO.md) · [Generator](src/e47_electroweak_identities.py)

---

## What this is

A first-principles map from a spectral kernel to three electroweak ratios.

```text
V2^{⊗ 3}  →  C  →  K=(C-6I)(C-30I)  →  E47 = ker K
     dim 125                              dim 47
                                              ↓
                                         Ωc = 47/125
                                              ↓
                                    G_F → v → m_Z^(0) = v Ωc
                                              ↓
                                    m_W / m_Z = √(10/13)
                                    m_t / m_H = 172/125
```

## What this is not

- Not a fit. No continuous parameters were adjusted to the masses.
- $T_{\mathrm{obs}}=0.007692169$ is an audit RMS, not a $p$-value.
- Not a claim that the integer-$246$ fifteen-row ladder is the instrument.
  That table is [audit only](docs/audit_ladder.md).
- $c(3\,\mathrm{GeV})$ is a running of $47/37$, not a recovered closed form.
- Supplemental matched-form $\hat p$ values live in a [separate note](docs/SUPPLEMENTAL_MONTE_CARLO.md). They pressure the audit ladder. They do not replace $I_1,I_2,I_3$.

## Audit snapshot

$$
\mathrm{median}|\delta|=0.33\%,\quad
\mathrm{mean}|\delta|=0.56\%,\quad
\mathrm{RMS}(\delta)=0.77\%,\quad
\max|\delta|=1.74\%.
$$

Supplemental matched-form audit, certified executed, not deposited as raw draws:

$$
\hat p_{\times 3}\approx 0.00714,
\qquad
\hat p_{\mathrm{decade}}\approx 0.001575.
$$

## Run

```bash
python3 src/e47_electroweak_identities.py
```

Machine copies: [data/identities.json](data/identities.json) · [data/supplemental_monte_carlo.json](data/supplemental_monte_carlo.json).

## City

| Surface | Role |
|---|---|
| [E47-Kartekeya](https://github.com/nicholaskouns-create/E47-Kartekeya) | executable City, tests, certificates |
| [Convergence + noiseless-subsystem certificate](https://github.com/nicholaskouns-create/E47-Kartekeya/blob/main/certificates/MC-E47-CONVERGENCE-NOISELESS-20260928-001.json) | machine-certified kernel convergence and C⁵⊗V₂ ⊕ C²⊗V₅ collective-SU(2) multiplicity closure |
| [This repo](https://github.com/nicholaskouns-create/E47-Electroweak-Identities) | electroweak identity instrument |
| [Root atlas](https://nicholaskouns-create.github.io/) | vestibule |
| [Foundry plate](https://github.com/nicholaskouns-create/E47-Foundry-Lifetime-Intersection) | lifetime algebra, same kernel |

## Cite

Use [CITATION.cff](CITATION.cff). License: [CC0 1.0](LICENSE).
