from flask import Flask, jsonify

print("NAME:", __name__)
app = Flask(__name__)
print(app)
@app.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return "About Me"

@app.route("/books")
@app.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"}
    ]
    return jsonify(books)

app.run(port=5000)
