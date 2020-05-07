import socket

HOST = "127.0.0.1"
PORT = 9000

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 14

<h1>Hello</h1>"""


def print_request(sock: socket.socket, bufsize: int = 1024) -> None:
    response = ""
    data = sock.recv(bufsize)
    response += data.decode("utf-8")

    print("".join(f"< {line}\n" for line in response.splitlines()))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

while True:
    client_connection, client_address = server_socket.accept()
    print(f"New connection from {client_address}")
    print_request(client_connection)
    client_connection.sendall(RESPONSE)
    client_connection.close()
