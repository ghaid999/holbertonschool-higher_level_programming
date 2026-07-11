#!/usr/bin/python3
"""
Module task_04_flask

A simple RESTful API built with Flask. Stores users in memory and
exposes endpoints to list, retrieve, and add users.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Return a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return a simple status string to confirm the API is running."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Return the full user object for the given username.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the in-memory users dictionary.
    """
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
