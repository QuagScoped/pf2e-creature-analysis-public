# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:49:48 2024

@author: quagscoped

Steps to using this file:
1. Define working directory with path="" at the top
2. Go to the main() function along the bottom and follow the steps
3. Message quagscoped on discord if you have any questions
"""

# add directory path to import from
import sys
path = "C:/Users/Alexander/Desktop/Code Projects/pf2e-creature-analysis-public"
sys.path.append(path)

# function imports
from functions_plotting import plot_per_level
from functions_plotting import baseline

# library imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# global file imports
os.chdir(path)
creature_stats = pd.read_excel("./datasets/all_books_creatures.xlsx")

saves_by_level = pd.read_excel("./datasets/saves_by_level.xlsx")
saves_by_level_rel = pd.read_excel("./datasets/saves_by_level_rel.xlsx")

ac_by_level = pd.read_excel("./datasets/ac_by_level.xlsx")
ac_by_level_rel = pd.read_excel("./datasets/ac_by_level_rel.xlsx")
    
mods_by_level = pd.read_excel("./datasets/abilities_by_level.xlsx")
mods_by_level_rel = pd.read_excel("./datasets/abilities_by_level_rel.xlsx")

def filter_by_key(*filters):
    '''
    Parameters
    ----------
    *filters : the keywords (traits/languages/source/immunities/sizes) of the creatures you want to keep
    format as ("keyword type", keyword1), ("keyword type", keyword2)
    valid keywords: Traits, Languages, Source, Size, Immunities, Resistances, Weaknesses (and technically Name)

    Returns
    -------
    the list of creatures matching the traits you want to filter by
    '''
    conditions = [
        creature_stats[column].apply(lambda x: term in str(x))
        for column, term in filters
    ]
    return creature_stats[(pd.concat(conditions, axis=1).sum(axis=1) > 0)]

def filter_out_key(*filters):
    '''
    Parameters
    ----------
    *filters : the keywords (traits/languages/source/immunities/sizes) of the creatures you want to remove
    format as ("keyword type", keyword1), ("keyword type", keyword2)
    valid keywords: Traits, Languages, Source, Size, Immunities, Resistances, Weaknesses (and technically Name)

    Returns
    -------
    the list of creatures without the traits you want to filter by
    '''
    conditions = [
        creature_stats[column].apply(lambda x: term in str(x))
        for column, term in filters
    ]
    return creature_stats[~(pd.concat(conditions, axis=1).any(axis=1))]

def plot_settings():
    '''
    Edit plot settings here, or alternative save the figure by uncommenting plt.savefig().
    The default settings should be fine, but feel free to play around with them.
    '''
    textsize = 14
    
    plt.title("Insert short and descriptive title here.", fontsize=textsize)
    
    plt.xticks(np.arange(-1, 26, 2), fontsize=textsize)
    plt.xlabel("Creature level", fontsize=textsize)
    
    plt.yticks(fontsize=textsize)
    plt.ylabel("Insert y axis description here.", fontsize=textsize)
    
    plt.legend(fontsize=textsize)
    plt.grid()
    
    # plt.savefig("./testfig.png", dpi=250)
    plt.show()

def main():

    # creating an empty plot, change figsize if it is too big/small for your monitor
    plt.figure(figsize=(20, 12))
    
    # filter data here, example provided:
    keywords = (("Immunities", "mental"),
                ("Traits", "swarm"),
                ("Traits", "mindless")
        )
   
    filtered_creatures = filter_out_key(*keywords)
    
    # calling functions to plot, for stat try plotting out AC or saves
    plot_per_level(filtered_creatures, "Will", saves_by_level)
    
    # plotting baseline, always use relative data for this
    baseline(saves_by_level_rel)
        
    # showing the plot, look in the function plot_settings() above if you want to change anything and/or save it
    plot_settings()
    
if __name__ == '__main__':
    main()