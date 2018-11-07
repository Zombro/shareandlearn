# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 17:56:44 2018
@author: kevzo
"""

import re
import random
from nltk.tokenize import wordpunct_tokenize


# simple, starting example
sample = '''For the problem of variable selection in generalized linear models, we develop various
adaptive Bayesian criteria. Using a hierarchical mixture setup for model uncertainty,
combined with an integrated Laplace approximation, we derive Empirical Bayes and
Fully Bayes criteria that can be computed easily and quickly. The performance of these
criteria is assessed via simulation and compared to other criteria such as AIC and BIC
on normal, logistic and Poisson regression model classes. A Fully Bayes criterion based
on a restricted region hyperprior seems to be the most promising.'''

tokens = wordpunct_tokenize(sample)
# beginner simplification : eliminate all punctuation and capitalization
f = [i.lower() for i in tokens if re.search('\\w', i)]
g = {i for i in f}
flat = ' '.join(f)
norm = {i: len(re.findall(i, flat)) for i in g}
markov = {}
i = 0
j = len(f)
# the LAST WORD needs some special handling...
for i in range(j-1):
    a = f[i]
    b = f[i+1]
    if a not in markov:
        markov[a] = {b: 1}
    else:
        if b in markov[a]:
            markov[a][b] += 1
        else:
            markov[a][b] = 1


def test():
    ret = [random.choice(list(markov.keys()))]
    for i in range(50):
        ret.append(random.choice(list(markov[ret[-1]].keys())))
    return ret


r = test()
print(' '.join(r))
