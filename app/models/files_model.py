
from pymongo import MongoClient
from flask import jsonify, request, make_response
from dotenv import load_dotenv
from os import getenv
from http import HTTPStatus
import gridfs


load_dotenv()
allowed_extensions = getenv('ALLOWED_EXTENSIONS')
download_location = getenv('DOWNLOAD_LOCATION')

client = MongoClient('mongodb://localhost:27017/')

db = client['files']

fs = gridfs.GridFS(db)


class FilesModel:
    
    def __init__(self):
        pass


    @staticmethod
    def is_file_in_directory():
        name_list = []
        files_list = list(db.fs.files.find())
        for files in files_list:
            if files['filename'] not in name_list:
                name_list.append(files['filename'])

        return name_list


    @staticmethod
    def list_all_files():
        files_list = list(db.fs.files.find())
        for files in files_list:
            files['_id'] = str(files['_id'])
        return jsonify(files_list)


    @staticmethod
    def list_all_files_by_extension(extension):
        files_list = list(db.fs.files.find())
        files_by_extension_list = []
        if extension not in allowed_extensions:
            return make_response({'message': f"No files found with the extension '{extension}'."}, HTTPStatus.NOT_FOUND)
        else:
            for files in files_list:
                file_extension = files['filename'].split('.')[-1]
                if file_extension in allowed_extensions and file_extension == extension:
                    files_by_extension_list.append(files)

            for files in files_by_extension_list:
                files['_id'] = str(files['_id'])

            return jsonify(files_by_extension_list)


    @staticmethod
    def upload_file():
        file_to_be_uploaded = request.files['file']
        file_extension = file_to_be_uploaded.content_type.split('/')[1]

        if file_extension in allowed_extensions:
            if file_to_be_uploaded.filename in FilesModel.is_file_in_directory():
                return make_response({'message': f"A file with name '{file_to_be_uploaded.filename}' already exists."}, HTTPStatus.CONFLICT)
            else:
                contents = file_to_be_uploaded.read()

                fs.put(contents, filename=file_to_be_uploaded.filename)

                return {'message': f"File '{file_to_be_uploaded.filename}' uploaded successfully!"}

        else:
            return make_response({'message': f"The extension '{file_extension}' is not supported."}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE)


    @staticmethod
    def download_file(filename):
        file = db.fs.files.find_one({'filename': filename})
        file_id = file['_id']

        if filename not in FilesModel.is_file_in_directory():
            return make_response({'message': f"File '{filename}' does not exist."}, HTTPStatus.NOT_FOUND)

        file_to_download = fs.get(file_id).read()
        folder = download_location + file['filename']
        with open (folder, 'wb') as downloader:
            downloader.write(file_to_download)
        return {'message': 'File downloaded successfully!'}
