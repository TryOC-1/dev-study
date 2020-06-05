import os


def fileSearch(folder, filetype):
    folder = os.path.abspath(folder)

    for folder, _, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(folder, filename)
            _, endname = os.path.splitext(path)
            if endname[1:] == filetype:
                print(path)


if __name__ == "__main__":
    ftype = input("What are you search file type?: ")
    fileSearch(
        "/Users/gimbogyeong/try_oc_study/airflow-study/d20200604/delicious", ftype
    )
