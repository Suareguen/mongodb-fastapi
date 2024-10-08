from fastapi import APIRouter, HTTPException
from app.schemas.item_schema import ItemSchema
from app.services.item_service import create_item, get_all_items, get_item, update_item, delete_item

router = APIRouter()

@router.post("/items/", response_model=dict)
async def create_new_item(item: ItemSchema):
    item = await create_item(item.dict())
    return item

@router.get("/items/", response_model=list)
async def read_items():
    items = await get_all_items()
    return items

@router.get("/items/{item_id}", response_model=dict)
async def read_item(item_id: str):
    item = await get_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=dict)
async def update_existing_item(item_id: str, item: ItemSchema):
    updated_item = await update_item(item_id, item.dict())
    if updated_item:
        return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", response_model=dict)
async def delete_existing_item(item_id: str):
    deleted_item = await delete_item(item_id)
    if deleted_item:
        return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
