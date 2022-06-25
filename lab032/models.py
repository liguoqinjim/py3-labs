# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ShopScore(Base):
    __tablename__ = 'shop_score'

    id = Column(Integer, primary_key=True, server_default=text("nextval('shop_score_id_seq'::regclass)"))
    x = Column(Numeric)
    y = Column(Numeric)
    version = Column(Integer)
    create_date = Column(DateTime, server_default=text("now()"))
