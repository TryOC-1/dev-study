import os


def fill_interval_file(folder, prefix="spam"):
    folder = os.path.abspath(folder)

    files = []
    for filename in os.listdir(folder):
        if filename.startswith(prefix):
            files.append(filename)

    files.sort()
    print(files)

    # TODO : start number
    file = files[0]
    base, ext = os.path.splitext(file)
    start = int(base[len(prefix) :])

    # TODO : counting
    for f in files:
        expect = f"{prefix}{start:03d}{ext}"
        print("origin: " + f)
        print(f"expect: {prefix}{start:03d}{ext}")
        start += 1

        if f != expect:
            origin_path = os.path.join(folder, f)
            expect_path = os.path.join(folder, expect)
            os.rename(origin_path, expect_path)


fill_interval_file("/Users/gimbogyeong/try_oc_study/airflow-study/d20200604/test")
