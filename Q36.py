with open("India.txt", "r") as f:
    text = f.read()
    for ch in ".,!?;:\"'()":
        text = text.replace(ch, "")
        
    words = text.split()
    longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))