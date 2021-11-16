from flask import Flask
from app.controllers.files_controller import download, list_files, list_files_by_extension, upload, largefile_error


def files_route(app: Flask):
    app.get('/download/<string:filename>')(download)
    app.get('/files')(list_files)
    app.get('/files/<string:extension>')(list_files_by_extension)
    app.post('/upload')(upload)
    app.errorhandler(413)(largefile_error)