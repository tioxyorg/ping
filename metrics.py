from prometheus_client import Histogram, Counter, Summary, Info
import env

# Default labels
metric_label_keys = ['endpoint', 'app', 'hostname']

# Metrics
AMOUNT_TIMES_CALLED = Counter('amount_times_called', 'Amount of times a function was called', metric_label_keys)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', metric_label_keys)
PONG_REQUESTS = Counter('pong_requests_total', 'Total times you hit your PONG', metric_label_keys)
MISS_REQUESTS = Counter('miss_requests_total', 'Total times you missed your PONG', metric_label_keys)

def get_labels_dict(*metric_values):
    labels = {
        "app": env.APP_NAME,
        "hostname": env.HOSTNAME,
    }
    for i, label_value in enumerate(metric_values):
        labels.__setitem__(metric_label_keys[i], label_value)
    return labels
