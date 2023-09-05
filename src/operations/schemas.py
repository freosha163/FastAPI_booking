from pydantic import BaseModel


class RoleGet(BaseModel):
    id: int = None
    name: str = None

    class Config:
        orm_mode = True


class RoleAdd(BaseModel):
    name: str = None

    class Config:
        orm_mode = True


# class RestaurantGet(BaseModel):
#     id: int
#     name: str
#     description: str
#     address: str

#     class Config:
#         orm_mode = True


# class RestaurantCreate(BaseModel):
#     name: str
#     description: str
#     address: str

#     class Config:
#         orm_mode = True


# class RestaurantUpdate(BaseModel):
#     name: str = None
#     description: str = None
#     address: str = None

#     class Config:
#         orm_mode = True


# class TableGet(BaseModel):
#     id: int
#     name: str
#     description: str
#     smoke: bool = False
#     restaurant_id: int

#     class Config:
#         orm_mode = True


# class TableCreate(BaseModel):
#     name: str
#     description: str
#     smoke: bool
#     restaurant_id: int

#     class Config:
#         orm_mode = True


# class TableUpdate(BaseModel):
#     name: str
#     description: str
#     smoke: bool
#     restaurant_id: int

#     class Config:
#         orm_mode = True
