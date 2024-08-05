# Text Corpus Analysis with N-grams

## Overview

This project provides a Python script to analyze a given text corpus by generating and analyzing n-grams. It performs the following tasks:

1. **Unigrams**: Frequency counts of individual words.
2. **Bigrams**: Frequency counts of consecutive word pairs.
3. **Trigrams**: Frequency counts of consecutive word triplets.
4. **Bigram Probabilities**: Conditional probabilities of one word following another.
5. **Next Word Prediction**: Predicts the next word given a previous word using bigram probabilities.

Additionally, the script saves the results to a file and generates visualizations of the most frequent unigrams, bigrams, and trigrams.

## Table of Contents

- [Installation](#installation)
- [Prerequisites](#prerequisites)

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or later: [Download Python](https://www.python.org/downloads/)
- Pip (Python package manager): [Install Pip](https://pip.pypa.io/en/stable/installation/)

To verify the installation of Python and Pip, use the following commands:

```bash
python --version
pip --version
pip install nltk
