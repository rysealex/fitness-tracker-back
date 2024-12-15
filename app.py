from flask import Flask, request, jsonify
from user import UserStats, User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
'alexryse': UserStats({
    'fname': 'Alex',
    'lname': 'Ryse',
    "height": 5.7,
    "weight": 165,
    "age": 20,
    "gender": 'Male',
})
"""

user_database = {}

@app.route('/user/<username>/stats', methods = ['POST', 'GET'])
def stats(username):
    if request.method == 'POST':
        data = request.get_json()

        # create user stats
        user_stats = UserStats(data)
        user = user_database[username]
        user.set_user_stats(user_stats)
        user_database[username] = user

        return jsonify({"message": f"user {username} created"}), 200
    elif request.method == 'GET':
        # return user stats
        if username in user_database:
            user = user_database[username]
            return jsonify(user.get_user_stats()), 200
        else:
            return jsonify({"message": "user not found"}), 404
        
@app.route('/user', methods = ['POST'])
def create_user():
    if request.method == 'POST':
        data = request.get_json()
        
        # create a user with username/password
        user = User(data)
        user_database[user.get_username()] = user

        return jsonify({"message": f"user {user.get_username()} created"}), 200
    
@app.route('/user/<username>', methods = ['GET'])    
def get_user(username):
    if request.method == 'GET':
        # return the username/password
        if username in user_database:
            user = user_database[username]
            return jsonify(user.get_password()), 200
        else:
            return jsonify({"message": "user not found"}), 404

    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)  # Change 3000 to your desired port 
    