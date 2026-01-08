# ======================================================
# Reference:
# Applied Base Information Theory (TAIB)
# Zenodo DOI: https://doi.org/10.5281/zenodo.18171045
# ======================================================
import numpy as np
import matplotlib.pyplot as plt
import csv

# ------------------------------------------------------
# Plot configuration (paper-oriented)
# ------------------------------------------------------
def set_plot_style():
    plt.style.use("seaborn-v0_8-paper")
    plt.rcParams.update({
        "font.family": "serif",
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 7,
        "figure.figsize": (7, 4.5),
        "figure.dpi": 200,
        "savefig.dpi": 300,
    })

# ------------------------------------------------------
# TAIB parameters
# ------------------------------------------------------
a = 2.9e-122
epsilon = 4.28
tau_0 = 1.0

def eml_latency(f_loc):
    return tau_0 * (1.0 + (1.0 / epsilon) * np.log1p(f_loc / a))

# ------------------------------------------------------
# Dataset container
# ------------------------------------------------------
DATASET = []

def record_row(test_id, p1, p2, ref, taib, delta, sigma, aux1=None, aux2=None):
    DATASET.append([
        test_id, p1, p2, ref, taib, delta, sigma, aux1, aux2
    ])

# ------------------------------------------------------
# Test 1: Kerr deflection
# ------------------------------------------------------
def run_kerr_test():
    set_plot_style()

    b_vals = [3.0, 5.0, 10.0, 20.0, 50.0]
    spin = 0.9
    ref_vals, taib_vals = [], []

    for b in b_vals:
        f = (1.0 / b**2) * (1.0 - spin / b)
        lat = eml_latency(f)

        taib_defl = (4.0 / b) * (lat / tau_0)
        ref_defl = 4.0 / b
        delta = abs((taib_defl - ref_defl) / ref_defl) * 100.0
        sigma = f / a

        record_row("KERR", b, spin, ref_defl, taib_defl, delta, sigma)
        ref_vals.append(ref_defl)
        taib_vals.append(taib_defl)

    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(b_vals, taib_vals, "o-", label="TAIB")
    ax.plot(b_vals, ref_vals, "--", label="GR reference")
    ax.set_yscale("log")
    ax.set_xlabel("Impact parameter b (Rs)")
    ax.set_ylabel("Deflection (rad)")
    ax.set_title("Kerr deflection benchmark")
    ax.legend()
    ax.grid(alpha=0.2)
    plt.show()

# ------------------------------------------------------
# Test 2: Cosmic void response
# ------------------------------------------------------
def run_void_test():
    radii = [10, 20, 30, 40, 50]

    for r in radii:
        f = a * 0.1
        lat = eml_latency(f)
        ref = -(r**2) * 1e-6
        delta = abs((lat - abs(ref)) / abs(ref)) * 100.0
        sigma = f / a

        record_row("VOID", r, None, ref, lat, delta, sigma)

# ------------------------------------------------------
# Test 3: Entanglement limit
# ------------------------------------------------------
def run_bell_test():
    set_plot_style()

    distances = np.logspace(10, 40, 6)
    fidelities = []

    for d in distances:
        lat = (d / tau_0) * (a * epsilon)
        fid = np.exp(-lat)
        sigma = lat / a

        record_row("BELL", d, None, None, fid, 0.0, sigma)
        fidelities.append(fid)

    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(distances, fidelities, "o-")
    ax.set_xscale("log")
    ax.set_xlabel("Distance (Lp)")
    ax.set_ylabel("Fidelity")
    ax.set_title("Entanglement coherence limit")
    ax.grid(alpha=0.2)
    plt.show()

# ------------------------------------------------------
# Test 4: Shapiro delay analogue
# ------------------------------------------------------
def run_shapiro_test():
    distances = [1, 2, 5, 10]

    for d in distances:
        f = 1.0 / d**2
        lat = eml_latency(f) - tau_0
        delta = (lat / tau_0) * 100.0
        sigma = f / a

        record_row("SHAPIRO", d, None, 0.0, lat, delta, sigma)

# ------------------------------------------------------
# Test 5: N-qubit scalability
# ------------------------------------------------------
def run_qubit_test():
    set_plot_style()

    qubits = [2, 10, 50, 100, 1000]
    coh_times = []

    for n in qubits:
        f = n * a * epsilon
        t_coh = 1.0 / (f * 1e120 + 1e-12)
        sigma = f / a

        record_row("QUBITS", n, N_

