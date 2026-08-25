from glob import glob
import os
import zipfile
import shutil

def unzip(filepath, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    extracted = []

    with zipfile.ZipFile(filepath, 'r') as zf:
        for member in zf.infolist():
            if member.is_dir():
                continue

            member_path = os.path.normpath(member.filename)
            target_path = os.path.join(target_directory, member_path)

            abs_target = os.path.abspath(target_path)
            abs_root = os.path.abspath(target_directory)
            if not abs_target.startswith(abs_root + os.sep):
                raise ValueError(f'Refusing to extract {member.filename}')

            zf.extract(member, target_directory)
            extracted.append(target_path)

    os.remove(filepath)
    return extracted

def flatten():
    filepaths = glob('source-store/dehessen/*/*/*.tif')
    name_to_path = {}
    for filepath in filepaths:
        filename = filepath.split('/')[-1]
        if filename not in name_to_path:
            name_to_path[filename] = []
        name_to_path[filename].append(filepath)
    for filename in name_to_path.keys():
        os.rename(name_to_path[filename][0], f'source-store/dehessen/{filename}')

    # remove dirs
    for filepath in glob('source-store/dehessen/*'):
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
    

def main():
    # outer
    filepaths = glob('source-store/dehessen/*.zip')
    for filepath in filepaths:
        target_directory = filepath.replace('.zip', '')
        unzip(filepath, target_directory)

    # inner
    filepaths = glob('source-store/dehessen/*/*.zip')
    for filepath in filepaths:
        target_directory = filepath.replace('.zip', '')
        unzip(filepath, target_directory)

    flatten()


if __name__ == '__main__':
    main()