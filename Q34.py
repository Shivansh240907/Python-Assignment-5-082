target_word = input("Enter the word to count: ").lower()
with open("India.txt", "r") as f:
    text = f.read().lower()
    for ch in ".,!?;:\"'()":
        text = text.replace(ch, "")
        
    words = text.split()
    count = words.count(target_word)

print(f"The word '{target_word}' occurs {count} times.")