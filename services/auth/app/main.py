from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routers import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # ajusta puertos según tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)