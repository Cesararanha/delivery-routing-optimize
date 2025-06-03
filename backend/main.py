from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # domínio do React/Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API está funcionando"}
