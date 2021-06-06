from fastapi import FastAPI
from starlette.routing import Host

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Helloworld, FastAPI"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)