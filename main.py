from flask import Flask, jsonify

app = Flask(__name__)

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.route('/')
def hello_world():
  return '<H1>Hello, Welcome to StayActiv!</H1>'


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    #return "Welcome"
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
  app.run()