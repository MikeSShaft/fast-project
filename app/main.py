from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/brands/", response_model=list[schemas.Brand])
def read_brands(db: Session = Depends(get_db)):
    brands = crud.get_brands(db)
    return brands

@app.post("/brands/", response_model=schemas.Brand)
def create_brands(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db, brand)

@app.get("/brands/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@app.put("/brands/{brand_id}", response_model=schemas.Brand)
def update_brand_endpoint(brand_id: int, brand: schemas.BrandUpdate, db: Session = Depends(get_db)):
    db_brand = crud.update_brand(db, brand_id, brand)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@app.delete("/brands/{brand_id}")
def delete_brand_endpoint(brand_id: int, db: Session = Depends(get_db)):
    success = crud.delete_brand(db, brand_id)
    if not success:
        raise HTTPException(status_code=404, detail="Brand not found")
    return {"message": "Brand deleted successfully"}