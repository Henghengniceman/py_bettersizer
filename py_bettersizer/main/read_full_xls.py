#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:04:59 2021

@author: tobias
"""


def read_bettersizer_data(path, add_bin_boundaries=True):
    """Wrapper to import all elements from bettersizer .xls sheet"""
    import py_bettersizer.lib.io.xls as io_xls
    import py_bettersizer.lib.sd.structure as sd_structure
    
    sd = io_xls.read_sd_data(path)
    if add_bin_boundaries:
        channel_resolution = sd_structure.calc_channel_resolution(sd['Diam um'])
        sd['dp_um_lower'], sd['dp_um_upper'] = sd_structure.calc_bin_boundaries(sd['Diam um'], channel_resolution)
    
    out_dict = dict()
    out_dict['metadata'] = io_xls.read_metadata(path)
    out_dict['metadata']['System status'] = io_xls.read_system_status(path)
    out_dict['analysis'] = io_xls.read_analysis_data(path)
    out_dict['sd'] = sd
    
    return out_dict
