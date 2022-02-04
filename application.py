import uvicorn
from fastapi import FastAPI, Request, Response

application = FastAPI(debug=True)

@app.post("/api/v1/echo/")
async def echo(request: Request):
    body = await request.body()
    return Response(body)

uvicorn.run("application:application")
