from flask import Flask, render_template, request
from search_system import VectorSearchEngine

app = Flask(__name__)

def get_query(form) -> str:
    return form.get("query", "").strip()


def get_mode(form) -> str:
    return "lemmas" if form.get("mode") == "lemmas" else "tokens"


def perform_search(query: str, mode: str):
    if not query:
        return []

    search_engine = VectorSearchEngine(index_dir="tf-idf", mode=mode)
    return search_engine.search(query)


@app.get("/")
def index():
    return render_template("search.html", query="", results=[], mode="tokens")


@app.post("/")
def search():
    query = get_query(request.form)
    mode = get_mode(request.form)
    results = perform_search(query, mode)

    return render_template("search.html", query=query, results=results, mode=mode)


if __name__ == "__main__":
    app.run(debug=True)