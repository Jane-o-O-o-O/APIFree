 ```python
from pydantic import BaseModel, Field, validator
from datetime import datetime

class PostBase(BaseModel):
    """
    Base schema for Post.
    """
    title: str
    content: str
    published: bool = Field(default=False)

    class Config:
        schema_extra = {
            "example": {
                "title": "Hello World",
                "content": "This is a test post.",
                "published": False
            }
        }

class PostCreate(PostBase):
    """
    Schema for creating a new Post.
    """
    pass

class PostUpdate(PostBase):
    """
    Schema for updating an existing Post.
    """
    pass

class Post(PostBase):
    """
    Full schema for a Post.
    """
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Hello World",
                "content": "This is a test post.",
                "published": False,
                "created_at": "2023-04-01T12:00:00Z",
                "updated_at": "2023-04-01T12:00:00Z"
            }
        }
```

### 解释
1. **PostBase**: 基础模式，包含所有Post的字段，包括`title`、`content`和`published`。`published`默认为`False`。
2. **PostCreate**: 用于创建新Post的模式，继承自`PostBase`。
3. **PostUpdate**: 用于更新现有Post的模式，继承自`PostBase`。
4. **Post**: 完整的Post模式，包含`id`、`created_at`和`updated_at`字段。使用`orm_mode`来支持ORM操作。
5. **Config**: 配置类，包含`schema_extra`用于提供示例数据。

每个类都包含详细的文档字符串和配置，以确保代码的可读性和可维护性。