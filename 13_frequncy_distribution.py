from collections import Counter
import re

def generate_word_frequency(text):
    text = text.lower()

    words = re.findall(r'\b\w+\b', text)

    word_frequency = Counter(words)

    return word_frequency

def main():
    with open("C:/Users/aspi/Documents/fods/13_sample.txt", "r") as file:
        text = file.read()

    word_frequency = generate_word_frequency(text)

    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
