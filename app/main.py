from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import models, schemas,  crud, middleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

middleware.add_middleware(app)

@app.post("/blogs/", response_model=schemas.BlogCreate)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)

@app.get("/blogs/", response_model=list[schemas.BlogResponse])
def read_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)

@app.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

@app.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def update_blog(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    db_blog = crud.update_blog(db, blog_id, blog)
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    return db_blog

@app.delete("/blogs/{blog_id}", response_model=schemas.BlogResponse)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.delete_blog(db, blog_id)
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    return db_blog

