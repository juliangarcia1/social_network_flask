from flask import Flask,g
import models
from flask.ext.login import LoginManager

DEBUG =True
PORT=8000
HOST='0.0.0.0'

app = Flask(__name__)
app.secret_key='sdsads9878d967986324/(()/&(...adaewer)'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id==user_id)
    except models.DoesNotExist:
        pass


@app.before_request
def before_request():
    """Connect to the database before each request"""
    # g.db =
    pass


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
        username='Julian',
        email='juliancatorce@gmail.com',
        password='password'
    )
    app.run(debug=True,
            host=HOST,
            port=PORT)
