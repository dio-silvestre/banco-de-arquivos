from flask import request
from http import HTTPStatus
from app.models.files_model import FilesModel


def download(filename: str):
    return FilesModel.download_file(filename), HTTPStatus.OK


def list_files():
    return FilesModel.list_all_files(), HTTPStatus.OK


def list_files_by_extension(extension: str):
    return FilesModel.list_all_files_by_extension(extension), HTTPStatus.OK


def upload():
    return FilesModel.upload_file(), HTTPStatus.CREATED


def largefile_error(e):
    file_size = request.headers.get('Content-Length')
    return {'msg': f"This file's size ({file_size}B) exceeds the maximum size allowed (50MB)."}, HTTPStatus.REQUEST_ENTITY_TOO_LARGE
