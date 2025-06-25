from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("upload-book/")
async def upload_book(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}

