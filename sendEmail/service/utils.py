from time import time_ns
from uuid import uuid4


def gen_unique_cod():
    return f"{time_ns()}{str(uuid4()).replace('-', '')}"



