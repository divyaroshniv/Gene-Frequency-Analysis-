#Example Genotype counts
AA = 120
Aa = 200
aa = 80

N = AA + Aa + aa

p = (2*AA + Aa)/(2*N)
q = (2*aa + Aa)/(2*N)

print("Allele Frequency p(A):", p)
print("Allele Frequency q(A):", q)

print("\nExpected Genotype Frequencies:")
print("AA =", p**2)
print("Aa =", 2*p*q)
print("aa=", q**2)