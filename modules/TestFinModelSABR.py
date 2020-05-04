# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:10:12 2019

@author: Dominic
"""


from financepy.models.FinModelSABR import blackVolFromSABR





alpha = 0.28
beta = 1.0
rho = -0.09
nu = 0.21

f = 0.043
k = 0.050
t = 1.0


def test_SABR():

    print("ALPHA", "BETA", "RHO", "VOL")

    for alpha in [0.1, 0.2, 0.3]:
        for beta in [0.5, 1.0, 2.0]:
            for rho in [-0.8, 0.0, 0.8]:
                vol = blackVolFromSABR(alpha, beta, rho, nu, f, k, t)
                print(alpha, beta, rho, vol)


test_SABR()

