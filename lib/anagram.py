class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        original_sorted = sorted(self.word.lower())

        for w in word_list:
            if sorted(w.lower()) == original_sorted and w.lower() != self.word.lower():
                matches.append(w)

        return matches

