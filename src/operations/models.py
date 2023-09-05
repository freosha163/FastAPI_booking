# from sqlalchemy import (Table,
#                         Column,
#                         Integer,
#                         String,
#                         TIMESTAMP,
#                         DateTime,
#                         ForeignKey,
#                         Boolean
#                         )
# from auth.models import User
# from database import metadata


# restaurant = Table(
#     'restaurant',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False),
#     Column('description', String),
#     Column('address', String, nullable=False),
# )


# booking = Table(
#     'booking',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('from_date', TIMESTAMP),
#     Column('to_date', DateTime),
#     Column('user_id', ForeignKey(User.id)),
#     Column('restaurant_id', ForeignKey(restaurant.c.id)),
# )


# table = Table(
#     'table',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('description', String),
#     Column('smoke', Boolean),
#     Column('restaurant_id', Integer, ForeignKey(restaurant.c.id)),
# )
