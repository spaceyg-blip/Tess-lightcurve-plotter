from src.download_lightcurve import download_lc
from src.plot_lightcurve import plot_lc

target = "AB Dor"

lc = download_lc(
    target
)

plot_lc(
    lc
)
