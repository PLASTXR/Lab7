from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from app.models.user import User

class TodoCategory(SQLModel, table=True):
    category_id: int = Field(foreign_key="category.id", primary_key=True)
    todo_id: int = Field(foreign_key="todo.id", primary_key=True)

class Category(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: int = Field(foreign_key="user.id")
    text:str

    todos:list['Todo'] = Relationship(back_populates="categories", link_model=TodoCategory)

class TodoCreate(SQLModel):
    text:str

class TodoResponse(SQLModel):
    id: Optional[int] = Field(primary_key=True, default=None)
    text:str
    done: bool = False

class TodoUpdate(SQLModel):
    text: Optional[str] = None
    done: Optional[bool] = None

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: int = Field(foreign_key="user.id")
    text:str
    done: bool = False

    user: User = Relationship(back_populates="todos")
    categories:list['Category'] = Relationship(back_populates="todos", link_model=TodoCategory)

    def toggle(self):
        self.done = not self.done
    
    def get_cat_list(self):
        return ', '.join([category.text for category in self.categories])
