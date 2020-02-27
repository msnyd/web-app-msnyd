from flask import Flask, jsonify, render_template


def create_app():

    app = Flask(__name__) 


    @app.route("/")
    def index():
        x = 2 + 2
        return f"Hello World! {x}"

    @app.route("/about")
    def about():
        return "About Me"

    @app.route("/books")
    def books():
        books = [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"}
        ]
        return render_template("books.html")
    @app.route("/books.json")
    def list_books():
        books = [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"}
        ]
        return jsonify(books)
        
    return app

