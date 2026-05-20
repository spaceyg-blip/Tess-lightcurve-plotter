import matplotlib.pyplot as plt

def plot_lc(lc):

    plt.figure(figsize=(12,5))

    plt.plot(
        lc.time.value,
        lc.flux.value,
        linewidth=0.8
    )

    plt.xlabel(
        "Time (BTJD)"
    )

    plt.ylabel(
        "Flux"
    )

    plt.title(
        "TESS Light Curve : AB Dor"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/tess_lightcurve.png",
        dpi=300
    )

    plt.show()
