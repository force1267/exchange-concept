import gunicorn.app.base
from config import gunicorn as config
from app.flask_app import app as flask_app

class GunicornServer(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()
    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)
    def load(self):
        return self.application


def run_gunicorn_server():
    options = {
        'bind': config.bind,
        'workers': config.workers,
        'threads': config.threads
    }
    GunicornServer(flask_app, options).run()
