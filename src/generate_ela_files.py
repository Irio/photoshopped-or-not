import math
import os
import subprocess
import sys

def path_to_file(folder, file_name):
    return ('%s/%s' % (folder, file_name))

def image_files_in_folder(folder, include_path=True):
    path = lambda file: (path_to_file(folder, file_name)) if include_path else file
    all_files = os.listdir(folder)
    path_list = []
    for file in all_files:
        if file.endswith('.jpg'):
            path_list.append(path(file))
    return path_list

def output_from_input(path):
    file_name = path.split('/')[-1]
    return '/'.join([OUTPUT_FOLDER, file_name])

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))



INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = '%s-ela' % INPUT_FOLDER
images = image_files_in_folder(INPUT_FOLDER, False)
images = [image for image in images if image not in image_files_in_folder(OUTPUT_FOLDER, False)]
images = (map(path_to_file, [INPUT_FOLDER] * len(images), images))
io_paths = map(lambda input_path: (input_path, output_from_input(input_path)), images)

for path_batch in chunker(io_paths, 8):
    processes = []
    for input_file, output_file in path_batch:
        default_options = 'python image-forensics-ela.py --trigger=1 --enhance=50'
        shell_command = '%s %s %s' % (default_options, input_file, output_file)
        process = subprocess.Popen(shell_command, shell=True)
        processes.append(process)
        print(input_file, output_file)
    [process.wait() for process in processes]

# python generate_ela_files.py non-psed
