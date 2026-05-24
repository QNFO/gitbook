---
ISNI: 0000000526456062
author: Rowan Brad Quni
email: rowan.quni@qnfo.org
website: http://qnfo.org
ORCID: https://orcid.org/0009-0002-4317-5604
robots: By accessing this content, you agree to https://qnfo.org/LICENSE. Non-commercial use only. Attribution required.
DC.rights: https://qnfo.org/LICENSE. Users are bound by terms upon access.
created: 2025-04-22T05:05:54Z
modified: 2025-05-09T03:21:53Z
title: 8 References
aliases: [References]
---

# References

Axelrod, R. (1997). *The complexity of cooperation: Agent-based models of competition and collaboration*. Princeton University Press.

Bailey, D. H., Borwein, J. M., & Stodden, V. (2015). Set the default to “published”: Reproducibility in computational science. *Notices of the American Mathematical Society*, *62*(6), 642-645.

Buchberger, B., & Collins, G. E. (Eds.). (1982). *Computer algebra: Symbolic and algebraic computation*. Springer-Verlag.

Crane, M. (2018). Questionable answers in numerical computation. *American Scientist*, *106*(3), 166-173.

Fousse, L., Hanrot, G., Lefèvre, V., Pélissier, P., & Zimmermann, P. (2007). MPFR: A multiple-precision binary floating-point library with correct rounding. *ACM Transactions on Mathematical Software (TOMS)*, *33*(2), 13.

Grebogi, C., Ott, E., & Yorke, J. A. (1987). Chaos, strange attractors, and fractal basin boundaries in nonlinear dynamics. *Science*, *238*(4827), 632–638.

Humphreys, P. (2004). *Extending ourselves: Computational science, empiricism, and scientific method*. Oxford University Press.

Hutson, M. (2018). Artificial intelligence faces reproducibility crisis. *Science*, *359*(6377), 725-726.

IEEE. (1985). *IEEE Standard for Binary Floating-Point Arithmetic* (ANSI/IEEE Std 754-1985). Institute of Electrical and Electronics Engineers.

IEEE. (2008). *IEEE Standard for Floating-Point Arithmetic* (IEEE Std 754-2008). Institute of Electrical and Electronics Engineers.

IEEE. (2019). *IEEE Standard for Floating-Point Arithmetic* (IEEE Std 754-2019). Institute of Electrical and Electronics Engineers.

Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, *20*(2), 130–141.

Moore, R. E. (1966). *Interval analysis*. Prentice-Hall.

Parker, W. S. (2009). Does matter really matter? Computer simulations, experiments, and materiality. *Synthese*, *169*(3), 483–496.

Peng, R. D. (2011). Reproducible research in computational science. *Science*, *334*(6060), 1226–1227.

Penrose, R. (1989). *The emperor’s new mind: Concerning computers, minds, and the laws of physics*. Oxford University Press.

Sauer, T., Yorke, J. A., & Casdagli, M. (1991). Embedology. *Journal of Statistical Physics*, *65*(3-4), 579–616.

Schmidhuber, J. (1997). A computer scientist’s view of life, the universe, and everything. In C. Freksa, M. Jantzen, & R. Valk (Eds.), *Foundations of Computer Science*

Turing, A. M. (1948). Rounding-off errors in matrix processes. The Quarterly Journal of Mechanics and Applied Mathematics, 1(1), 287–308.

von Neumann, J., & Goldstine, H. H. (1947). Numerical inverting of matrices of high order. Bulletin of the American Mathematical Society, 53(11), 1021–1099.

Wilkinson, J. H. (1963). Rounding errors in algebraic processes. Prentice-Hall.

---

# Notes

1.  **Floating-Point Mechanics (Section 1.2, Section 1.3, Section 3):** The discussion of the IEEE 754 standard, the structure of floating-point numbers (sign, exponent, mantissa), finite precision, machine epsilon, ULP, representation error, rounding error, absorption, catastrophic cancellation, overflow/underflow, and special values relates directly to the details covered in [[0141_Floating_Point_Approximation]].

2.  **Core Concept of Implied Discretization (Section 1.2, Section 1.3):** The introduction and definition of “implied discretization” as the unavoidable granularity imposed by finite computation, distinct from explicit discretization (`dt`, `dx`), corresponds to the central theme of [[0143_Implied_Discretization]].

3.  **Risk of Artificial Quantization (Section 1.4, Section 4.1.1, Section 5.1.3):** The specific challenge highlighted regarding the potential for numerical artifacts (granularity, convergence limits) to mimic genuine physical quantization, particularly in the context of foundational theories aiming for emergent quantization (like IO/EQR), is the core issue addressed in [[0142_IO_Numerical_Quantization_Risk]]. The discussion of convergence testing as a mitigation strategy also relates back to this note.

4.  **Deeper Consequences and Mitigation (Section 3.3, Section 4, Section 5):** The detailed exploration of the consequences of implied discretization across various domains (error propagation, instability, impact on chaos, AI, physics simulations, etc.) and the critical evaluation of mitigation strategies (higher precision, alternative arithmetics, algorithmic choices, qualitative focus) align with the content of [[0144_Implied_Discretization_Deep_Dive]].

5.  **Fundamental Limits and Research Questions (Section 6, Section 7.5):** The discussion probing whether implied discretization points towards fundamental limits related to computability, Gödelian boundaries, the map-territory problem, and the limits of quantitative description corresponds to the research questions outlined in [[0145_RQ_Quantitative_Limits]]. The mention of Gödelian limits specifically connects to [[0013_Mathematical_Limits_Godel]].


---
*Published by [QNFO](https://github.com/QNFO) under the [QNFO Content License Agreement v1.1](https://github.com/QNFO/license). Non-commercial use only. Attribution required.*
*Original: 2025\00\Implied Discretization\8 References.md*
