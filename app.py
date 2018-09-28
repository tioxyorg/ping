from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from flask import Flask, jsonify
from envparse import env
import os


app = Flask(__name__)

# Necessary to expose Prometheus metrics
app_dispatch = DispatcherMiddleware(
    app,
    {
        '/metrics': make_wsgi_app()
    },
)

@app.route('/')
def root():
    return "pong"


@app.route('/hello/<user>')
def say_hello_user(user):
    hello_message = f"Hello {user} NEW VERSION!"
    return hello_message, 200


@app.route('/health')
def get_health():
    health_message = "You should try Ping Pong!"
    return health_message, 200


@app.route('/metrics')
def metrics():
    APP_COMMIT = env.str(
        'APP_COMMIT', default="no-commit-specified"
    )
    desired_metrics = {
        "APP_COMMIT": APP_COMMIT,
    }
    return jsonify(desired_metrics)


if __name__ == '__main__':
    app.run()
