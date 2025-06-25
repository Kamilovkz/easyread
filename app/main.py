from fastapi import FastAPI, UploadFile, File
import json

app = FastAPI()

with open("app/data/books.json", "r") as f:
    books = json.load(f)


@app.get("/books/")
def list_books():
    return [{"id": b["id"], "title": b["title"], "author": b["author"]} for b in books]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"} 

@app.post("upload-book/")
async def upload_book(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}

