import lightkurve as lk

def download_lc(target):

    search = lk.search_lightcurve(
        target,
        mission="TESS"
    )

    lc = search.download()

    return lc
