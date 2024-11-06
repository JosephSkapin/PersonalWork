import math

print("This is a demonstration of the RSA encryption algorithm\n")
#Private Keys
p = 127 #Large Prime P
q = 131 #Large Prime Q

#Public keys are (N,e)
N = p*q
e =11 #Encryption Exponent

d = 0 #Decryption Exponent (unknown for now)
phi = (p-1)*(q-1) #phi(n) is euler's totient function of n, which is (p-1)(q-1) for primes p,q
c = 0 #Cipher Text
m = 99 #Message



def relatively_prime(a,b):
    return math.gcd(a,b) == 1


print(f"N = {N}\n"
      f"p = {p}\n"
      f"q = {q}\n"
      f"e = {e}\n"
      f"phi = {phi}"

)
if relatively_prime(e,phi):
    print(f"{e} and {phi} are relatively prime")
else:
    print(f"{e} and {phi} are not relatively prime")


#To find d we use de = 1(mod(phi(n)) or in other-words de = 1 mod (p-1)(q-1)
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("No modular inverse exists for the given e and phi. i.e phi and e are not relatively prime")
    else:
        return x % phi

#Encryption Formula
c = (m**e) % N  #Written as C = (M^e) mod N
print(f"Cipher Text = {c}")


#Find d
d = modular_inverse(e,phi)
print(f"d = {d}")


#Decryption Formula

message = (c**d) % N
print(f"message = {message}")







