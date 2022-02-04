import uvicorn
from fastapi import FastAPI, Request, Response

app = FastAPI(debug=True)

@app.post("/api/v1/echo/")
async def echo(request: Request):
    body = await request.body()
    return Response(body)

uvicorn.run("application:app")
