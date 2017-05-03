"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import jsonify, request
from MadproBot import app
from MadproBot.responses import reply_to_line

@app.route('/')
@app.route('/home')
def home():
    return jsonify({
        "message": "this endpoint is active"
    })

@app.route('/webhook', methods=['POST'])
def webhook():
    reply_to_line(request.json)
    return '', 200, {}
