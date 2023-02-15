#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:18:22 2021

@author: tobias
"""
import numpy as np


def calc_channel_resolution(bin_diameter, mode='int'):
    """Calculate channel resolution (bins per decade)"""
    channel_resolution = len(bin_diameter) / (np.log10(max(bin_diameter)) - np.log10(min(bin_diameter)))
    
    if mode == 'int':
        channel_resolution = int(round(channel_resolution))
    
    return channel_resolution


def calc_bin_boundaries(bin_mean_diameter, channel_resolution):
    """Calculate lower and upper bin boundaries for a given mean diameter and channel resolution
    This calculation was derived using the expression 'dNdlogD = dN * channel_res'."""
    bin_lower_boundary = 2 * bin_mean_diameter / (10**(1 / channel_resolution) + 1)
    bin_upper_boundary = 2 * bin_mean_diameter / (10**(-1 / channel_resolution) + 1)
    return (bin_lower_boundary, bin_upper_boundary)
