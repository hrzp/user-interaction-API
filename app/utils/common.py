"""
Here we define the most commonly used and repetitive functions
"""
from pathlib import Path
import json
import pickle
import os


def upsert_user_directory(username):
    """
    This function checks the user directory if not exist, creates it.
    """
    Path(os.path.join(
        "data", username)
    ).mkdir(parents=True, exist_ok=True)


def check_data_file(path):
    """
    Create a new file if not exist
    """
    Path(path).touch(exist_ok=True)


def cwd_data():
    """
    This function return the data directory path
    """
    return os.path.join(os.getcwd(), "data")


def upsert_data(path, name, value):
    """
    This function get a path of a json file and insert a name, value
    to it.
    """
    # create file if not exist
    check_data_file(path)
    latest_data = dict()
    # Specifies the update code or new item
    status_code = 201

    # Ignore if the file was empty
    try:
        pickle_in = open(path, "rb")
        latest_data = pickle.load(pickle_in)
        pickle_in.close()
    except EOFError:
        pass

    if name in latest_data:
        status_code = 200

    # update and write new value to file
    latest_data.update({name: value})
    pickle_out = open(path, "wb")
    pickle.dump(latest_data, pickle_out)
    pickle_out.close()

    return status_code


def get_data(path):
    data = dict()
    # Ignore if the file was empty
    try:
        pickle_in = open(path, "rb")
        data = pickle.load(pickle_in)
        pickle_in.close()
    except EOFError:
        pass
    except FileNotFoundError:
        pass
    return data
