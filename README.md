# Quote API

A simple REST API based on Flask for storing, adding, editing, and deleting quotes.

## Features

- Get all quotes
- Get quotes by author or ID
- Add a new quote
- Edit a quote
- Delete a quote

## Routes

- 'GET /api/quotes' - Get all quotes
- 'GET /api/quote/id' - Get quote by id
- 'GET /api/quotes/author' - Get all quotes from an author
- 'POST /api/quote/' - Add a quote
- 'DELETE /api/quote/id' - Delete a quote
- 'PATCH /api/quote/id' - Edit a quote

## Notes

Quotes are currently being stored in memory and are deleted by server restart.

Will be linked to SQLite database in the future

## Running the Project

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
