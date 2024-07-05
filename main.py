import os
import sys
from config.env import ENV
from cronjob import cronjob
from app import run_gunicorn_server, run_flask_debug_server


if __name__ == "__main__":
    app_name = sys.argv[1]
    app_names = ["main", "cronjob", ""]
    if app_name not in app_names:
        print("invalid argument:", app_name, "\nprovide one of:", *app_names)
        exit(1)
    if app_name == "":
        app_name = "main"
    
    if app_name == "main":
        if ENV in ["development"]:
            run_flask_debug_server()
        else:
            run_gunicorn_server()
    
    if app_name == "cronjob":
        cronjob()
