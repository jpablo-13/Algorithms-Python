#!/usr/bin/python

#find the greatest common denominator of two numbers
#using Euclid's algorithm

def gcd(a,b):
    
    while b!=0:
        t = a # t= 50
        a = b # a = 150
        b = t%b #b = 50 % 150
    return a


x = 50
y = 150

print(gcd(x,y))
        

