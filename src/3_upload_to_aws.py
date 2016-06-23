import configparser
import os
import tinys3


def should_upload_file(basename, already_uploadead):
    return basename.endswith('.jpg') and \
        basename not in already_uploadead

settings = configparser.RawConfigParser()
settings.read('config.ini')
access_key = settings.get('Amazon', 'AccessKey')
secret_key = settings.get('Amazon', 'SecretKey')

connection = tinys3.Connection(access_key, secret_key)
folders = dict(true='psed-by-email', false='non-psed')

for key in folders:
    bucket = 'psed-or-not-%s' % key
    local_folder = folders[key]
    print(bucket, local_folder)

    already_uploadead = [meta['key'] for meta in connection.list(bucket=bucket)]
    files = list(filter(lambda basename: should_upload_file(basename, already_uploadead),
                   os.listdir(local_folder)))

    print(len(os.listdir(local_folder)), len(files))
    for file_name in files:
        print(file_name)
        image_file = open('/'.join([local_folder, file_name]), 'rb')
        connection.upload(file_name, image_file, bucket)
