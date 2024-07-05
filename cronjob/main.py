from app.controller.settle import settle


def cronjob():
    settle()