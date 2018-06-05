from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.ext.declarative import declarative_base
from database import Activities, ProgramRoutine
import datetime

Base = declarative_base()
engine = create_engine('sqlite:///stayactiv-dev.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
dbsession = DBSession()


#Query = dbsession.query(Activities).all()
list = dbsession.query(ProgramRoutine).all()

for activity in list:
    print(activity.name)

