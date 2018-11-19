from prometheus_client import Histogram, Counter, Summary, Info
import env


metric_label_keys = ['endpoint', 'app', 'hostname']
AMOUNT_TIMES_CALLED = Counter('amount_times_called', 'Amount of times a function was called', metric_label_keys)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', metric_label_keys)
PONG_COUNT = Histogram('pong_count', 'Total times you missed your PONG', metric_label_keys+['message'])


def get_labels_dict(*metric_values):
    labels = {
        "app": env.APP_NAME,
        "hostname": env.HOSTNAME,
    }
    for i, label_value in enumerate(metric_values):
        labels.__setitem__(metric_label_keys[i], label_value)
    return labels
