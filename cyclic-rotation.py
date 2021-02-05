# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:36:18 2021

@author: devbob2020

This function takes two arguements:
    'A' is an array to be shifted.
    
    'K' is an integer amount to shift the array in the 
    positive (right) or negative (left) direction.
"""

def solution(A, K):
    print(A)
    if len(A) == 0 or K == 0:
       return A
    if K > 0:
        for elem in range(K):
            temp = A.pop(-1)
            A.insert(0, temp)
            #print(A)
    elif K < 0:
        for elem in range(abs(K)):
            temp = A.pop(0)
            A.append(temp)
            #print(A)
    return A
