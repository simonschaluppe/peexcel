

import matplotlib.pyplot as plt
import numpy as np

from utils.targets import ZQSynergy


def xy_balance_plot(
        ax,
        xmax=200,
        dx=10,
        ymax=200,
        dy=10
):
    #plot targets
    gfzs = np.array([0,0.2,0.4,0.6, 0.8,
                     1.,1.25,1.5,1.75,
                     2.,2.5,3,4,6])
    target_class = ZQSynergy()
    targets = target_class.alpha_zielwert_bgf(gfzs)
    for dy in targets:
        x, y = target_line(dy, xmax, ymax)
        ax.plot(x,y,"--", color="grey",label="asdsad")
        #TODO: annotate lines with gfz


    #plot points
    x = [140,110,80, 60, 55, 51]
    y = [0,0,20, 30, 35, 35]
    ax.plot(x,y,"o--", label="asdsad")


    # axis formatting
    ax.set(ylim=(0,ymax))
    ax.set(xlim=(0,xmax))
    ax.set(ylabel="PED Primary Energy Export $[kWh/m²_{GFA}]$")
    ax.set(xlabel="PED Primary Energy Import $[kWh/m²_{GFA}]$")
    #TODO: noborder
    #TODO: draw x and y axis as arrows


def target_line(
        offset:float,
        xmax=100,
        ymax=100,
):
    x = np.arange(0, xmax, 10)
    y = np.arange(0, ymax, 10) + offset
    return x, y


if __name__ == "__main__":
    fig, ax = plt.subplots(1,1, figsize=(6,6))
    xy_balance_plot(ax)
    fig.show()

