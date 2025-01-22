import pygame
import sys

class TrieNode:
    def __init__(self, letter=None):
        self.children = {}
        self.letter = letter
    
    def __contains__(self, letter):
        return letter in self.children
    
    def __getitem__(self, letter):
        return self.children[letter]
    
    def __setitem__(self, letter, node):
        self.children[letter] = node
        return self
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = TrieNode(letter)
                self.size += 1
            node = node[letter]
        node['$'] = TrieNode('$')
        self.size += 1
        return self

    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter].children

        return '$' in node
    
    def getMatchingWords(self, prefix):
        if not prefix:
            return []
        node = self.root
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter].children

        return self._getMatchingWords(node, prefix)
    
    def _getMatchingWords(self, node, prefix):
        words = []
        for letter, child in node.items():
            if letter == '$':
                words.append(prefix)
            else:
                words.extend(self._getMatchingWords(child.children, prefix + letter))
        return words
    
    def getMatchingWordsWithLimit(self, prefix, limit):
        if not prefix:
            return []
        node = self.root
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter].children

        return self._getMatchingWordsWithLimit(node, prefix, limit)
    
    def _getMatchingWordsWithLimit(self, node, prefix, limit):
        words = []
        for letter, child in node.items():
            if len(words) >= limit:
                break
            if letter == '$':
                words.append(prefix)
            else:
                words.extend(self._getMatchingWordsWithLimit(child.children, prefix + letter, limit - len(words)))
        return words
    

tree = Trie()

tree.insert('hello')
tree.insert('helloman')
tree.insert('world')
tree.insert('hey')

print(tree.search('hello')) # True
print(tree.search('world')) # True
print(tree.search('hell')) # False

print(tree.getMatchingWords('he')) # ['hello']
print(tree.getMatchingWordsWithLimit('he', 1)) # ['hello']

print(tree.getMatchingWords(''))

print(tree.size) # 14

current = ''
while True:
    pygame.init()

    # Set up the display
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Trie Input')

    font = pygame.font.Font(None, 36)
    current = ''

    def draw_text(text, position, opacity=255):
        text_surface = font.render(text, True, (255, 255, 255, opacity))
        text_surface.set_alpha(opacity)
        window.blit(text_surface, position)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current = ''
                elif event.key == pygame.K_BACKSPACE:
                    current = current[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    current += event.unicode

        window.fill((0, 0, 0))
        cw_text = f"Current word: {current}"
        draw_text(cw_text, (20, 20))
        draw_text(f"Search result: {tree.search(current)}", (20, 60))
        draw_text(f"Matching words: {tree.getMatchingWords(current)}", (20, 100))
        draw_text(f"Matching words with limit: {tree.getMatchingWordsWithLimit(current, 5)}", (20, 140))
        
        if current:
            matching_words = tree.getMatchingWords(current)
            if matching_words:
                first_match = matching_words[0]
                if len(first_match) > len(current):
                    rest_of_word = first_match[len(current):]
                    # draw_text(" " * len(cw_text) + rest_of_word, (20, 20), opacity=100)
                    draw_text(rest_of_word, (20 + font.size(cw_text)[0], 20), opacity=100)
        
        pygame.display.flip()
