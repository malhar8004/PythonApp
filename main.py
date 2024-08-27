from fastapi import FastAPI, Query, Request, Form, HTTPException, Depends
from pydantic import BaseModel
import random
import string
import hashlib
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "malhar"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    participant_name = "Malhar Dhaygude"
    welcome_message = f"Welcome to the FastAPI application, {participant_name}!"
    return HTMLResponse(content=f"<html><body><h1>{welcome_message}</h1></body></html>")



@app.post("/generate-token", response_class=HTMLResponse)
async def generate_token(request: Request, length: int = Form(...)):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return templates.TemplateResponse("form.html", {"request": request, "token": token})


"""
Generate a token with a specified length.

Parameters:
- length (int): Length of the token (default: 8)

Returns:
- dict: A dictionary containing the generated token

Example:
>>> api_generate_token(length=10)
{'token': 'aBcDeFgHiJ'}
"""

@app.get("/api/generate-token")
async def api_generate_token(length: int = Query(8, description="Length of the token")):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return {"token": token}

class TokenRequest(BaseModel):
    text: str

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key

@app.post("/api/generate-tokens")
async def api_generate_tokens(body: TokenRequest, api_key: str = Depends(get_api_key)):
    checksum = generate_checksum(body.text)
    return {"checksum": checksum}

def generate_checksum(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)