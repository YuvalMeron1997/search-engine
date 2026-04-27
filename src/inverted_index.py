import math
from collections import defaultdict, Counter

class InvertedIndex:
    def __init__(self, docs):
        self.docs = docs
        self.N = len(docs)
        self.index = defaultdict(list)
        self.df = Counter()
        self.doc_len = {}

        self.build_index()

    def build_index(self):
        for doc_id, text in self.docs.items():
            tokens = text.lower().split()
            self.doc_len[doc_id] = len(tokens)
            counts = Counter(tokens)

            for term, tf in counts.items():
                self.index[term].append((doc_id, tf))
                self.df[term] += 1

    def idf(self, term):
        return math.log((self.N + 1) / (self.df[term] + 1)) + 1
