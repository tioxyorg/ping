import socket
import envparse


HOSTNAME = socket.getfqdn()
APP_NAME = 'ping'
APP_COMMIT = envparse.env.str('APP_COMMIT', default="null")
MISS_APPEARANCES = envparse.env.int('MISS_APPEARANCES', default=50)
HIT_APPEARANCES = envparse.env.int('HIT_APPEARANCES', default=50)
