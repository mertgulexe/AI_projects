import flask
import sqlite3
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    """Returns items from the database as dictionaries rather than lists
    These work better when we output them to JSON."""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route("/", methods=["GET"])
def home():
    return """<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>"""


@app.route("/api/v1/resources/books/all", methods=["GET"])
def api_all():
    conn = sqlite3.connect("books.db")  # connection to the database
    conn.row_factory = dict_factory  # line lets the connection object know to
    # use the 'dict_factory' function we’ve defined.
    cur = conn.cursor()  # cursor obj. that moves through the db to pull data
    all_books = cur.execute("SELECT * FROM books;").fetchall()  # execute SQL query

    return jsonify(all_books)


@app.errorhandler(404)
def page_not_found(e):
    """Create an error page seen by the user if the user encounters an error 
    or inputs a route that hasn’t been defined."""
    return "<h1>404</h1><p>The resource couldn't be found.</p>", 404


@app.route("/api/v1/resources/books", methods=["GET"])
def api_filter():
    query_parameters = request.args  # grabs all the q_params provided in the URL

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()
