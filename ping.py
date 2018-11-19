from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from flask import Flask, jsonify
import random
import metrics
import env


app = Flask(__name__)
app_dispatch = DispatcherMiddleware(
    app,
    {
        '/metrics': make_wsgi_app(),
    },
)

def is_pong(miss_appearances, hit_appearances):
    miss = miss_appearances * [False]
    hit = hit_appearances * [True]
    return random.choice(miss + hit)


@app.route('/')
def root():
    labels = metrics.get_labels_dict('/')
    metrics.AMOUNT_TIMES_CALLED.labels(**labels).inc()

    hit = is_pong(env.MISS_APPEARANCES, env.HIT_APPEARANCES)
    if hit:
        message = "pong"
    else:
        message = "MISS"

    metrics.PONG_COUNT.labels(**labels,message=message).observe(int(hit))
    return jsonify(message=message)


@app.route('/hello/<user>')
def say_hello_user(user):
    labels = metrics.get_labels_dict(f"/hello/{user}")
    metrics.AMOUNT_TIMES_CALLED.labels(**labels).inc()

    hello_message = f"Hello {user}"
    return jsonify(message=hello_message), 200


@app.route('/health')
def get_health():
    labels = metrics.get_labels_dict("/health")
    metrics.AMOUNT_TIMES_CALLED.labels(**labels).inc()

    health_message = "You should try Ping Pong!"
    return jsonify(message=health_message), 200


@app.route('/metrics')
def expose_metrics():
    labels = metrics.get_labels_dict("/metrics")
    metrics.AMOUNT_TIMES_CALLED.labels(**labels).inc()


if __name__ == '__main__':
    app.run()
