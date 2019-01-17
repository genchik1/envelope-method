# code: utf-8
import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.optimize import curve_fit


data = pd.read_csv('data/train_dataset.tsv', sep='\t', index_col=None, header=0)
# print (data.head())

axes_x = data['0'].values
# print (axes_x)

t_1_up = [493, 609, 763, 1100]
t_1_down = [469, 540, 658, 901, ]

t_2_up = [505, 576, 684, 880]
t_2_down = [517, 607, 764, 1046]

t_3_up = [531, 607, 729, 948]
t_3_down = [486, 553, 656, 823, 1100]

t_4_up = [511, 611, 764, 1100]
t_4_down = [538, 657, 900]

t_5_up = [506, 580, 683, 882]
t_5_down = [515, 608, 767, 1040]


# graph 1

# g_2_up = data[data['0'].isin(t_2_up)][['0', '2']]
# g_2_down = data[data['0'].isin(t_2_down)][['0', '2']]

# T_up = np.array(g_2_up['0'].values)
# power_up = np.array(g_2_up['2'].values)

# xnew_up = np.linspace(T_up.min(), T_up.max(), 100)
# power_smooth_up = spline(T_up, power_up, xnew_up, order=2)

# T_down = np.array(g_2_down['0'].values)
# power_down = np.array(g_2_down['2'].values)

# xnew_down = np.linspace(T_down.min(), T_down.max(), 100)
# power_smooth_down = spline(T_down, power_down, xnew_down, order=2)

# def c():

    
def func(x, a, b, c, d):
    return a + b/(x*x) + c/(x*x*x*x)
    # return a * np.exp(-b * x) + c

g_1_up = data[data['0'].isin(t_1_up)][['0', '1']]

T_up = np.array(g_1_up['0'].values)
xdata = np.linspace(T_up.min(), T_up.max(), 911)

y = func(xdata, *t_1_up)
y_noise = np.array(data['1'].values)
ydata = y + y_noise

popt, pcov = curve_fit(func, xdata, ydata)
print (popt)
popt = popt - 450
print (popt)

fig, ax = plt.subplots()
ax.plot(xdata, func(xdata, *popt))
ax.plot(data['0'].values, data['1'].values)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
plt.show()