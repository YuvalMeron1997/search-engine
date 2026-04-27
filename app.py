from flask import Flask, request, jsonify
import json
from src.backend import SearchBackend

with open("data/sample_docs.json") as f:
    docs = json.load(f)

backend = SearchBackend(docs)

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify([])

    results = backend.search(query)
    output = [(doc_id, docs[doc_id]) for doc_id, _ in results]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
