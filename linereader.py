import os
from pathlib import Path
import inspect


def read_file(file_name):
    # If relative path, make it relative to the caller's script
    if not os.path.isabs(file_name):
        caller_frame = inspect.stack()[1]
        caller_path = Path(caller_frame.filename).parent
        file_name = caller_path / file_name
    
    with open(file_name, "r") as f:
        return [line.replace('\n', '') for line in f]


def read_lines(file_name, token):
    # If relative path, make it relative to the caller's script
    if not os.path.isabs(file_name):
        caller_frame = inspect.stack()[1]
        caller_path = Path(caller_frame.filename).parent
        file_name = caller_path / file_name
    
    with open(file_name, 'r') as f:
        return [line.replace('\n', '').split(token) for line in f]


def read_line(file_name, token):
    # If relative path, make it relative to the caller's script
    if not os.path.isabs(file_name):
        caller_frame = inspect.stack()[1]
        caller_path = Path(caller_frame.filename).parent
        file_name = caller_path / file_name
    
    with open(file_name, 'r') as f:
        line = f.readline()

        if token is None:
            return line
        if token == '':
            return list(line)
        return line.split(token)


def read_parts(file_name, delim, split_instructions):
    arr = read_file(file_name)

    part = []
    parts = dict().fromkeys(split_instructions)
    i = 0
    for idx, item in enumerate(arr):
        if item != delim:
            part.append(item)

        if item == delim or idx == len(arr) - 1:
            parts[split_instructions[i]] = part
            part = []
            i += 1

    return parts