 ```python
from pydantic import BaseModel, Field, validator
from datetime import datetime

class ItemCreate(BaseModel):
    """
    数据验证和序列化模式 - 创建变体
    """
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(None, min_length=0, max_length=1000)
    price: float = Field(..., gt=0)
    tax: float = Field(None, ge=0)

    @validator('name')
    def name_must_be_unique(cls, v):
        if 'example' in v.lower():
            raise ValueError('Name cannot contain "example"')
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

class ItemUpdate(BaseModel):
    """
    数据验证和序列化模式 - 更新变体
    """
    name: str = Field(None, min_length=1, max_length=100)
    description: str = Field(None, min_length=0, max_length=1000)
    price: float = Field(None, gt=0)
    tax: float = Field(None, ge=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

class ItemResponse(BaseModel):
    """
    数据验证和序列化模式 - 响应变体
    """
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
                "created_at": "2023-04-01T12:00:00Z",
                "updated_at": "2023-04-01T12:00:00Z",
            }
        }
```

### 文件路径: `app/schemas/__init__.py`
### 文件描述:
该文件定义了用于数据验证和序列化的Pydantic模型。包括创建、更新和响应变体，并添加了字段验证器和示例数据。

### 主要类:
1. **ItemCreate**: 用于创建新项目的验证和序列化模式。
2. **ItemUpdate**: 用于更新现有项目的验证和序列化模式。
3. **ItemResponse**: 用于返回项目的响应验证和序列化模式。

### 特点:
- 使用Pydantic的`BaseModel`定义数据模型。
- 包含字段验证器，如`name_must_be_unique`。
- 配置了`Config`类，包括`orm_mode`和`schema_extra`。
- 添加了示例数据，便于测试和文档展示。

### 示例数据:
每个模型都包含一个`schema_extra`，展示了如何在自动生成的API文档中展示示例数据。