from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    # DIAGNOSTIC: Returns the files found in the current directory
    return {"files_found": os.listdir(".")}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
