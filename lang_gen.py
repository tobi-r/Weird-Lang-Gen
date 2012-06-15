'''
Created on 23.05.2012

@author: tobias
'''

import random
import bisect

abc = { chr(e) for e in range(ord('a'), ord('z') + 1) }
vovels = { 'a', 'e', 'i', 'o', 'u', 'y' }
consonants = { e for e in abc if e not in vovels }

sounding = vovels | {'y'}
notsounding = consonants

# Of 10000
frequency = {'a': 651, 'c': 306, 'b': 189, 'e': 1739, 'd': 508, 'g': 301, 'f': 166, 
             'i': 755, 'h': 476, 'k': 121, 'j': 27, 'm': 252, 'l': 344, 'o': 250, 
             'n': 977, 'q': 2, 'p': 79, 's': 600, 'r': 700, 'u': 434, 
             't': 615, 'w': 189, 'v': 67, 'y': 4, 'x': 3, 'z': 112}

freqVovels = { k: frequency[k] for k in frequency if k in vovels }
freqConsonant = { k: frequency[k] for k in frequency if k in consonants }

def genRandomLetter(freq):
    totals = {}
    tSum = 0
    
    for k in freq:
        tSum += freq[k]
        totals[k] = tSum
    
    rnd = random.random() * tSum
    for k in totals:
        if rnd < totals[k]:
            return k

def genSyllable():
    n_prevovels = int(round(abs(random.gauss(0.3, 0.5)) + .5))
    n_vovels = 1
    n_postvovels = int(round(abs(random.gauss(0.3, 0.5)) + .5))
    
    return (''.join(genRandomLetter(freqConsonant) for i in range(n_prevovels)) + 
            ''.join(genRandomLetter(freqVovels) for i in range(n_vovels)) + 
            ''.join(genRandomLetter(freqConsonant) for i in range(n_postvovels)))

def genWord(n_syllables):
    return ''.join(genSyllable() for i in range(n_syllables))

random.seed(100)

for i in range(50):
    print(' '.join(genWord(random.randint(1, 3)) for i in range(5)))

#print([ genRandomLetter(frequency) for i in range(12) ])