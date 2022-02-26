import math
import matplotlib.pyplot as plt
from statistics import NormalDist
import os
import sys

r = 0.01
q = 0
tau = 1

# current stock price, taken as the average of current bid and ask
S = (2694.1902+2686.5999)/2

def dplus(sigma,K):
    return (math.log(S/K)+(r-q+0.5*sigma**2)*tau)/math.sqrt(sigma**2*tau)

def dminus(sigma,K):
    return (math.log(S/K)+(r-q-0.5*sigma**2)*tau)/math.sqrt(sigma**2*tau)

def N(d):
    return NormalDist(mu=0, sigma=1).cdf(d)

def C(sigma,K):
    return S*(math.e**(-q*tau))*N(dplus(sigma,K))-K*(math.e**(-r*tau))*N(dminus(sigma,K))

# recursively divides intervals in half
def IV(price, K, high, low):
    if high-low<0.001:
        return high
    elif C((high+low)/2, K)>price:
        return IV(price, K, (high+low)/2, low)
    else:
        return IV(price, K, high, (high+low)/2)

# store values used to plot graph
arrmoneyness = []
arrIV = []

f = open(os.path.join(sys.path[0], 'goog_quotedata.csv'), encoding='utf-8')

# skip useless info
for i in range(4):
    f.readline()

# log moneyness between -0.2 and 0.2
lowK = S/(math.e**0.2)
highK = S*(math.e**0.2)

for row in f:
    line = row.split(',')
    strike = float(line[11])
    if strike<lowK or strike>highK:
        continue
    price = (float(line[4])+float(line[5]))/2
    arrmoneyness.append(math.log(strike/S))
    arrIV.append(IV(price, strike, 10, 0))

plt.scatter(arrmoneyness ,arrIV)
plt.xlabel('log(K/S)')
plt.ylabel('implied volatility')
plt.show()