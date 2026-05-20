import matplotlib.pyplot as plt

def plot_lc(lc):

    plt.figure(figsize=(10,5))

    plt.plot(
        lc.time.value,
        lc.flux.value
    )

    plt.xlabel(
        "Time"
    )

    plt.ylabel(
        "Flux"
    )

    plt.title(
        "TESS Light Curve"
    )

    plt.show()
