from collections import Counter, defaultdict
from time import perf_counter
from typing import List, Dict, Set
import random

def generate_test_data(size: int = 1000000) -> List[str]:
    """Generate test data - a list of random words."""
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    return random.choices(words, k=size)

# Challenge 1: Count word frequencies
def slow_count_frequencies(words: List[str]) -> Dict[str, int]:
    """Count frequencies the slow way."""
    frequencies = {}
    for word in words:
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1
    return frequencies

def fast_count_frequencies(words: List[str]) -> Dict[str, int]:
    """Count frequencies the fast way."""
    return Counter(words)

# Challenge 2: Find unique pairs of words that appear together
def slow_find_pairs(words: List[str]) -> Set[tuple]:
    """Find unique pairs the slow way."""
    pairs = set()
    for i in range(len(words)-1):
        pair = (min(words[i], words[i+1]), max(words[i], words[i+1]))
        pairs.add(pair)
    return pairs

def fast_find_pairs(words: List[str]) -> Set[tuple]:
    """Find unique pairs the fast way."""
    return {(min(a,b), max(a,b)) for a, b in zip(words, words[1:])}

# Challenge 3: Group words by their first letter
def slow_group_by_first_letter(words: List[str]) -> Dict[str, List[str]]:
    """Group words by first letter the slow way."""
    groups = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

def fast_group_by_first_letter(words: List[str]) -> Dict[str, List[str]]:
    """Group words by first letter the fast way."""
    groups = defaultdict(list)
    [groups[word[0]].append(word) for word in words]
    return dict(groups)

def benchmark_function(func, data, name: str):
    """Benchmark a function's execution time."""
    start = perf_counter()
    result = func(data)
    end = perf_counter()
    print(f"{name} took {end - start:.4f} seconds")
    return result

def main():
    # Generate test data
    print("Generating test data...")
    data = generate_test_data()

    # Challenge 1: Word frequencies
    print("\nChallenge 1: Count word frequencies")
    slow_result = benchmark_function(slow_count_frequencies, data, "Slow count")
    fast_result = benchmark_function(fast_count_frequencies, data, "Fast count")
    assert slow_result == fast_result, "Results don't match!"

    # Challenge 2: Find pairs
    print("\nChallenge 2: Find unique pairs")
    slow_result = benchmark_function(slow_find_pairs, data, "Slow pairs")
    fast_result = benchmark_function(fast_find_pairs, data, "Fast pairs")
    assert slow_result == fast_result, "Results don't match!"

    # Challenge 3: Group by first letter
    print("\nChallenge 3: Group by first letter")
    slow_result = benchmark_function(slow_group_by_first_letter, data, "Slow grouping")
    fast_result = benchmark_function(fast_group_by_first_letter, data, "Fast grouping")
    assert slow_result == fast_result, "Results don't match!"

if __name__ == "__main__":
    main()
