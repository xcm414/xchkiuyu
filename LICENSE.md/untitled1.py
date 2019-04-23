# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:02:45 2019

@author: Administrator
"""

from sklearn import linear_model
reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
reg.coef_
reg.intercept_ 