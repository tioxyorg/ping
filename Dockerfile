FROM python:3.7.0-alpine
LABEL maintainer="gabrieltiossi@gmail.com"
ARG APP_COMMIT=null

# GCC is required for uWSGI
RUN apk add --no-cache \
    gcc \
    libc-dev \
    musl-dev \
    linux-headers \
 && pip install --upgrade pipenv

WORKDIR /app/
COPY . /app/
RUN python setup.py install

# To install dev-packages from setup.py
# RUN pip install -e .[dev]

EXPOSE 5000
CMD [ "uwsgi",                      \
      "--http", "0.0.0.0:5000",     \
      "--wsgi-file", "app.py",      \
      "--callable", "app_dispatch"  ]
