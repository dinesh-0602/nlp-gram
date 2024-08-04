import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter, defaultdict
import random

# Ensure nltk resources are available
nltk.download('punkt')

# Sample text corpus
corpus = """The quick brown fox jumps over the lazy dog. The dog barks back at the fox.
            The fox runs away into the forest. A quick red fox appears."""

# Tokenize the text
tokens = word_tokenize(corpus.lower())

# 1. Unigrams
unigrams = list(tokens)
unigram_counts = Counter(unigrams)

# 2. Bigrams
bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)

# 3. Trigrams
trigrams = list(ngrams(tokens, 3))
trigram_counts = Counter(trigrams)

# 4. Bigram Probabilities
bigram_probabilities = defaultdict(lambda: defaultdict(float))

for (w1, w2), count in bigram_counts.items():
    bigram_probabilities[w1][w2] = count / unigram_counts[w1]

# 5. Next Word Prediction
def predict_next_word(word):
    possible_words = bigram_probabilities[word]
    if not possible_words:
        return None
    next_word = max(possible_words, key=possible_words.get)
    return next_word

# Display outputs

# Unigrams
print("Unigrams and their frequencies:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

print("\nBigrams and their frequencies:")
for bigram, count in bigram_counts.items():
    print(f"{bigram}: {count}")

print("\nTrigrams and their frequencies:")
for trigram, count in trigram_counts.items():
    print(f"{trigram}: {count}")

print("\nBigram Probabilities:")
for w1, w2_probs in bigram_probabilities.items():
    for w2, prob in w2_probs.items():
        print(f"P({w2} | {w1}) = {prob:.2f}")

# Next word prediction examples
test_words = ['the', 'quick', 'fox']
print("\nNext Word Predictions:")
for word in test_words:
    next_word = predict_next_word(word)
    print(f"Next word after '{word}': {next_word}")
