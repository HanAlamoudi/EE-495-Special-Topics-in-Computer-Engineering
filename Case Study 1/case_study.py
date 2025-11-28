# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:06:26 2021

@author: Haneen Alamoudi
ID: 1708436
"""

import pandas as pd
import numpy as np

#Reading CSV file 
corona = pd.read_csv('Corona_Updated.csv')

corona['Temp_Cat'] = corona['Temprature'].apply(lambda x : 0 if x < 24 else 1)

corona_t = corona[['Confirmed', 'Temp_Cat']]

#main function to calculate two sample z test
def TwoSampZ(X1, X2, sigma1, sigma2, N1, N2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    ovr_sigma = sqrt(sigma1**2/N1 + sigma2**2/N2)
    z = (X1 - X2)/ovr_sigma
    pval = 2*(1 - norm.cdf(abs(z)))
    return z, pval

d1 = corona_t[(corona_t['Temp_Cat'] == 1)]['Confirmed']

d2 = corona_t[(corona_t['Temp_Cat']==0)]['Confirmed']

#calculate the mean
m1, m2 = d1.mean(), d2.mean()

#calculate the standard deviation
sd1, sd2 = d1.std(), d2.std()
n1,n2 = d1.shape[0], d2.shape[0]

#Calling the two sample z test fuction
z,p = TwoSampZ(m1, m2, sd1, sd2, n1, n2)

#save and round the z-score and p-value 
z_score = np.round(z,8)
p_val = np.round(p,6)

#final result of the test
if(p_val < 0.05):
    Hypothesis_Status =  'Reject Null Hypothesis : Significant'
else:
    Hypothesis_Status = 'Do Not Reject Null Hypothesis : Not Significant'

print(p_val)
print(Hypothesis_Status)

