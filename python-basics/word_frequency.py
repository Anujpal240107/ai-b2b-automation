# Read input file
with open("input.txt", "r") as f:
    text = f.read()

# Convert to lowercase and split into words
words = text.lower().split()

# Count word frequencies
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Write results to output.txt
with open("output.txt", "w") as f:
    for word, count in word_counts.items():
        f.write(f"{word}: {count}\n")

print("Done! Check output.txt")
