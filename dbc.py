import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    token = Column(String(36), nullable=False)
    avatar_uuid = Column(String(250), nullable=True)


engine = create_engine('postgresql+psycopg2://wad-adm:StrongPassw0rd@127.0.0.1:55437/wad_db')
Base.metadata.create_all(engine)
