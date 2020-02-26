from app.utils.response_handler import Response
from app.utils.validator import requirment
import app.utils.common as utils
import os


@requirment('name', 'value')  # check paramters
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


@requirment('name', 'value')  # check paramters
def set_global_data(data):
    """
    This function inserts a key, value in global data.json in the main directory.
    if the key has existed it replaced the value.
    work same as set_user_data
    :url /api/setGlobalData/:   path
    :param data:                name and value to submit
    :return:                    201 on create, 200 on update, 400 on errors
    """

    # create the user data.json path
    path = os.path.join(utils.cwd_data(), "global_data.json")

    # insert key, value. updated if exist
    status_code = utils.upsert_data(path, data['name'], data['value'])
    message = 'Data submitted' if status_code == 201 else "Data updated"
    return Response.success(message=message, payload=data, status_code=status_code)


def get_user_data(username):
    """
    This function fetches all data from user and global data files and returns them.
    In duplicate data, User data is prioritized
    :url /api/getUserData/{username}:   path
    :param username:                    username in data directory
    :return:                            200 on success, 400 on errors
    """

    # create the user data.json path
    path = os.path.join(utils.cwd_data(), username, "data.json")

    # create the global data.json path
    global_path = os.path.join(utils.cwd_data(), "global_data.json")

    # Collect global data first and update with user data
    # It will replace duplicate global data with users
    result = dict()
    result = utils.get_data(global_path)
    result.update(utils.get_data(path))

    # produce the desired response
    data = list(
        map(lambda key_value:
            {
                "name": key_value[0],
                "value": key_value[1]
            },
            result.items()
            )
    )

    return Response.success("", payload=data)
