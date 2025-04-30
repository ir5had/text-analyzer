def count_words(text):
    """Count total words in the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        int: The total number of words.
    """
    if not text.strip():
        return 0
    words = text.lower().split()
    return len(words)


def get_frequent_words(text, top_n=3):
    """Get the top N most frequent words and their counts.

    Args:
        text (str): The input text to analyze.
        top_n (int): Number of top frequent words to return (default: 3).

    Returns:
        list: List of tuples (word, count) sorted by count (descending) and word (alphabetically).
    """
    if not text.strip():
        return []

    # Split into words and count frequencies
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort by count (descending) and word (alphabetically)
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:top_n]