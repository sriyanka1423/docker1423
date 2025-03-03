import os
import re
import socket
from collections import Counter

# Define file paths
input_dir = "/home/data/"
output_dir = "/home/data/output/"
file1_path = os.path.join(input_dir, "IF-1.txt")
file2_path = os.path.join(input_dir, "AlwaysRememberUsThisWay-1.txt")
output_file_path = os.path.join(output_dir, "result.txt")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to count words in a text file with proper contraction handling
def count_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()

        # Step 1: Expand contractions correctly
        contractions = {
            "i'm": "i am", "i've": "i have", "i'll": "i will", "i'd": "i would",
            "you're": "you are", "you've": "you have", "you'll": "you will", "you'd": "you would",
            "he's": "he is", "he'll": "he will", "he'd": "he would",
            "she's": "she is", "she'll": "she will", "she'd": "she would",
            "it's": "it is", "it'll": "it will", "it'd": "it would",
            "we're": "we are", "we've": "we have", "we'll": "we will", "we'd": "we would",
            "they're": "they are", "they've": "they have", "they'll": "they will", "they'd": "they would",
            "that's": "that is", "who's": "who is", "what's": "what is", "where's": "where is",
            "when's": "when is", "why's": "why is", "how's": "how is",
            "let's": "let us", "d'you": "do you",
            "don't": "do not", "doesn't": "does not", "didn't": "did not",
            "can't": "cannot", "couldn't": "could not", "shouldn't": "should not",
            "won't": "will not", "wouldn't": "would not", "isn't": "is not", "ain't": "is not",
            "weren't": "were not", "hasn't": "has not", "haven't": "have not",
            "hadn't": "had not", "mightn't": "might not", "mustn't": "must not"
        }

        # Replace contractions in text
        for contraction, expanded in contractions.items():
            text = text.replace(contraction, expanded)

        # Step 2: Use a proper regex to extract words and prevent single letters from being counted
        words = re.findall(r"\b[a-zA-Z']+\b", text)

        return words, Counter(words)

# Count words in both files
words_file1, counter_file1 = count_words(file1_path)
words_file2, counter_file2 = count_words(file2_path)

# Compute word counts
total_words_file1 = len(words_file1)
total_words_file2 = len(words_file2)
grand_total_words = total_words_file1 + total_words_file2

# Get top 3 most common words
top_3_file1 = counter_file1.most_common(3)
top_3_file2 = counter_file2.most_common(3)

# Get container's IP address
container_ip = socket.gethostbyname(socket.gethostname())

# Prepare result text
result_text = f"""Total words in IF-1.txt: {total_words_file1}
Total words in AlwaysRememberUsThisWay-1.txt: {total_words_file2}
Grand total words: {grand_total_words}

Top 3 words in IF-1.txt: {top_3_file1}
Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_3_file2}

Container IP Address: {container_ip}
"""

# Write result to output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(result_text)

# Print result to console
print(result_text)