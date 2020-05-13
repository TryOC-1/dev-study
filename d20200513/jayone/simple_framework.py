def app(environ, start_response):
    """A barebones WSGI app."""
    status = "200 OK"
    response_headers = [("Content-Type", "text/plain"), ("Content-Length", 13)]
    start_response(status, response_headers)
    return [b"Hello World!\n"]
