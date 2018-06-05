from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stayactiv-dev.db'

Base = SQLAlchemy(app)
migrate = Migrate(app, Base)

manager = Manager(app)
manager.add_command('Base', MigrateCommand)

class Activities(Base.Model):
    __tablename__ = 'Activities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    createdDate = Column(DateTime(timezone=True), server_default=func.now(), default=True)
    updatedDate = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Exercises(Base.Model):
    __tablename__ = 'Exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    type = Column(String, nullable=False)
    muscle = Column(String, nullable=False)
    routine = Column(String, nullable=False)
    createdDate = Column(DateTime(timezone=True), server_default=func.now(), default=True)
    updatedDate = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def serialize(self):
        return {
            'id'         : self.id,
            'name'       : self.name,
            'difficulty' : self.difficulty,
            'type'       : self.type,
            'muscle'     : self.muscle,
            'routine'    : self.routine
        }

class WorkoutPrograms(Base.Model):
    __tablename__ = 'WorkoutPrograms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    type = Column(String, nullable=False)
    bodypart = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    routine = Column(String, nullable=False)
    createdDate = Column(DateTime(timezone=True), server_default=func.now(), default=True)
    updatedDate = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'difficulty': self.difficulty,
            'type': self.type,
            'frequency': self.frequency,
            'bodypart' : self.bodypart,
            'routine': self.routine
        }

class ProgramRoutine(Base.Model):
    __tablename__ = 'ProgramRoutine'
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    muscle = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    restTime = Column(Integer, nullable=False)
    previewLink = Column(String, nullable=False)
    createdDate = Column(DateTime(timezone=True), server_default=func.now(), default=True)
    updatedDate = Column(DateTime(timezone=True), onupdate=func.now())
    programId = Column(Integer, ForeignKey(WorkoutPrograms.id))
    exerciseId = Column(Integer, ForeignKey(Exercises.id))
    WorkoutPrograms = relationship('WorkoutPrograms', foreign_keys=[programId])
    Exercises = relationship('Exercises', foreign_keys=[exerciseId])

    @property
    def serialize(self):
        return {
            'id': self.id,
            'week': self.week,
            'day': self.day,
            'muscle': self.muscle,
            'sets': self.sets,
            'repetition' : self.reps,
            'rest time': self.restTime,
            'preview image': self.previewLink
            # 'program Id' : self.programId,
            # 'exercise Id' : self.exerciseId
        }


engine = create_engine('sqlite:///stayactiv-dev.db')
Base.metadata.create_all(engine)

#if __name__ == '__main__':
#    manager.run()