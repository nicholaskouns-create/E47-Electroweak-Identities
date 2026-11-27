> ⚛️ **[E₄₇ Φ₄ LIVE QUANTUM CIRCUIT](https://nicholaskouns-create.github.io/qsvt-phi4/)** · [250D QSP / 500D LCU full interactive diagram](https://nicholaskouns-create.github.io/E47-Kartekeya/interfaces/qsvt-phi4-circuit/) · [First-principles formalism and 14-check NumPy certificate](https://github.com/nicholaskouns-create/E47-Kartekeya/tree/main/research/e47/qsp_phi4). Cross-repository research link; not an independent validation in this repository.

# E47 Electroweak Identities

> **Current license:** [All Rights Reserved](LICENSE) for owned original material. No new reuse permission. Earlier licenses and third-party/public-domain rights remain unaffected.


> **Current licensing:** [All Rights Reserved](LICENSE) for original material owned by Nicholas Shane Kouns. No new reuse permission is granted. Previously granted licenses and third-party/public-domain rights remain unaffected.


> **Main entry portal:** [The Mathematical City](https://nicholaskouns-create.github.io/website/) — explore the districts, interactive labs, and research index.
>
> **[Explore PiP Manta](https://nicholaskouns-create.github.io/E47-Kartekeya/interfaces/pip-manta/embed.html)**

## Canonical E47 kernel authority · 2026-10-08

This instrument inherits the finite E47 kernel but does not redefine it. The current authority is [E47 Grassmann–Casimir Formalism (corrected)](https://github.com/nicholaskouns-create/E47-Kartekeya/blob/main/research/e47/E47_Grassmann_Casimir_Formalism_Corrected_20261008.md): `dim ker K = 47`, the physical projector identity is `P^T G = G P`, the distinct Grassmann constraint map has `dim ker A = 82`, and set equality of a 47-dimensional Grassmann intersection with `ker K` requires an explicit witness.

Cross-platform route: [Notion canonical formalism](https://app.notion.com/p/3a046094fd30811eb015e14e1c5bce7c) · [Drive archive](https://docs.google.com/document/d/1F6UvhIOElXLoTPMW3VtOntxv86r81uKQeGcQikNv3bE) · [Supabase Citadel](https://gpkjvihkyectnenvnbng.supabase.co/functions/v1/city-app-host/see/) · [Linear REC-12](https://linear.app/4521/issue/REC-12/publish-e47-grassmann-casimir-proof-and-34-check-python-package).

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

Residuals in the table are the claim boundary. `+1.525%`, `−0.488%`, `−0.171%` are not closure. `78` in the kernel complement is `dim H − dim E47`, not Lucas `L_9` (`L_9=76`).

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
- Not yet a derivation of $\sqrt{10/13}$. $I_2$ is stated beside the kernel; no step from $K$ to $10/13$ is deposited here.

## Audit snapshot

$$
\mathrm{median}|\delta|=0.33\%,\quad
\mathrm{mean}|\delta|=0.56\%,\quad
\mathrm{RMS}(\delta)=0.77\%,\quad
\max|\delta|=1.74\%.
$$

Deposited look-elsewhere audit, reproducible here and run in CI ([source](audit/e47_mass_ladder_look_elsewhere_audit.py), fixed seeds):

| Null | $p$ | What it measures |
|---|---:|---|
| flexible template, log-uniform targets | $\approx 0.043$ | how often random targets fit as well under the same grammar |
| flexible template, linear targets | $\approx 0.012$ | the same, with linear mantissas |
| global DAG, random atoms | $<1.8\times10^{-5}$ (0 of 163,345) | atom choice, conditional on the formulas as chosen |

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

Use [CITATION.cff](CITATION.cff). Current license: [All Rights Reserved](LICENSE).

[The E₄₇ spectral kernel · formalism and verification](e47-spectral-kernel/README.md)


<!-- FUN-WITH-EINSTEIN-2026 -->
### 🪐 Fun With Einstein — mathematical research lab
[Live interactive lab](https://nicholaskouns-create.github.io/fun-with-einstein/) · [Python, Lean, Coq certificate sources](https://github.com/nicholaskouns-create/E47-Kartekeya/tree/main/docs/fun-with-einstein) · [Continuous integration](https://github.com/nicholaskouns-create/E47-Kartekeya/actions/workflows/fun-with-einstein.yml)

Exact C₅ ratio φ⁻², E₄₇ rank-47 projector, 250D ancilla measurement and separately scoped stationary Einstein recovery.
<!-- /FUN-WITH-EINSTEIN-2026 -->


---

### Interactive E₄₇ spectral geometry (computed)

[**Open the standalone E₄₇ 3D visualizer**](./e47-geometry/index.html) · [**Open on GitHub Pages**](https://nicholaskouns-create.github.io/E47-Electroweak-Identities/e47-geometry/)

An additive, mobile-friendly research instrument showing the 125-site product-spin lattice, the exact 47-dimensional projector-density field (125 rational samples with denominator 315), five orthogonal axial slices, the seven SU(2) spectral sectors, optimal contraction Γ* = I − K²/99144 and the five-stage exact polynomial projector. The volumetric embedding is a coordinate visualization, not a claim that E₄₇ is a physical three-dimensional solid. No existing instruments are replaced.


<!-- ΩBA-PROOF-LINK-20261124 -->
### ΩBA · First-Principles Triadic Contraction and E₄₇ Continuity

[**Open the light-mode interactive ΩBA proof plate**](https://nicholaskouns-create.github.io/omega-ba/) · [Local Unicode derivation](omega-ba/README.md) · [Executable NumPy validation](omega-ba/omega_ba_validation.py) · [Local interactive page](omega-ba/index.html).

A mathematical three-stage alignment → binding → commitment map (𝒪=A∘B∘Ω), Banach strict-contraction proof with explicit assumptions, and a distinct E₄₇ spectral complement contraction (125→47, rate 15/17). Python tests and evidence boundaries are supplied; acoustic, biological and retrocausal effects are not asserted.
<!-- /ΩBA-PROOF-LINK-20261124 -->

## E₄₇ and the Standard Model

[Gauge and matter derivation](https://nicholaskouns-create.github.io/E47-Electroweak-Identities/standard-model/) · [Runnable Python validation](standard-model/validate.py) · [Read the page source](standard-model/index.html)

Pair exchange gives the gauge subgroup. Choosing the exterior-square matter module recovers one generation’s gauge representations. The page includes the assumptions, anomaly sums, Yukawa charge checks, and executed Python output.
