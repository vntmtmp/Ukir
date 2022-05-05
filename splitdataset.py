# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:17:54 2022

@author: vntm
"""

import splitfolders  # or import split_folders

input_folder = 'D:/SKRIPSI/Program/Test(2)/Dataset/'

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
#Train, val, test
splitfolders.ratio(input_folder, output="D:/SKRIPSI/Program/Test(2)/Dataset_split", 
                   seed=42, ratio=(.8, .2), 
                   group_prefix=None) # default values


# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
# enable oversampling of imbalanced datasets, works only with fixed