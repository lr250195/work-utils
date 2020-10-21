import os
import time
import shutil
import configparser

folder = 'entregas-reportes'

configs = configparser.ConfigParser()
configs.read('../../folders.ini')

path = configs[folder]['url']


def list_files(directory):
    return os.listdir(directory)


def get_files(list_of_files):
    list = []
    for element in list_of_files:
        if "." in element:
            list.append(element)
    return list


def get_file_date(file_path):
    return time.strftime("%Y%m%d", time.localtime(os.path.getctime(file_path)))


file_list = list_files(path)
files = get_files(file_list)

for file in files:
    original_path = f'{path}/{file}'
    date = get_file_date(original_path)
    destination_path = f'{path}/{date}'

    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    shutil.move(original_path, f'{destination_path}/{file}')

