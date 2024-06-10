from fastapi import FastAPI
from items.routes_item import router
from database import Base, engine
from banners.routes_alt import router as Banners
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(Banners)


# FastAPI generează automat documentația API. Poți accesa documentația
# interactivă generată de Swagger UI la http://127.0.0.1:8000/docs
# și documentația generată de ReDoc la http://127.0.0.1:8000/redoc.