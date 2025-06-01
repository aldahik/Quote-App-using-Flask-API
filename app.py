from flask import Flask, jsonify, request

app = Flask(__name__)

quotes = [
    {"id": 1, "author": "Einstein", "quote": "Imagination is more important than knowledge"},
    {"id": 2, "author": "Yoda", "quote": "Do, or do not. There is no try."},
    {"id": 3, "author": "Nietzsche", "quote": "He who has a why can bear almost any how."},

]

@app.route("/")
def home():
    return "Welcome to the Quote API!!"

@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

@app.route("/api/quote", methods=["GET"])
def get_quote_by_author():
    author = request.args.get("author")
    if not author:
        return jsonify({"error": "Missing author parameter"}), 400

    results = [q for q in quotes if q["author"].lower() == author.lower()]
    if not results:
        return jsonify({"error": "No quotes found for that author"}), 404

    return jsonify(results)

@app.route("/api/addquote", methods=["POST"])
def add_quote():
    data = request.get_json()

    if not data or "author" not in data or "text" not in data:
        return jsonify({"error": "Invalid data. Must include 'author' and 'text'."}), 400

    # Generate a new ID (find max ID + 1)
    # “Loop through every quote in quotes. Try to get the id (use 0 if missing). Find the highest one. Add 1. That’s the new ID.”
    new_id = max([q.get("id", 0) for q in quotes], default = 0) + 1

    new_quote = {
        "id": new_id,
        "author": data["author"],
        "text": data["text"]
    }

    quotes.append(new_quote)
    return jsonify({"message": "Quote added successfully!"}), 201

@app.route("/hello")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)