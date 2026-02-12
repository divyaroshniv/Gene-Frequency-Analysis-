import matplotlib.pyplot as plt

file = open("HBB.fasta", "r")

sequence = ""
for line in file:
    if not line.startswith(">"):
        sequence += line.strip()

file.close()

A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

total = len(sequence)

print("Total Length:", total)
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

print("\nNucleotide Frequency:")
print("A:", A/total)
print("T:", T/total)
print("G:", G/total)
print("C:", C/total)

labels = ["A", "T", "G", "C"]
counts = [A, T, G, C]

plt.bar(labels, counts)
plt.xlabel("Nucleotides")
plt.ylabel("Count")
plt.title("Haemoglobin Gene (HBB) Nucleotide Frequency")
plt.show()
