# TAIB Stress-Test — Operational Benchmarks

This repository contains the benchmark suite, datasets, and reference scripts associated with the **TAIB Stress-Test**, an operational audit of the Applied Base Information Theory (TAIB).

The objective of this repository is to provide:
- Reproducible numerical benchmarks
- Unified datasets used in the TAIB stress-testing framework
- Reference implementations for latency, saturation, and coherence metrics
- Plotting routines used in the accompanying technical appendix

## Scope

The benchmarks explore five representative domains:

1. Kerr deflection and rotational asymmetry
2. Cosmic void evolution
3. Informational Shapiro delay
4. Multipartite entanglement limits (Bell-type scenarios)
5. Decoherence driven by system complexity (N-qubit scaling)

The focus is operational rather than interpretative: all results are generated from explicit algorithms and exported as traceable datasets.

## Repository Structure

/benchmarks
TAIB_BENCHMARKGitHub.py
/data
Dataset_S1.csv
/docs
TAIB_Stress_Test_Extended_Appendix.pdf


## Relation to the Main Paper
The theoretical foundations of TAIB are presented in the following paper:

**Applied Base Information Theory (TAIB): Operational Modeling of Information Flow in Cosmological and Quantum Systems**  
Zenodo:(https://doi.org/10.5281/zenodo.18171045)
Academia.edu: (https://www.academia.edu/145827156/The_Bus_Information_and_Latency_Theory_TAIB_An_Architectural_Reformulation_of_Physical_Dynamics)
This repository supports the theoretical paper available on Zenodo and Academia.edu.  
It provides the executable and data-level complement required for independent verification and peer audit.

## Reproducibility

All simulations are deterministic and can be executed with standard scientific Python tools:
- numpy
- matplotlib

No proprietary dependencies are required.

## License

This work is licensed under the **Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

Commercial use is **not** permitted under this license.  
Commercial licensing may be negotiated separately.

---

© 2025 — José Luis Gamio.
