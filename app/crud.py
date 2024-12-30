from sqlalchemy.orm import Session
from . import models, schemas

def create_blog(db: Session, blog : schemas.BlogCreate):
    db_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def get_blogs(db:Session):
    return db.query(models.Blog).all()

def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        for key, value in blog.model_dump(exclude_unset=True).items():
            setattr(db_blog, key, value)
        db.commit()
        db.refresh(db_blog)
        return db_blog
    
def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog
