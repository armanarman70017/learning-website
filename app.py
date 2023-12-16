from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': '$1000'
}, {
    'id': 2,
    'title': 'Developer',
    'location': 'New Delhi',
    'salary': '$500'
}]


@app.route('/')
def hello_world():
  return render_template('DemoHome.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
