import random
import string
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {}

def generate_room_id():
    """Generate a random room ID"""
    id_length = 5
    return ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(id_length))

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('create')
def on_create():
    """Create a game lobby"""
    room_id = generate_room_id()
    ROOMS[room_id] = 'ROOM ID' + room_id
    join_room(room_id)
    emit('join_room', {'room': room_id})

if __name__ == '__main__':
    socketio.run(app, debug=True)
