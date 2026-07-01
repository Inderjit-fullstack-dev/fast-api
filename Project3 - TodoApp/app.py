from datetime import datetime
from typing import List, Optional

# IMPORT FROM OUR NEW STRUCTURE
from database import Todo, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session


# ---------- PYDANTIC SCHEMAS ----------
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ---------- CREATE FASTAPI APP ----------
app = FastAPI(
    title="Todo API",
    description="Simple Todo CRUD API with Models folder",
    version="1.0.0",
)


# ---------- CRUD OPERATIONS ----------


# 1. CREATE - Add a new todo
@app.post("/todos/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo item"""
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# 2. READ ALL - Get all todos
@app.get("/todos/", response_model=List[TodoResponse])
def get_all_todos(
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    """Get all todos with optional filters"""
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    todos = query.offset(skip).limit(limit).all()
    return todos


# 3. READ ONE - Get a specific todo
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo by ID"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    return todo


# 4. UPDATE - Update a todo
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    """Update a todo item"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    if todo_update.title is not None:
        todo.title = todo_update.title

    if todo_update.description is not None:
        todo.description = todo_update.description

    if todo_update.completed is not None:
        todo.completed = todo_update.completed

    todo.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(todo)

    return todo


# 5. DELETE - Delete a todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by ID"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    db.delete(todo)
    db.commit()


# 6. TOGGLE - Mark todo as complete/incomplete
@app.patch("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    """Toggle the completion status of a todo"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    todo.completed = not todo.completed
    todo.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(todo)

    return todo
