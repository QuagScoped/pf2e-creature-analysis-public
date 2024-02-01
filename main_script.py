# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:49:48 2024

@author: Alexander

Steps to using this file:
1. Define working directory with path=""
2.
"""

# change working directory to import
import sys
path = r"C:\Users\Alexander\Desktop\Code Projects\pf2e-creature-analysis-public"
sys.path.append(path)

# function imports
from functions import *

# library imports
import pandas as pd

# global file imports
creature_stats = pd.read_excel("./datasets/all_books_creatures.xlsx")

def filter_by_key(*filters):
    '''
    Parameters
    ----------
    *filters : the keywords (traits/languages/source/immunities) of the creatures you want to keep
    format as ("keyword type", keyword1), ("keyword type", keyword2)

    Returns
    -------
    the list of creatures matching the traits you want to filter by
    '''
    return creature_stats[
        any(
            creature_stats[column].apply(lambda x: term in str(x))
            for column, term in filters
        )
    ]

def main():
    
    # local file imports
    saves_by_level = pd.read_excel("./datasets/saves_by_level.xlsx")
    saves_by_level_rel = pd.read_excel("./datasets/saves_by_level_rel.xlsx")

    ac_by_level = pd.read_excel("./datasets/ac_by_level.xlsx")
    ac_by_level_rel = pd.read_excel("./datasets/ac_by_level_rel.xlsx")
    
    mods_by_level = pd.read_excel("./datasets/abilities_by_level.xlsx")
    mods_by_level_rel = pd.read_excel("./datasets/abilities_by_level_rel.xlsx")
   
    # calling functions
    
    plot_perlevel()
    
    print("This is the main program")

if __name__ == '__main__':
    main()