"""
Here we define the most commonly used and repetitive functions
"""
from pathlib import Path
import os


def upsert_user_directory(username):
    """
    This function checks the user directory if not exist, creates it.
    """
    Path(os.path.join(
        "data", username)
    ).mkdir(parents=True, exist_ok=True)
