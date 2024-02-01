# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:03:02 2024

@author: quagscoped

This is a library file, feel free to read the function descriptions.
"""

import pandas as pd

def filter_by_key(creatures_dataset, *filters):
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
        creatures_dataset[column].apply(lambda x: term in str(x))
        for column, term in filters
    ]
    return creatures_dataset[(pd.concat(conditions, axis=1).sum(axis=1) > 0)]

def filter_out_key(creatures_dataset, *filters):
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
        creatures_dataset[column].apply(lambda x: term in str(x))
        for column, term in filters
    ]
    return creatures_dataset[~(pd.concat(conditions, axis=1).any(axis=1))]