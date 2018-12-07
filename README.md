# ping
# Comment

### Installation
------
```sh
pipenv update
```

### Running
------
```sh
uwsgi --http 0.0.0.0:5000 --wsgi-file ping.py --callable app_dispatch
```

### Testing
------
```sh
pytest -s -p no:warnings tests/
```

### Environment Variables
- **HIT_APPEARANCES** (int): Amount of Hit appearances to be chosen
- **MISS_APPEARANCES** (int): Amount of Miss appearances to be chosen
 
