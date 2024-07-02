from flask import Flask, jsonify, request,Request

app = Flask(__name__)

# Sample book list
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)# Add a new book

@app.route("/books/<int:book_id>",methods=["GET"])
def search(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error":"Book not found"}),404

# add new book to the list
@app.route('/books', methods=['POST'])
def add_book():
    title=request.json.get("title")
    author=request.json.get("author")
    book_id=books[-1]['id']+1

    new_book={"id":book_id,"title":title,"author":author}
    books.append(new_book)
    return "success",200

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json.get('title')
            book['author'] = request.json.get('author')
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message":"book removed successfully"}),200
    return jsonify({'error': 'Book not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
