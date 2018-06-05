from flask import Flask, jsonify
from sqlalchemy import create_engine, and_, distinct
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from database import Base, Activities, Exercises, WorkoutPrograms, ProgramRoutine

engine = create_engine('sqlite:///stayactiv-dev.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

app = Flask(__name__)

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.route('/')
def hello_world():
  return '<body><h2>Welcome to StayActiv</h2>' \
         '<ul><li><a href="https://stayactiv.azurewebsites.net/activities">Activities</a>' \
         '</li><li><a href="https://stayactiv.azurewebsites.net/exercises">Exercises</a>' \
         '</li><li><a href="https://stayactiv.azurewebsites.net/WorkoutPrograms">Workout Programs</a>' \
         '</li><li><a href="https://stayactiv.azurewebsites.net/ProgramRoutine">Program Routine</a></li>' \
         '</ul></body>'

@app.route('/activities', methods=['GET'])
def get_activities():
    try:
        List = dbsession.query(Activities).all()
    except:
        NoResultFound

    return jsonify(Ativities=[i.serialize for i in List])


@app.route('/exercises', methods=['GET'])
def get_exercises():
    try:
        List = dbsession.query(Exercises).all()
    except:
        NoResultFound

    return jsonify(Exercises=[i.serialize for i in List])


@app.route('/WorkoutPrograms', methods=['GET'])
def get_workoutPrograms():
    try:
        List = dbsession.query(WorkoutPrograms).all()
    except:
        NoResultFound

    return jsonify(WorkoutPrograms=[i.serialize for i in List])


@app.route('/ProgramRoutine', methods=['GET'])
def get_programRoutine():
    try:
        list = dbsession.query(ProgramRoutine).all()
    except:
        NoResultFound

    return jsonify(ProgramRoutine=[i.serialize for i in list])


if __name__ == '__main__':
  #app.debug = True
  app.run()