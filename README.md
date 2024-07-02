# Book Management REST API

This is a simple REST API built using Flask for managing a list of books. The API allows you to add new books, update existing books, and delete books from the list.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/surajks10/RESTapi.git
    cd RESTapi
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the API

1. Start the Flask development server:

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## Endpoints

### Get all books

- **URL:** `/books`
- **Method:** `GET`
- **Description:** Retrieves a list of all books.
- **Response:**
    ```json
    [
        {
            "id": 1,
            "title": "Book Title",
            "author": "Author Name",
        },
        ...
    ]
    ```

### Get a single book

- **URL:** `/books/<id>`
- **Method:** `GET`
- **Description:** Retrieves a specific book by its ID.
- **Response:**
    ```json
    {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name"
    }
    ```

### Add a new book

- **URL:** `/books`
- **Method:** `POST`
- **Description:** Adds a new book to the list.
- **Request:**
    ```json
    {
        "title": "New Book Title",
        "author": "New Author Name"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Book added successfully",
        "book": {
            "id": 2,
            "title": "New Book Title",
            "author": "New Author Name"
        }
    }
    ```

### Update a book

- **URL:** `/books/<id>`
- **Method:** `PUT`
- **Description:** Updates an existing book by its ID.
- **Request:**
    ```json
    {
        "title": "Updated Book Title",
        "author": "Updated Author Name"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Book updated successfully",
        "book": {
            "id": 1,
            "title": "Updated Book Title",
            "author": "Updated Author Name"
        }
    }
    ```

### Delete a book

- **URL:** `/books/<id>`
- **Method:** `DELETE`
- **Description:** Deletes a book by its ID.
- **Response:**
    ```json
    {
        "message": "Book deleted successfully"
    }
    ```

## How It Works

The API is built using Flask, a lightweight web framework for Python. It provides a set of RESTful endpoints for managing a list of books. The data is stored in memory, so it will be lost when the server is restarted.

Each book has the following fields:
- `id` (integer): A unique identifier for the book.
- `title` (string): The title of the book.
- `author` (string): The author of the book.

The main operations supported by the API are:
- **Retrieving all books**: A `GET` request to the `/books` endpoint returns a list of all books.
- **Retrieving a single book**: A `GET` request to the `/books/<id>` endpoint returns the details of a specific book.
- **Adding a new book**: A `POST` request to the `/books` endpoint adds a new book to the list.
- **Updating a book**: A `PUT` request to the `/books/<id>` endpoint updates the details of an existing book.
- **Deleting a book**: A `DELETE` request to the `/books/<id>` endpoint deletes a book from the list.

## License

This project is licensed under the MIT License.
