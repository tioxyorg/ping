# ping

Installation
```sh
pipenv update
```

Running
```sh
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app_dispatch
```
