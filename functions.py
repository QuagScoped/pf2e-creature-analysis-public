# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 01:25:51 2024

@author: quagscoped

This is a library file, you should not be here.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_per_level(creatures_dataset, stat, correction_data):
    
    # taking mean per level and subtracting moderate values
    mean_per_level = creatures_dataset.groupby("Level")[stat].mean().reset_index()
    merged_filter = pd.merge(mean_per_level, correction_data[["Level", "Moderate"]], on="Level", how="left")
    merged_filter[stat] -= merged_filter["Moderate"]
    
    plt.plot(merged_filter["Level"], merged_filter[stat], ".", label=f"Mean {stat} of filtered creatures.", markersize=14)

