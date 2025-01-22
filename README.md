# Trie Implementation with Pygame Interface

This project implements a **Trie data structure** in Python, which supports operations like inserting words, searching for words, and retrieving matching words based on prefixes. It also features a **real-time interface** built using **Pygame** to allow users to interact with the Trie.

---

## Features

### Trie Functionality
- **Insert Words**: Add words to the Trie.
- **Search Words**: Check if a word exists in the Trie.
- **Prefix Matching**: Retrieve all words in the Trie that match a given prefix.
- **Limited Prefix Matching**: Retrieve a limited number of words that match a given prefix.
- **Efficiency**: Words are stored efficiently using nodes and only necessary characters are added.

### Pygame Interface
- A simple graphical interface for interacting with the Trie.
- Displays:
  - The current input word.
  - Whether the word exists in the Trie.
  - All words that match the current prefix.
  - A preview of the first matching word beyond the current prefix.

---

## How to Use

### Trie Class
The `Trie` class is implemented to support common operations:
1. **Insert Words**: Add words to the Trie using `insert(word)`.
2. **Search Words**: Check if a word exists using `search(word)`.
3. **Prefix Matching**:
   - Get all matching words with `getMatchingWords(prefix)`.
   - Get limited matching words with `getMatchingWordsWithLimit(prefix, limit)`.

Example usage:
```python
tree = Trie()
tree.insert('hello')
tree.insert('helloman')
tree.insert('world')
print(tree.search('hello'))  # Output: True
print(tree.getMatchingWords('he'))  # Output: ['hello', 'helloman', 'hey']
