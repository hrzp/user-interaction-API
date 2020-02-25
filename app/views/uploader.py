from app.utils.common import upsert_user_directory
from app.utils.response_handler import Response
from werkzeug.utils import secure_filename
from flask import request, jsonify
import connexion
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(username):
    """
    This function upload the user file in the user directory.
    :url /api/upload:   path
    :param username:    username in data directory
    :param file:        file to upload in user directory
    :return:            201 on success, 400 on validation errors
    """
    # get the files from connexion
    file = connexion.request.files
    if 'file' not in file:
        resp = jsonify({'message': 'No file part in the file'})
        resp.status_code = 400
        return resp
    file = file['file']
    if file.filename == '':
        return Response.failure('No file selected for uploading')

    # TODO: should check the file size

    # create the user directory if not exist
    upsert_user_directory(username)

    # check for a clean file extension
    if not (file and allowed_file(file.filename)):
        return Response.failure('Allowed file types are txt, pdf, png, jpg, jpeg, gif')

    # srcure the file name and save it on disk
    filename = secure_filename(file.filename)
    file.save(os.path.join(os.getcwd(), 'data', username, filename))
    return Response.success('File successfully uploaded', status_code=201)
