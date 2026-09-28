# E47 Electroweak Identities

Frozen first-principles instrument. 28 September 2026.

**Not a fit. Not a look-elsewhere p-value.**

$$
K=(C-6I)(C-30I),\qquad
\dim E_{47}=47,\qquad
\Omega_c=\frac{47}{125}
$$

$$
m_Z^{(0)}=v\,\Omega_c,\qquad
\frac{m_W}{m_Z}=\sqrt{\frac{10}{13}},\qquad
\frac{m_t}{m_H}=1+\Omega_c=\frac{172}{125}
$$

Sole dimensionful input: $G_F$ from the muon lifetime.

| Field | Value |
|---|---|
| Status | FROZEN |
| Author | Nicholas S. Kouns |
| Affiliation | AIMS Research Institute |
| $v$ | $246.21964023926205\,\mathrm{GeV}$ |
| $m_Z^{(0)}$ | $92.57858472996253\,\mathrm{GeV}$ |
| $m_W^{(0)}$ | $81.19679015350891\,\mathrm{GeV}$ |
| $m_W/m_Z$ | $0.8770580193070292$ |
| $m_t/m_H$ | $1.376$ |
| Generator SHA-256 | `a4f692a05209aded64e53261db303155a055af81f5f0682ee89b9365b7620f6c` |
| Look-elsewhere | not computed, not claimed |

## Repository map

| Path | Role |
|---|---|
| [docs/E47_Electroweak_and_Mass_Ladder_Recovery.md](docs/E47_Electroweak_and_Mass_Ladder_Recovery.md) | symbolic proof |
| [docs/identities.md](docs/identities.md) | CERN-facing three-line instrument |
| [src/e47_electroweak_identities.py](src/e47_electroweak_identities.py) | canonical generator |
| [src/e47_electroweak_lock.json](src/e47_electroweak_lock.json) | machine lock |
| [index.html](index.html) | Pages surface |

## Headline residuals

| Identity | E47 | Measured | Residual |
|---|---|---|---|
| $m_Z/v=\Omega_c$ | $0.376$ | $0.370352$ | $+1.525\%$ |
| $m_W/m_Z$ | $0.877058$ | $0.881357$ | $-0.488\%$ |
| $m_t/m_H$ | $1.376$ | $1.378355$ | $-0.171\%$ |

The integer-$246$ fifteen-row table is **audit only**. $c(3\,\mathrm{GeV})$ has no recovered generator in the locked dictionary.

## Run

```bash
python3 src/e47_electroweak_identities.py
```

## Related City surfaces

- Executable City: [E47-Kartekeya](https://github.com/nicholaskouns-create/E47-Kartekeya)
- Root atlas: [nicholaskouns-create.github.io](https://nicholaskouns-create.github.io/)
- Foundry plate: [E47-Foundry-Lifetime-Intersection](https://github.com/nicholaskouns-create/E47-Foundry-Lifetime-Intersection)

Cite: N. S. Kouns, *E47 Electroweak Identities*, 28 September 2026, generator SHA-256 `a4f692a05209aded64e53261db303155a055af81f5f0682ee89b9365b7620f6c`.
