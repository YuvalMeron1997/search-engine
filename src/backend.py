import math
from collections import defaultdict
from src.inverted_index import InvertedIndex

class SearchBackend:
    def __init__(self, docs):
        self.index = InvertedIndex(docs)

    def search(self, query):
        tokens = query.lower().split()
        scores = defaultdict(float)

        for term in tokens:
            if term not in self.index.index:
                continue

            idf = self.index.idf(term)
            postings = self.index.index[term]

            for doc_id, tf in postings:
                scores[doc_id] += (tf / self.index.doc_len[doc_id]) * idf

        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return results[:5]
