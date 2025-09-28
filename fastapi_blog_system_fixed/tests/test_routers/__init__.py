 ```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from tests.test_routers.models import Item, ItemCreate, ItemUpdate
from tests.test_routers.database import get_db, SessionLocal, engine
from tests.test_routers.crud import item_crud

router = APIRouter()

@router.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    Args:
    item (ItemCreate): The item to create.
    db (Session): The database session.

    Returns:
    Item: The created item.
    """
    db_item = item_crud.get_item_by_name(db, name=item.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists")
    return item_crud.create_item(db=db, item=item)

@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of items.

    Args:
    skip (int): The number of items to skip.
    limit (int): The maximum number of items to return.
    db (Session): The database session.

    Returns:
    list[Item]: A list of items.
    """
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get a single item by ID.

    Args:
    item_id (int): The ID of the item.
    db (Session): The database session.

    Returns:
    Item: The item.
    """
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an existing item.

    Args:
    item_id (int): The ID of the item.
    item (ItemUpdate): The updated item.
    db (Session): The database session.

    Returns:
    Item: The updated item.
    """
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_crud.update_item(db=db, db_item=db_item, item=item)

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an existing item.

    Args:
    item_id (int): The ID of the item.
    db (Session): The database session.
    """
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item_crud.delete_item(db=db, db_item=db_item)
    return

# Initialize the database
item_crud.get_db = get_db
item_crud.init_db(engine)
```