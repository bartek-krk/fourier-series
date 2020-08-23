# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:48:29 2020
@author: Bartosz Lukasik

@param formula - formula under the summation sign
@param a0 - constant
@param rank - number of summed sines
@param border - symmetrical leftmost and rightmost expansion border
"""

from numpy import sin, cos, pi, linspace
from matplotlib.pyplot import figure, plot, grid, title, savefig
from imageio import imread, mimsave
from os import mkdir, path, getcwd
from shutil import rmtree
from subprocess import call

def fourier(aRank,t):
    coefs = list()
    for k in range(1,aRank+1):
        formula = ((-cos(k*pi)+1)/k)*sin(k*t)
        coefs.append(formula)
        
    sines = list()
    a0 = pi
    
    for i in range(0,len(coefs[0])):
        buffer = list()
        for j in range(0,len(coefs)):
            buffer.append(coefs[j][i])
        sines.append(a0/2+sum(buffer))
        buffer.clear()
    return sines


        
border = pi

x = linspace(-border,border)

rank = 60

if path.exists(getcwd() + '\\fourier\\'):
    rmtree(getcwd() + '\\fourier\\')
mkdir(getcwd() + '\\fourier\\')

for r in range(1,rank+1):
    a = fourier(r,x)
    figure()
    plot(x,a,'r-')
    grid()
    title('k = ' + str(r))
    savefig(getcwd() + '\\fourier\\'+ str(r) + ".png")

filenames = list()

for i in range(1,rank+1):
    filenames.append(str(i) + '.png')
    
images = list()

for filename in filenames:
    images.append(imread(getcwd() + '\\fourier\\' + str(filename)))

mimsave(getcwd() + '\\fourier\\animation.gif', images, duration=0.1)

call(getcwd() + '\\fourier\\animation.gif', shell=True)