class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)

        for c in list(freq.keys()):
                freq[c] -= 1

                if freq[c] == 0:
                   del freq[c]

                if len(set(freq.values())) == 1:
                    return True
                freq[c] += 1

        return False
    