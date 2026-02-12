from Bio import SeqIO
import matplotlib.pyplot as plt

record = SeqIO.read("HBB.fasta", "fasta")
sequence = record.seq

print(f"Analysing: {record.description}")
print(f"length: {len(sequence)}bp")

window_size = 100
step_size = 20

positions = []
gc_values = []

for i in range(0, len(sequence) - window_size, step_size):
    subsequence = sequence[i:i + window_size]
    g_count = subsequence.count("G")
    c_count = subsequence.count("C")
    gc_percentage = (g_count + c_count) / len(subsequence) * 100

    positions.append(i)
    gc_values.append(gc_percentage)

    plt.figure(figsize=(12,6))
    plt.plot(positions, gc_values, linewidth=1)
    plt.title(f"GC Content Distribution of HBB Gene ({record.id})")
    plt.xlabel("Gene Position (bp)")
    plt.ylabel("GC Content (%)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()