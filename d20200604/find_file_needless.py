import enum
import os


class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


def convert_unit(size_in_bytes, unit):
    if unit == SIZE_UNIT.KB:
        return size_in_bytes / 1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes / (1024 * 1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes / (1024 * 1024 * 1024)
    else:
        return size_in_bytes


def get_file_size(file_name, size_type=SIZE_UNIT.BYTES):
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)


def findFile(folder):
    folder = os.path.abspath(folder)

    for foldername, _, filenames in os.walk(folder):
        print(foldername)

        for filename in filenames:
            path = os.path.join(foldername, filename)
            temp = get_file_size(path, SIZE_UNIT.MB)
            if temp <= 100:
                print("filename: %s, filesize: %fMB" % (path, temp))


findFile("/Users/gimbogyeong/try_oc_study/airflow-study/d20200604")
