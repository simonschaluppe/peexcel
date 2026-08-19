from matplotlib.colors import LinearSegmentedColormap


BALANCE_CMAP = LinearSegmentedColormap.from_list(
    "pexl_balance",
    [
        "red",
        "white",
        "lightgreen",
        "green",
        "darkgreen",
        "black",
        "black",
        "black",
        "black",
        "darkgreen",
        "green",
        "lightgreen",
        "white",
        "red",
    ],
    N=17,
)