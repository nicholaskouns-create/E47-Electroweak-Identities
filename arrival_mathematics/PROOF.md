# Arrival Mathematics: Continuity, Variational Closure, and Spectral Convergence

This companion proof binds the E47 spectral core to a general residual-closure theorem.

For a linear residual R(x)=Ax with B=A†WA≥0 and positive spectrum in [Δ,M],

x_{n+1}=(I-εB)x_n → P_{ker A}x_0,

with optimal constant step ε*=2/(Δ+M) and q*=(M-Δ)/(M+Δ).

For the supplied spin-2 carrier V=V₂^{⊗3}, dim V=125, K_E=(C-6I)(C-30I),

E47=ker K_E=E6⊕E30,
dim E47=25+22=47,
Ωc=47/125=0.376.

With B=K_E², Δ=11664 and M=186624, so

Γ*=I-K_E²/99144,
q*=15/17,
||Γ*^n-P47||₂=(15/17)^n.

At n=220,

||Γ*^220-P47||₂≈1.0998014528×10^-12.

The executable validator also verifies a compatible zero-residual witness, the D→10 dimensional flow root λ10=1.075766066086837, the identity λ10^20=(λ10+1)^2≈4.30880476111762, and 256 random-state projections with maximum error ≈7.40×10^-13 and zero kernel drift to numerical precision.

Evidence boundary: these spectral and convergence statements are mathematical consequences of the stated carrier/operator definitions. Physical identifications of Q, Ω, m_eff, D, H_perp, H_i and equivalences among them require additional coupling laws and/or independent empirical validation.

Core statement:

**Arrival is projection onto the jointly invariant zero-residual manifold.**
