import re


def parse_url(data: str) -> list:
    regex = re.compile(r"(https?:\/\/.*?)(\/.*)")

    regex_results = regex.findall(data)

    results = []
    for url, path in regex_results:
        results.append(Url(url, path))
    return results


class Url:
    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path
        self.query = {}

        self.parse_path(path)

    def parse_path(self, path: str):
        path, _, raw = path.partition("?")

        if raw == "":
            return

        self.path = path

        splited_datas = raw.split("&")
        for data in splited_datas:
            key, _, value = data.partition("=")
            self.query[key] = value


if __name__ == "__main__":
    data = """
    https://github.com/TryOC-1/dev-study/issues/32
    https://stackoverflow.com/questions/43627405/understanding-getitem-method
    https://www.google.com/search?sxsrf=ALeKk01yDJb2NjNj3_WyVxENS1sKmrIZfA%3A1590064004073&source=hp&ei=hHPGXrjxAdSi-QbHt5WwAQ&q=find&oq=find&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCABQ-QVYowhgpAloAHAAeACAAXGIAaADkgEDMS4zmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwi4w4WB-sTpAhVUUd4KHcdbBRYQ4dUDCAc&uact=5
    """

    parsed_datas = parse_url(data)

    for data in parsed_datas:
        print(data.query)
