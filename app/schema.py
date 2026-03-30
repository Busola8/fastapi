from pydantic import BaseModel, EmailStr, constr, StringConstraints
from datetime import datetime
from typing import Optional, Literal, Annotated

from pydantic.types import conint

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #default is true 



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True #default is true 

class PostCreate(PostBase):
    pass
#response 
class Post(BaseModel):
    title: str
    content: str
    published: bool
    id:int
    created_at: datetime 

    class Config:
        from_attributes = True


#or we cando 
# class Post(PostBase):
#     id:int
#     created_at: datetime 

    # class Config:
    #     orm_mode = True
# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True #default is true 

# class UpdatePost(BaseModel):
#     title: str # WE CAN REMOVE THIS TO MAKE SURE THEY CANT EDIT THESE
#     content: str # WE CAN REMOVE THIS TO MAKE SURE THEY CANT EDIT THESE
#     published: bool #INCASE THIS IS COMPULSORY

class UserCreate(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=72)]

#resonse user
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True



class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None



class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]