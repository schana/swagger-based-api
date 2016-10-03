import flask

from api import api
from api.subparts.alpha import alpha
from api.subparts.beta import beta

app = flask.Flask(__name__)
app.register_blueprint(api.api.blueprint)
app.register_blueprint(alpha.api.blueprint)
app.register_blueprint(beta.api.blueprint)
app.config['RESTPLUS_VALIDATE'] = True
application = app

if __name__ == '__main__':
    application.run(debug=True)
