from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from GitLab → HuggingFace CI/CD!\n This is just a sample project to understand the deployement of app from Github to HuggingFace"}

#if __name__ == "__main__":
   # uvicorn.run("app:app", host="0.0.0.0", port=8000) - Not needed for deploying in huggingface
