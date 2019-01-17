# code: utf-8
import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt


def open_data(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            # print (line)
            if '//' not in line and line != '\n':
                value = line.split(' ')
                if len(value)>1:
                    # print (value)
                    value_2 = []
                    for v in value:
                        if len(v)>0:
                            value_2.append(float(v))
                    if len(value_2)>0:
                        dict_of_data = {}
                        dict_of_data['lambda'] = value_2[0]
                        for i in range(1, len(value_2)):
                            dict_of_data['exp_'+str(i)] = value_2[i]
                        data.append(dict_of_data)
    data = pd.DataFrame(data)
    return data


def max_min(data, exp):
    df = data[['lambda', exp]].copy()
    n = []
    print (df.head())
    for row_index,row in df.iterrows():
        if row_index > 1 and row_index<len(df)-1:
            if row[exp]<df[exp].iloc[row_index-1] and row[exp]<df[exp].iloc[row_index+1] and row[exp]<df[exp].iloc[row_index-2] and row[exp]<df[exp].iloc[row_index+2]:
                n.append(row)
    n = pd.DataFrame(n)
    return n


def graphix(data, experiment, extremus=False):
    fig, ax = plt.subplots()
    for exp in experiment:
        if extremus:
            df = max_min(data, exp)
            ax.plot(df['lambda'], df[exp])
        ax.plot(data['lambda'], data[exp])
    ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
    plt.show()


if __name__ == "__main__":
    path = 'data/39_40_kvarts.sf'
    data = open_data(path)
    graphix(data, ['exp_1'], extremus=True)    #, 'exp_2', 'exp_3'