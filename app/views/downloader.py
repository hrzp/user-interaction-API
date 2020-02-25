from app.utils.common import upsert_user_directory, cwd_data
from app.utils.response_handler import Response
from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path
import connexion
import os


def download(username, filename):
    """
    This function download the user file in the user directory.
    :url /api/download/{username}/{filename}:   path
    :param username:    username in data directory
    :param file:        file to download in user directory
    :return:            200 on success, 400 on errors
    """

    directory = os.path.join(cwd_data(), username)
    file_path = os.path.join(directory, filename)

    # return error if file or directory not found
    if (not Path(file_path).is_file()):
        return Response.failure("File Not found")

    # send file to client
    return send_from_directory(
        directory=directory, filename=filename, as_attachment=True)
