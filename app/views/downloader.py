from app.utils.common import upsert_user_directory
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
    try:
        directory = os.path.join(os.getcwd(), "data", username)
        if (not Path(os.path.join(directory, filename)).is_file()):
            return Response.failure("File Not found")
        return send_from_directory(
            directory=directory, filename=filename, as_attachment=True)
    except FileNotFoundError:
        return Response.failure("File Not found")
