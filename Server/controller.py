import pickle
from socket import *

from constants import *


def search(filename, list_of_files):
    """
    :type list_of_files: dict
    """
    found = False
    return_data = {}
    for key in list_of_files:
        print (list_of_files[1]['shared_files'])
        if filename in list_of_files[1]['shared_files']:
            if not found:
                found = True
            return_data[1] = list_of_files[1]
    return found, return_data


def register(conn, list_of_files, peer_data_object=None):
    """
    :param conn:
    :param set_of_lists: dict
    :param peer_data_object: dict
    :return: None
    """
    if peer_data_object is None:
        peer_data_object = list()
    list_id = len(list_of_files) + 1  # allocate list_id
    list_of_files.append(peer_data_object)
    conn.send(pickle.dumps([list_id, True]))  # return ID


def append(conn, request, list_of_files):
    list_id = request[2]  # fetch list_id
    data = request[1]  # fetch data to append
    list_of_files.append(data)
    conn.send(pickle.dumps(OK))  # return an OK
