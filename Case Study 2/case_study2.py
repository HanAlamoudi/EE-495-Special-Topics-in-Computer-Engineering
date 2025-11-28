# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:55:07 2021

@author: Haneen Alamoudi
ID: 1708436
"""

from scipy.stats import chi2_contingency

data =[[207, 282, 241], [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)

alpha = 0.05
print("p value is " + str(p));
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (reject H0)')

