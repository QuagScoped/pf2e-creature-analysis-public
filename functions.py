# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:25:51 2024

@author: quagscoped

This is a library file, you should not be here.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_per_level(creatures_dataset, stat, correction_data):
    '''
    Parameters
    ----------
    creatures_dataset : Pandas dataset of creature statistics, either filtered or not.
    stat : The stat you want to find the mean per level of. Choose between AC, saves or ability modifiers.
    correction_data : The dataset per level of the stat you want to analyse.
    Usually saves_by_level_rel, ac_by_level_rel or mods_by_level_rel.

    Returns
    -------
    None, but plots mean creature statistic per level of creature_dataset.
    '''
    # taking mean per level and subtracting moderate values
    mean_per_level = creatures_dataset.groupby("Level")[stat].mean().reset_index()
    merged_filter = pd.merge(mean_per_level, correction_data[["Level", "Moderate"]], on="Level", how="left")
    merged_filter[stat] -= merged_filter["Moderate"]
    
    plt.plot(merged_filter["Level"], merged_filter[stat], ".", label=f"Mean {stat} of filtered creatures", markersize=14)

def baseline(baseline_data):
    '''
    Parameters
    ----------
    baseline_data : The relative dataset per level of the stat you want to plot.
    Usually saves_by_level_rel, ac_by_level_rel or mods_by_level_rel.

    Returns
    -------
    None, but plots horizontal line at y=0 to represent moderate baseline.
    '''
    plt.plot(baseline_data["Level"], baseline_data["Moderate"], "k", label="Moderate baseline (GMG)", markersize=14)
