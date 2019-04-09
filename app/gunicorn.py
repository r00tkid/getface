import os

# [IMPORT] settings
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

spec = spec_from_loader(
    "settings",
    SourceFileLoader(
        "settings",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
    ))
settings = module_from_spec(spec)
spec.loader.exec_module(settings)
# [END] settings

chdir = settings.BASE_DIR
worker_class = 'alternative'
backlog = 2048

if settings.DEBUG:
    bind = '0.0.0.0:8091'
else:
    bind = '0.0.0.0:8090'

workers = 1 if settings.DEBUG else (2 * os.cpu_count() + 1)
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
    'DJANGO_SECRET_KEY=%s' % settings.SECRET_KEY,
    'PROJECT_ROOT=%s' % settings.BASE_DIR,
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
