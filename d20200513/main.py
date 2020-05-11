from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "yourpassword"
socketio = SocketIO(app)


@app.route("/")
def session():
    return render_template("session.html")


def messageRecevied(methods=["GET", "POST"]):
    print("message was received!!!!! ")


@socketio.on("my event")
def handle_my_custom_event(json, methods=["GET", "POST"]):
    print("recevied my event" + str(json))
    socketio.emit("my response", json, callback=messageRecevied)


if __name__ == "__main__":
    socketio.run(app, debug=True)
