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

# Returns all quotes.
@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

# Route to get a quote from a specific author. GET method is used to fetch data from a server
@app.route("/api/quote", methods=["GET"])
def get_quote_by_author():
    author = request.args.get("author")
    if not author:
        return jsonify({"error": "Missing author parameter"}), 400

    results = [q for q in quotes if q["author"].lower() == author.lower()]
    if not results:
        return jsonify({"error": "No quotes found for that author"}), 404

    return jsonify(results)

# Find a quote by its ID
@app.route("/api/quote/<int:id>", methods=["GET"])
def get_quote_by_id(id):

    for quote in quotes:
        if quote["id"] == id:
            return jsonify(quote)

    return jsonify({"error": "Quote not found for ID"}), 404


# Route to add a new quote. POST method is used to send data to the server.
@app.route("/api/addquote", methods=["POST"])
def add_quote():
    data = request.get_json()

    if not data or "author" not in data or "quote" not in data:
        return jsonify({"error": "Invalid data. Must include 'author' and 'text'."}), 400

    # Generate a new ID (find max ID + 1)
    # “Loop through every quote in quotes. Try to get the id (use 0 if missing). Find the highest one and add 1.
    # default = 0 incase the list of quotes is empty.
    new_id = max([q.get("id", 0) for q in quotes], default = 0) + 1

    new_quote = {
        "id": new_id,
        "author": data["author"],
        "quote": data["quote"]
    }

    quotes.append(new_quote)
    return jsonify({"message": "Quote added successfully!"}), 201


@app.route("/api/quote/<int:quote_id>", methods=["PATCH"])
def edit_quote(quote_id):
    global quotes

    data = request.get_json()

    if not data or ("author" not in data and 'quote' not in data):
        return jsonify({"error": "Invalid data. Must include author or text."}), 400

    quote_to_edit = None

    for quote in quotes:
        if quote["id"] == quote_id:
            quote_to_edit = quote
            break

    if quote_to_edit is None:
        return jsonify({"error": "Quote not found"}), 404

    if "author" in data:
        quote_to_edit["author"] = data["author"]
    if "quote" in data:
        quote_to_edit["quote"] = data["quote"]

    return jsonify({"message": f"Quote ID: {quote_id} edited.", "quote" :quote_to_edit}), 200

@app.route("/api/quote/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    global quotes

    for quote in quotes:
        if quote["id"] == quote_id:
            quote_to_delete = quote
            break

    if quote_to_delete is None:
        return jsonify({"error": "Quote not found"}), 404

    quotes.remove(quote_to_delete)
    return jsonify({"message": f"Quote ID: {quote_id} deleted."}), 200


@app.route("/hello")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)