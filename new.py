# code: utf-8
import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.optimize import curve_fit


def C(y, y1, y2, x, x1, x2):
    Q1 = (y - y2)*(1-x*x/(x1*x1)) - (y-y1)*(1-x*x/(x2*x2))
    Q2 = (1/(x1*x1*x1*x1) - 1/(x*x*x*x))*(1-x*x/(x2*x2)) - (1/(x2*x2*x2*x2) - 1/(x*x*x*x))*(1-x*x/(x1*x1))
    return Q1/Q2


def B(y, y1, y2, x, x1, x2):
    Q1 = y - y1 + C(y, y1, y2, x, x1, x2)*(1/(x1*x1*x1*x1) - 1/(x*x*x*x))
    Q2 = 1/(x*x) - 1/(x1*x1)
    return Q1/Q2


def A(y, y1, y2, x, x1, x2):
    return B(y, y1, y2, x, x1, x2)/(x*x) + C(y, y1, y2, x, x1, x2)/(x*x*x*x) - y

def popts(*argv):
    return A(*argv), B(*argv), C(*argv)


def func(xdata, a, b, c):
    # return a*xdata*xdata + b*xdata + c
    # return a * np.exp(-b * xdata) + c
    return a + b/xdata*xdata + c/xdata*xdata*xdata*xdata


if __name__ == '__main__':
    data = pd.read_csv('data/train_dataset.tsv', sep='\t', index_col=None, header=0)

    t_1_up = [609, 763, 1100]        # 493,
    t_1_down = [540, 658, 901]      # 469,

    # up:
    up = data[data['0'].isin(t_1_up)][['0', '1']]

    popt = popts(*up['0'].values, *up['1'].values)

    fig, ax = plt.subplots()
    ax.plot(data['0'].values, func(data['0'].values, *popt))
    ax.plot(data['0'].values, data['1'].values)
    ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
    plt.show()