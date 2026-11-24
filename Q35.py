search_word = input("Enter the word to search: ").lower()

with open("India.txt", "r") as f:
    text = f.read().lower()
    for ch in ".,!?;:\"'()":
        text = text.replace(ch, "")
        
    words = text.split()

    if search_word in words:
        print(f"Yes, '{search_word}' exists in the file.")
    else:
        print(f"No, '{search_word}' does not exist in the file.")