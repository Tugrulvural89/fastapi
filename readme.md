# FastAPI Blog API

A lightweight, efficient blog API built with FastAPI, SQLAlchemy, and Alembic, featuring middleware for logging and error handling.

## Project Structure
```
blog_api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── main.py
│   └── middleware.py
├── alembic/
├── alembic.ini
└── requirements.txt
```

## Features

- CRUD operations for blog posts
- SQLAlchemy ORM integration
- Request logging middleware
- Global exception handling
- Alembic database migrations
- Pydantic schemas for data validation

## API Endpoints

- `POST /blogs/`: Create a new blog post
- `GET /blogs/`: List all blog posts
- `GET /blogs/{blog_id}`: Get a specific blog post
- `PUT /blogs/{blog_id}`: Update a blog post
- `DELETE /blogs/{blog_id}`: Delete a blog post

## Database Model

The Blog model includes:
```python
class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
```

## Middleware

The API includes middleware for:
- Request logging
- Global exception handling

```python
@app.middleware("http")
async def log_request(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "Invalid Request"})
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blog_api.git
cd blog_api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database connection in `app/database.py`

5. Initialize the database:
```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Running the Application

Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation will be available at `http://localhost:8000/docs`

## Usage Examples

### Create a Blog Post
```python
POST /blogs/
{
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post."
}
```

### Get All Blog Posts
```python
GET /blogs/
```

### Update a Blog Post
```python
PUT /blogs/1
{
    "title": "Updated Title",
    "content": "Updated content"
}
```

## Error Handling

The API includes built-in error handling for:
- 404 Not Found for non-existent blog posts
- 500 Internal Server Error for unexpected exceptions
- Input validation errors

## Dependencies

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.


