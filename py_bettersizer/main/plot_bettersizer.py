#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:59:26 2021

@author: tobias
"""


def plot_sd(path, save=False):
    """
    Plot the size bettersizer distribution contained in .xls file

    Parameters
    ----------
    path : str
        Path of bettersiter .xls file.
    save : bool or str
        Decide if plot should be saved. You can choose False/True or enter a custom file path.

    Returns
    -------
    fig : plt.figure
        Output figure.

    """
    import matplotlib.pyplot as plt
    import py_bettersizer
    
    xls_dict = py_bettersizer.read_bettersizer_data(path)
    (metadata, analysis, data) = xls_dict.values()
        
    fig = plt.figure()
    fig.suptitle("Bettersizer size distribution")
    
    ax = fig.add_subplot(111)
    ax.set_title(path)
    
    ax.set_ylabel('Fraction of total number in bin [%]', color='orange')
    ax.set_xlabel('Diameter [µm]')
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(which='major')
    ax.grid(which='minor', axis='both', ls=':')
    
    ax.bar(data['Diam um'], data['Diff%'], width=data['dp_um_upper'] - data['dp_um_lower'],
           edgecolor='k', lw=0.5, alpha=1, color='orange')
    ax.plot(data['Diam um'], data['Diff%'], c='green')
    
    ax2 = ax.twinx()
    ax2.set_ylabel('Cumulative fraction [%]', color='purple')
    ax2.plot(data['Diam um'], data['Cum%'], c='purple', marker='.')
    ax2.set_ylim(bottom=0)
    
    if save:
        from pathlib import Path
        
        if type(save) == str:
            save_path = Path(save)
        elif save is True:
            filename = path.split('/')[-1].rsplit('.', 1)[0]
            save_path = Path(f'./output/fig/{filename}.png')
        
        if not save_path.parent.exists():
            save_path.mkdir(parents=True)
        
        fig.savefig(save_path)
    
    plt.show()
    
    return fig
