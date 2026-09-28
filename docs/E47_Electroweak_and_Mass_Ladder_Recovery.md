# E47 Electroweak and Mass-Ladder Recovery

First-principles symbolic proof. Frozen 28 September 2026.

## Carrier and kernel

$$
V_2\cong\mathbb C^5,\qquad\mathcal H=V_2^{\otimes 3},\qquad\dim\mathcal H=5^3=125
$$

$$
J_a=J_a^{(2)}\otimes I\otimes I+I\otimes J_a^{(2)}\otimes I+I\otimes I\otimes J_a^{(2)},\qquad a\in\{x,y,z\}
$$

$$
C=J_x^2+J_y^2+J_z^2
$$

$$
V_2^{\otimes 3}\cong V_0\oplus 3V_1\oplus 5V_2\oplus 4V_3\oplus 3V_4\oplus 2V_5\oplus V_6
$$

$$
\operatorname{spec}(C)=\{0,2,6,12,20,30,42\}
$$

$$
\operatorname{mult}(C)=\{1,9,25,28,27,22,13\}
$$

$$
1+9+25+28+27+22+13=125
$$

$$
K=(C-6I)(C-30I)
$$

$$
\operatorname{spec}(K)=\{180,112,0,-108,-140,0,432\}
$$

$$
\ker K=E_6\oplus E_{30},\qquad\dim E_6=25,\qquad\dim E_{30}=22
$$

$$
E_{47}:=\ker K
$$

$$
\boxed{\dim E_{47}=25+22=47}
$$

$$
P_{47}=P_6+P_{30},\qquad P_{47}^2=P_{47},\qquad P_{47}^\dagger=P_{47},\qquad\operatorname{Tr}P_{47}=47
$$

$$
\boxed{\Omega_c=\operatorname{Tr}P_{47}/\dim\mathcal H=47/125=0.376}
$$

## Contraction

$$
K^2=(C-6I)^2(C-30I)^2
$$

$$
\operatorname{spec}(K^2)=\{32400,12544,0,11664,19600,0,186624\}
$$

$$
\Delta=\min(\operatorname{spec}(K^2)\setminus\{0\})=11664=108^2
$$

$$
\|K^2\|=186624=432^2,\qquad\kappa=16,\qquad\varepsilon_*=1/99144
$$

$$
\Gamma_*=I-\varepsilon_*K^2,\qquad\Gamma_*P_{47}=P_{47},\qquad\rho_*=15/17
$$

$$
\boxed{\Gamma_*^n\to P_{47}}
$$

## Electroweak identities

$$
G_F=1.1663788\times 10^{-5}\,\mathrm{GeV}^{-2}
$$

$$
\boxed{v=(\sqrt{2}G_F)^{-1/2}=246.21964023926205\,\mathrm{GeV}}
$$

$$
\boxed{m_Z^{(0)}=v\Omega_c=92.57858472996253\,\mathrm{GeV}}
$$

$$
\boxed{m_W/m_Z=\sqrt{10/13}=0.8770580193070292}
$$

$$
\boxed{m_W^{(0)}=81.19679015350891\,\mathrm{GeV}}
$$

$$
\boxed{m_t/m_H=1+\Omega_c=172/125=1.376}
$$

Headline residuals: $\delta_Z=+1.52496\%$, $\delta_{WZ}=-0.48779\%$, $\delta_{tH}=-0.17083\%$.

## Audit map (not the claim)

$$
v_{\mathbb Z}=246,\qquad\mathcal A_{246}\neq\mathcal I_{\mathrm{EW}}
$$

$$
H=125,\ t=172,\ Z=92.496,\ W\approx81.124,\ b=47/11,\ \tau=47^2/1250,\ c(m_c)=47/37
$$

$$
\mu=(78+27)\times10^{-3},\ s=94\times10^{-3},\ d=4.7\times10^{-3},\ u=(47/22)\times10^{-3},\ e=47^2/4320\times10^{-3}
$$

$$
m_{\nu_2}=(5/4)\sqrt{47}\,\mathrm{meV},\qquad m_{\nu_3}=47\cdot16/15\,\mathrm{meV}
$$

$$
c(3\,\mathrm{GeV})\notin\operatorname{Im}\mathcal A_{246},\qquad T_{\mathrm{obs}}=0.007692169\neq p_{\mathrm{LEE}}
$$

## PMNS and neutrino skeleton

$$
s_{13}^2=1/47,\quad s_{12}^2=15/49,\quad s_{23}^2=25/47,\quad\delta_{\mathrm{CP}}=16\pi/15
$$

$$
\boxed{\Delta m_{31}^2=2.51335\times10^{-3}\,\mathrm{eV}^2}
$$

(with $m_{\nu_1}=0$ on this one-mode plate).

## Closure

$$
\boxed{\mathcal I_{\mathrm{EW}}=(v\cdot47/125,\ \sqrt{10/13},\ 172/125)}
$$

$$
\boxed{\mathcal A_{246}\ \text{is audit-only},\qquad\mathcal I_{\mathrm{EW}}\ \text{is the frozen headline map}}
$$
