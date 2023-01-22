import os
from typing import Union
from pathlib import Path
import subprocess
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt

def load_text(input_file):
    """Load text from a text file and return as a string"""
    with open(input_file,"r") as file:
        text = file.read()
    return text


def clean_text(text):
    """Lowercase and remove punctuation from a string"""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    """Count unique words in a string"""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)



def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig