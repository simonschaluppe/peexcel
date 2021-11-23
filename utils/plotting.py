

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from utils.targets import ZQSynergy


def target_of_gfz(ax, df, ylims=(-75,150), xlims=(0,8), no_legend=False, **kwargs):
    if type(df) is pd.DataFrame:
        if no_legend: # names with leading underscore dont show
            df.columns = ["_" + col for col in df.columns]
    df.plot(ax=ax, **kwargs) #linestyle, linewidth, etc
    ax.set_ylim(*ylims); ax.set_xlim(*xlims)
    ax.set_xlabel("Geschoßflächenzahl [-]")
    ax.grid()

def plot_context_factor(ax, df, ylims=(-75,150), xlims=(0,5), no_legend=False, **kwargs):
    if no_legend: # names with leading underscore dont show
        df.columns = ["_" + col for col in df.columns]
    df.plot(ax=ax, linestyle="solid", linewidth=1.3, **kwargs)
    ax.set_ylim(*ylims); ax.set_xlim(*xlims)
    ax.set_xlabel("Floor space index")
    ax.grid()

    #ax.legend(title='', bbox_to_anchor=(1, 1), loc='upper left')

def xy_balance_plot(
        ax,
        xmax=200,
        dx=10,
        ymax=200,
        dy=10
):
    #plot targets
    gfzs = np.array([0,0.2,0.4,0.6, 0.8,
                     1.,1.5,
                     2.,3,5])
    target_class = ZQSynergy()
    targets = target_class.alpha_zielwert_bgf(gfzs)
    for gfz,dy in zip(gfzs,targets):
        tx, ty = target_line(dy, xmax, ymax)
        ax.plot(tx,ty,"--",
                linewidth=0.5,
                color="grey",
                )
        ax.text(xmax*0.5-dy/2, xmax*0.75-xmax*0.25+dy/2,f"FSI {round(gfz,2)}", size=7, rotation=45)
        ax.text(xmax*0.5-dy/2+20, xmax*0.75-xmax*0.25+dy/2+20,f"target {round(dy,2)}", size=5, rotation=45)
        #TODO: annotate lines with gfz


    #plot points



    # axis formatting
    ax.set(ylim=(0,ymax))
    ax.set(xlim=(0,xmax))
    ax.set(ylabel="PED Primary Energy Export $[kWh/m²_{GFA}]$")
    ax.set(xlabel="PED Primary Energy Import $[kWh/m²_{GFA}]$")
    #TODO: noborderK
    #TODO: draw x and y axis as arrows


def target_line(
        offset:float,
        xmax=100,
        ymax=100,
):
    x = np.arange(0, xmax, 10)
    y = np.arange(0, ymax, 10) + offset
    return x, y

def example_xy_balance():
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    xy_balance_plot(ax)

    x = [[140, 110, 80, 60, 55, 51]],
    y = [0, 0, 20, 30, 35, 35],
    ax.plot(x, y, "--ob", linewidth=2, linestyle="dashed")
    fig.show()

def demand_supply_balance(ax, data_dict, title=None):
    """
    :param ax: the matplotlib ax to draw on
    :param data_dict: dictionary with keys "demand"=[vals], "supply"=[supplies]
    :param title: string
    :return:
    """
    abs=0
    for l, x in data_dict["demand"].items():
        ax.bar(data_dict.keys(), [x, 0], bottom=abs, label=l)
        abs += x
        # print(f"plotting {l=}, {x=}")

    abs=0
    for l, x in data_dict["supply"].items():
        ax.bar(data_dict.keys(), [0, x], bottom=abs, label=l)
        abs += x

    ax.set(title=title)


def example_demand_supply_bars():
    balances = [
        dict(
            demand=dict(HVAC=45, Plugloads=33, Other=10),
            supply=dict(PeakShaving=8.1, PVdirectuse=50, PV_grid_offset=20, densitycontext=20)
        ),
        dict(
            demand=dict(HVAC=25, Plugloads=33, Other=5),
            supply=dict(PeakShaving=8.1, PVdirectuse=15, PV_grid_offset=20, densitycontext=20)
        )
    ]

    fig, ax = plt.subplots(1, len(balances), figsize=(6, 6), sharey=True)
    for i, balance in enumerate(balances):
        demand_supply_balance(ax[i], balance)

    ax[-1].legend()

    fig.show()

def peb_series(ax, data, series, var_name):
    ax.plot(np.arange(series), var_name,
            data=data, linestyle='-', marker='o')

if __name__ == "__main__":
    example_demand_supply_bars()



