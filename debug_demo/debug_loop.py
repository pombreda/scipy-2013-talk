# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:13:10 2013

"""

for idx in xrange(1, len(data_in)):
    # Insert data processing here
    new_data = data_in[idx - 1] + data_in[idx]
    data_out[idx] = new_data
