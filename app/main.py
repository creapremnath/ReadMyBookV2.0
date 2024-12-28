from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/home")
async def home():
    return {"message": "Welcome to my FastAPI application"}

@app.get("/about")
async def about():
    return {"message": "This is an API for a simple website"}

@app.get("/contact")
async def contact():
    return {"message": "For any inquiries, please contact me at email@example.com"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)