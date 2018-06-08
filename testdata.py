from sqlalchemy.orm import sessionmaker, lazyload
from sqlalchemy import and_, inspect
from sqlalchemy import create_engine, inspect
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.ext.declarative import declarative_base
from database import Activities, ProgramRoutine, Exercises
from flask import jsonify, json

Base = declarative_base()
engine = create_engine('sqlite:///stayactiv-dev.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

for u in dbsession.query(ProgramRoutine).all():
    Exercises = u.Exercises.__dict__
    workoutprograms = u.WorkoutPrograms.__dict__
    progam = u.__dict__
#
progam["Exercises"] = Exercises
progam["WorkoutPrograms"] = workoutprograms
print(progam)
progam.pop(Exercises)
print(progam)
#
# #new = dict(progam)
# d = json.JSONEncoder(progam)
# e = json.JSONDecoder(d)
# print()