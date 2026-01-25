import os
import sys
from flask import Flask
from flask_socketio import SocketIO 

# Setup Paths for PyInstaller support
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    # Assumes templates/static are in the root folder, one level up from 'app'
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.secret_key = os.urandom(24)

# This will now work correctly because it is using the correct class
socketio = SocketIO(app)

# Import routes at the end to avoid circular imports
from app import routes