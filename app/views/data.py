from app.utils.response_handler import Response
import app.utils.common as utils
import os


def set_user_data(username, data):
    """
    This function inserts a key, value in user data.json in the own user directory.
    if the key has existed it replaced the value.
    :url /api/setUserData/{username}:   path
    :param username:                    username in data directory
    :param data:                        name and value to submit
    :return:                            201 on create, 200 on update, 400 on errors
    """

    # create the user directory if not exist
    utils.upsert_user_directory(username)

    # create the user data.json path
    path = os.path.join(utils.cwd_data(), username, "data.json")

    # insert key, value. updated if exist
    status_code = utils.upsert_data(path, data['name'], data['value'])
    message = 'Data submitted' if status_code == 201 else "Data updated"
    return Response.success(message=message, payload=data, status_code=status_code)
