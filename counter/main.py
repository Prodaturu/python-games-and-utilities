import counter_app
from counter_app import home_page, app, show, db

@app.route('/') #run this function when on the given path
def home():
  return '<h1>Hello</h1>'

@app.route('/increment')
def increment():
  return 'increment'

app.run(host='0.0.0.0',port=81)
