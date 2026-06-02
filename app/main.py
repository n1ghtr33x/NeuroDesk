from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth, users
from app.api.v1.endpoints import ai

app = FastAPI(
    title="NeuroDesk API",
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, prefix='/api/v1')
app.include_router(users.router, prefix='/api/v1')
app.include_router(ai.router, prefix='/api/v1')

@app.get('/api/v1//health')
async def health():
    return {'status': 'ok'}