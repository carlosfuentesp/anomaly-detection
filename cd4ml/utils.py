import os


def ensure_dir_exists(directory):
    """If a directory doesn't exist, create it."""
    
    :param directory:
    :return:
    if not os.path.exists(directory):
        os.makedirs(directory)
