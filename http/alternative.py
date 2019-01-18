import os, sys, time
from gunicorn import util
from gunicorn.reloader import reloader_engines
from gunicorn.workers.gtornado import TornadoWorker as BaseWorker


class TornadoWorker(BaseWorker):
    def init_process(self):
        if self.cfg.env:
            for k, v in self.cfg.env.items():
                os.environ[k] = v

        util.set_owner_process(
            self.cfg.uid,
            self.cfg.gid,
            initgroups=self.cfg.initgroups
        )

        # Reseed the random number generator
        util.seed()

        # For waking ourselves up
        self.PIPE = os.pipe()
        for p in self.PIPE:
            util.set_non_blocking(p)
            util.close_on_exec(p)

        # Prevent fd inheritance
        for s in self.sockets:
            util.close_on_exec(s)
        util.close_on_exec(self.tmp.fileno())

        self.wait_fds = self.sockets + [self.PIPE[0]]

        self.log.close_on_exec()

        self.init_signals()

        # start the reloader
        if self.cfg.reload:
            def changed(fname):
                self.log.info("Worker reloading: %s modified", fname)
                # todo: call special hook
                self.alive = False
                self.cfg.worker_int(self)
                time.sleep(0.1)
                sys.exit(0)

            reloader_cls = reloader_engines[self.cfg.reload_engine]
            self.reloader = reloader_cls(
                extra_files=self.cfg.reload_extra_files,
                callback=changed
            )
            self.reloader.start()

        self.load_wsgi()
        self.cfg.post_worker_init(self)

        # Enter main run loop
        self.booted = True
        self.run()

    def heartbeat(self):
        if not self.alive:
            if self.server_alive:
                if hasattr(self, 'server'):
                    try:
                        self.server.stop()
                    except Exception:
                        pass
                self.server_alive = False
            else:
                if not hasattr(self.ioloop, '_callbacks') or not self.ioloop._callbacks:
                    self.ioloop.stop()
