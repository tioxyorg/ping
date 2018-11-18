from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import Counter, Summary, make_wsgi_app
from flask import Flask, jsonify
from envparse import env
import os


APP_NAME = 'ping'
app = Flask(__name__)

required_prometheus_labels = ['endpoint', 'app', 'hostname']
AMOUNT_TIMES_CALLED = Counter('amount_times_called', 'Amount of times a function was called', required_prometheus_labels)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', required_prometheus_labels)

# Necessary to expose Prometheus metrics
app_dispatch = DispatcherMiddleware(
    app,
    {
        '/metrics': make_wsgi_app(),
    },
)


def get_labels_dict(*metric_values):
    labels = {
        "app": APP_NAME,
        "hostname": os.environ['HOSTNAME'],
    }
    for i, value in enumerate(metric_values):
        labels[required_prometheus_labels[i]] = value
    return labels


@app.route('/')
def root():
    return "pong"


@app.route('/hello/<user>')
def say_hello_user(user):
    labels = get_labels_dict(f"/hello/{user}")
    AMOUNT_TIMES_CALLED.labels(**labels).inc()

    hello_message = f"Hello {user}"
    return hello_message, 200


@app.route('/health')
def get_health():
    labels = get_labels_dict("/health")
    AMOUNT_TIMES_CALLED.labels(**labels).inc()

    health_message = "You should try Ping Pong!"
    return health_message, 200


@app.route('/metrics')
def metrics():
    labels = get_labels_dict("/metrics")
    AMOUNT_TIMES_CALLED.labels(**labels).inc()


if __name__ == '__main__':
    app.run()
