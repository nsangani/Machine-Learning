# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:39:55 2022

@author: Sangani
"""


# Question 4

import numpy as np
from sklearn.decomposition import PCA

data = np.matrix('0 2; 2 4; 4 4; 5 4; 7 6')

pca = PCA(n_components  =2)
pca.fit(data)
pca.components_

