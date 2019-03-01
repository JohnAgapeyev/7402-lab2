#!/bin/python

def f(i, k, x):
    return ((2 * i * k)**x) % 15


L = 0b0010
R = 0b1000

print("Encryption plaintext {} {}".format(bin(L), bin(R)))

#Round 1 encrypt
X = f(1, 7, R)

print("Post round 1 f() output {}".format(bin(X)));

#Xor output
X = L ^ X

print("Post round 1 xor {} {}".format(bin(L), bin(R)));

#Swap
L = R
R = X

print("Post round 1 swap {} {}".format(bin(L), bin(R)));

#Round 2 encrypt
X = f(2, 7, R)

print("Post round 2 f() output {}".format(bin(X)));

#Xor output
L ^= X

print("Post round 2 xor {} {}".format(bin(L), bin(R)));

#No swap on last round

print("Encrypt Output {} {}".format(bin(L), bin(R)))

print("Decryption")

#Round 1 Decrypt
X = f(2, 7, R)

print("Post decrypt round 1 f() output {}".format(bin(X)));

#Xor output
X = L ^ X

print("Post decrypt round 1 xor {} {}".format(bin(L), bin(R)));

#Swap
L = R
R = X

print("Post decrypt round 1 swap {} {}".format(bin(L), bin(R)));

#Round 2 decrypt
X = f(1, 7, R)

print("Post decrypt round 2 f() output {}".format(bin(X)));

#Xor output
L ^= X

print("Decrypt output {} {}".format(bin(L), bin(R)))
