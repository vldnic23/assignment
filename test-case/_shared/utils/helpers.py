from datetime import datetime
import os
from _shared.utils.constants import DATE_FORMAT


def log(s):
    print(f'{datetime.now().strftime(f"{DATE_FORMAT} %H:%M:%S")}: {s}')


def get_env_var(var_name):
    var = os.getenv(var_name, None)
    if not var:
        raise Exception("{} environment variable is required!".format(var_name))
    return var
