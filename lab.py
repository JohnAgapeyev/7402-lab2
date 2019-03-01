#!/bin/python

def f(i, k, x):
    return ((2 * i * k)**x) % 15


L = 0b0010
R = 0b1000

print("Encryption plaintext {} {}".format(bin(L), bin(R)))

#Round 1 encrypt
X = f(1, 7, R)

#Xor output
X = L ^ X

#Swap
L = R
R = X

#Round 2 encrypt
X = f(2, 7, R)

#Xor output
L ^= X

#No swap on last round

print("Encrypt Output {} {}".format(bin(L), bin(R)))

print("Decryption")

#Round 1 Decrypt
X = f(2, 7, R)

#Xor output
X = L ^ X

#Swap
L = R
R = X

#Round 2 decrypt
X = f(1, 7, R)

#Xor output
L ^= X

print("Decrypt output {} {}".format(bin(L), bin(R)))
