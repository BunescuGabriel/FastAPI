
from fastapi import APIRouter, Depends, File, Form, UploadFile,HTTPException
from sqlalchemy.orm import Session
import os
import database
from . import models
from typing import List
from .schemas import BannerSchema

router = APIRouter(
    prefix="/banner",
    tags=["Banners"],
)


UPLOAD_DIRECTORY = "static/banners/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# @router.post("/add")
@router.post("/upload/")
async def upload_banner(name: str = Form(...), image: UploadFile = File(...), db: Session = Depends(database.get_db)):
    image_location = os.path.join(UPLOAD_DIRECTORY, image.filename)

    with open(image_location, "wb") as f:
        f.write(image.file.read())

    image_url = f"/static/banners/{image.filename}"
    banner = models.Banner(name=name, image_url=image_url)
    db.add(banner)
    db.commit()
    db.refresh(banner)

    return banner


@router.get("/", response_model=List[BannerSchema])
async def get_banners(db: Session = Depends(database.get_db)):
    banners = db.query(models.Banner).all()
    return banners

@router.get("/banner/{banner_id}", response_model=BannerSchema)
def read_banner(banner_id: int, db: Session = Depends(database.get_db)):
    banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if banner is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return banner

@router.delete("/banner_del/{banner_id}", response_model=BannerSchema)
def delete_banner(banner_id: int, db: Session = Depends(database.get_db)):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if db_banner is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_banner)
    db.commit()
    return db_banner


@router.put("/banner/{banner_id}", response_model=BannerSchema)
def update_banner(banner_id: int, name: str = Form(None), image: UploadFile = File(None),
                  db: Session = Depends(database.get_db)):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if db_banner is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update banner name if provided
    if name:
        db_banner.name = name

    # Upload new image if provided
    if image:
        image_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
        with open(image_location, "wb") as f:
            f.write(image.file.read())
        image_url = f"/static/banners/{image.filename}"
        db_banner.image_url = image_url

    db.commit()
    db.refresh(db_banner)
    return db_banner


@router.patch("/banner/{banner_id}", response_model=BannerSchema)
def patch_banner(banner_id: int, name: str = Form(None), image: UploadFile = File(None), db: Session = Depends(database.get_db)):
    db_banner = db.query(models.Banner).filter(models.Banner.id == banner_id).first()
    if db_banner is None:
        raise HTTPException(status_code=404, detail="Item not found")

    if name:
        db_banner.name = name
    if image:
        image_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
        with open(image_location, "wb") as f:
            f.write(image.file.read())
        image_url = f"/static/banners/{image.filename}"
        db_banner.image_url = image_url

    db.commit()
    db.refresh(db_banner)
    return db_banner