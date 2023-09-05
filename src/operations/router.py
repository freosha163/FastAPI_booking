from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
# from operations.models import restaurant, table, booking
from auth.models import Role
from operations.schemas import (RoleGet,
                                RoleAdd,
                                )
from fastapi import HTTPException
from typing import List


router = APIRouter(
    tags=['Role function']
)


# Добавить роль для аутентификации и авторизации
@router.get('/role', response_model=List[RoleGet])
async def get_role(session: AsyncSession = Depends(get_async_session)):
    query = select(Role)
    result = await session.execute(query)
    return result.scalars().all()




@router.post('/role')
async def add_role(new_role: RoleAdd, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Role).values(**new_role.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'role added'}


# @router.get('/restaurant', response_model=List[RestaurantGet])
# async def get_restaurant(restaurant_id: int = None, session: AsyncSession = Depends(get_async_session)):
#     if restaurant_id:
#         query = select(restaurant).where(restaurant.c.id == restaurant_id)
#         result = await session.execute(query)
#         return result.all()
#     query = select(restaurant).order_by(restaurant.c.id)
#     result = await session.execute(query)
#     return result.all()


# @router.post('/restaurant')
# async def create_restaurant(new_restaurant: RestaurantCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(restaurant).values(**new_restaurant.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {'status': 'restaurant added'}


# @router.put('/restaurant/{restaurant_id}', response_model=List[RestaurantUpdate])
# async def update_restaurant(restaurant_id: int, payload: RestaurantUpdate, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(restaurant).where(restaurant.c.id == restaurant_id).values(payload.dict(exclude_unset=True)).returning(restaurant)
#     result = await session.execute(stmt)
#     await session.commit()
#     return result.all()


# @router.delete('/restaurant/{restaurant_id}')
# async def delete_restaurant(restaurant_id: int, session: AsyncSession = Depends(get_async_session)):
#     try:
#         delete_query = delete(restaurant).where(restaurant.c.id == restaurant_id)
#         await session.execute(delete_query)
#         await session.commit()
#         return {'status': 'success',
#                 'data': f'Restaurant with id {restaurant_id} has been deleted'
#                 }
#     except Exception:
#         raise HTTPException(status_code=404, detail=f'Restaurant with id {restaurant_id} doesn\'t exist')


# @router.get('/table', response_model=List[TableGet])
# async def get_table(restaurant_id: int = None, table_id: int = None, session: AsyncSession = Depends(get_async_session)):
#     if restaurant_id and table_id:
#         query = select(table).filter(table.c.restaurant_id == restaurant_id, table.c.id == table_id)
#         result = await session.execute(query)
#         return result.all()
#     if restaurant_id:
#         query = select(table).filter(table.c.restaurant_id == restaurant_id)
#         result = await session.execute(query)
#         return result.all()
#     query = select(table).order_by(table.c.restaurant_id)
#     result = await session.execute(query)
#     return result.all()


# @router.post('/table')
# async def create_table(new_table: TableCreate, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(table).values(**new_table.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {'status': 'table has been added'}


# @router.put('/table/{table_id}', response_model=List[TableUpdate])
# async def update_table(table_id: int, payload: TableUpdate, session: AsyncSession = Depends(get_async_session)):
#     stmt = update(table).where(table.c.id == table_id).values(payload.dict(exclude_unset=True)).returning(restaurant)
#     result = await session.execute(stmt)
#     await session.commit()
#     return result.all()


# @router.delete('/restaurant/{restaurant_id}/{table_id}')
# async def delete_table(restaurant_id: int, table_id: int, session: AsyncSession = Depends(get_async_session)):
#     try:
#         delete_query = delete(table).where(table.c.restaurant_id == restaurant_id, table.c.id == table_id)
#         await session.execute(delete_query)
#         await session.commit()
#         return {'status': 'success',
#                 'data' : f'Table with restaurant_id {restaurant_id} and table_id {table_id} has been deleted'
#                 }
#     except Exception:
#         raise HTTPException(
#             status_code=404,
#             detail=f'Table with restaurant_id {restaurant_id} and table_id {table_id} doesn\'t exist'
#         )
