import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.abspath(os.path.join(BASE_DIR, 'project', 'log'))

if os.environ.get('DJANGO_ENVIRONMENT_MOD') == 'dev':
    DEBUG = True
else:
    DEBUG = False

chdir = BASE_DIR
worker_class = 'alternative'
backlog = 2048

if DEBUG:
    bind = '0.0.0.0:8091'
else:
    bind = '0.0.0.0:8090'

workers = 1 if DEBUG else (2 * os.cpu_count() + 1)
worker_connections = 1000
timeout = 30
keepalive = 2

spew = False

reload = True
reload_engine = 'poll'
max_requests = 2000
max_requests_jitter = 1500

daemon = False

raw_env = [
    'PROJECT_ROOT=%s' % BASE_DIR,
]

pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = os.path.join(LOGS_DIR, 'gunicorn.debug.log') if DEBUG else os.path.join(LOGS_DIR, 'gunicorn.error.log')
accesslog = os.path.join(LOGS_DIR, 'gunicorn.access.log')
loglevel = 'debug' if DEBUG else 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = 'gunicorn'


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def pre_fork(server, worker):
    server.log.info("Spawning worker")


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def worker_int(worker):
    """
    @type worker: gunicorn.workers.base.Worker
    """
    worker.log.info("worker received INT or QUIT signal")


def post_worker_init(worker):
    """
    @type worker: gunicorn.workers.base.Worker
    """
    # from gunicorn.reloader import reloader_engines
    #
    # def changed(filename):
    #     print(filename)
    #
    # worker.reloader = reloader_engines[
    #     worker.cfg.reload_engine
    # ](extra_files=worker.cfg.reload_extra_files, callback=changed)
    # worker.reloader.start()
    worker.log.info("Post init done.")


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")

# capture_output = True
