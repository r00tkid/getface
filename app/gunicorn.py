import os
from app import settings

bind = '0.0.0.0:8090'
backlog = 2048

workers = 1 if settings.DEBUG else (2 * os.cpu_count() + 1)
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False

reload = True
max_requests = 2000
max_requests_jitter = 1500

daemon = False
raw_env = [
    'DJANGO_SECRET_KEY=%s' % settings.SECRET_KEY,
]
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = os.path.join(settings.LOGS_DIR, 'gunicorn.debug.log') if settings.DEBUG \
    else os.path.join(settings.LOGS_DIR, 'gunicorn.error.log')
accesslog = os.path.join(settings.LOGS_DIR, 'gunicorn.access.log')
loglevel = 'debug' if settings.DEBUG else 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = 'gunicorn'


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    server.log.info("Spawning worker")


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")

#capture_output = True