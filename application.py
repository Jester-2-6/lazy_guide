import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/')
async def root():
  return 'Home page'

@app.post("/api/v1/echo/")
async def echo(request: Request):
    body = await request.body()
    return Response(body)

if __name__ == "__main__":
  uvicorn.run("application:app")
