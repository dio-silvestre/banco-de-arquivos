from flask import Flask


def init_app(app: Flask):
    from app.routes.files_route import files_route
    files_route(app)

    return app