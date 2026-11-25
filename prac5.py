p=23
g=5
print("publicly shared value:")
print("prime(P):",p)
print("base(g):",g)

a=6
A=(g**a)%p

b=139
B=(g**b)%p

print("Alice public key(A):",A)
print("bob public key(B):",b)

secret_Alice=(B**a)%p 
secret_Bob=(A**6)%p

print("shared secret computed by alice:", secret_Alice)
print("shared secret computed by bob:", secret_Bob)

if secret_Alice==secret_Bob:
    print("key exchange succesful! Shared secret key=",secret_Alice)
else:
        print("key Exchnage Failed")
