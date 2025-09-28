```python
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

# 初始化FastAPI应用
app = FastAPI()

# 模拟数据库会话
fake_db = []

# 用户模型
class User(BaseModel):
    id: int
    name: str
    email: str

# 依赖注入：获取数据库会话
def get_db():
    return fake_db

# 获取所有用户
@app.get("/users/", response_model=List[User], tags=["users"])
def test_get_users(db: Session = Depends(get_db)):
    """
    Test for retrieving all users.
    """
    return db

# 创建新用户
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED, tags=["users"])
def test_create_user(user: User, db: Session = Depends(get_db)):
    """
    Test for creating a new user.
    """
    db.append(user)
    return user

# 获取单个用户
@app.get("/users/{user_id}", response_model=User, tags=["users"])
def test_get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Test for retrieving a single user by ID.
    """
    user = next((u for u in db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# 更新单个用户
@app.put("/users/{user_id}", response_model=User, tags=["users"])
def test_update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    """
    Test for updating a single user by ID.
    """
    for i, u in enumerate(db):
        if u.id == user_id:
            db[i] = user
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# 删除单个用户
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def test_delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Test for deleting a single user by ID.
    """
    for i, u in enumerate(db):
        if u.id == user_id:
            del db[i]
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

# 添加文档字符串
app/docs
```

请注意，上述代码中的数据库会话`fake_db`是一个模拟的数据库，实际应用中应使用SQLAlchemy或其他数据库ORM工具。此外，`app/docs`命令用于启动FastAPI的Swagger UI，方便查看和测试API。