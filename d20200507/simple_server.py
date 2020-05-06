import socket

HOST = "127.0.0.1"
PORT = 9000

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 14

<h1>Hello</h1>"""


# AF_INET(ipv4 주소를 사용하는, IP), SOCK_STREAM(연결형 통신, TCP)의 소켓 생성 => TCP/IP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 해당 소켓을 재사용할 수 있도록 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 소켓의 IP 주소 및 포트 설정
server_socket.bind((HOST, PORT))
# 최대 1개 까지 connection(연결) 유지
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

while True:
    client_connection, client_address = server_socket.accept()
    print(f"New connection from {client_address}")
    # RESPONSE 데이터 전달
    client_connection.sendall(RESPONSE)
    # 해당 소켓과 접속 끊음
    client_connection.close()
