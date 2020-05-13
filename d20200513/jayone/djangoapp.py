import sys

from helloworld import wsgi  # noqa: E402

sys.path.insert(0, "./helloworld")

app = wsgi.application
