```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter()

# 示例路由：获取所有用户
@router.get("/users/", response_model=list[schemas.User], status_code=status.HTTP_200_OK)
def read_users(db: Session = Depends(get_db)):
    """
    获取所有用户
    """
    users = crud.user.get_multi(db)
    return users

# 示例路由：创建新用户
@router.post("/users/", response_model=schemas.UserCreate, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    创建新用户
    """
    db_user = crud.user.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create(db=db, obj_in=user)

# 示例路由：获取单个用户
@router.get("/users/{user_id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    获取单个用户
    """
    db_user = crud.user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# 示例路由：更新用户信息
@router.put("/users/{user_id}", response_model=schemas.User, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """
    更新用户信息
    """
    db_user = crud.user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.user.update(db=db, db_obj=db_user, obj_in=user)

# 示例路由：删除用户
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    删除用户
    """
    db_user = crud.user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.user.remove(db, id=user_id)
    return {"detail": "User deleted"}
```

这个示例展示了如何使用FastAPI框架创建一个简单的RESTful API，包含用户管理的四个基本操作：获取所有用户、创建新用户、获取单个用户、更新用户信息和删除用户。每个路由都有适当的依赖注入（获取数据库会话）、请求/响应模型、错误处理和状态码，以及详细的文档字符串。