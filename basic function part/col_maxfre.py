# -*- coding: utf-8 -*-
"""
Created on Thu May 05 17:48:17 2016

@author: Spock
"""
def col_maxfre(col):
    freqmax=0; maxi=0;
    for item in col:
        if (col.count(item)>freqmax and item!="?"):
            freqmax=col.count(item)
            maxi=item
    return maxi

    
