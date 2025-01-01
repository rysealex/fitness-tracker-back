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

@app.route('/user/<username>/stats', methods = ['POST', 'GET', 'PUT'])
def stats(username):
    if request.method == 'POST':
        data = request.get_json()

        # create user stats
        user_stats = UserStats(data)
        user_database[username].set_user_stats(user_stats)

        return jsonify({"message": f"user {username} stats created"}), 200
    elif request.method == 'GET':
        # return user stats
        if username in user_database:
            user = user_database[username]
            return jsonify(user.get_user_stats().get_stats()), 200
        else:
            return jsonify({"message": "user not found"}), 404
    elif request.method == 'PUT':
        # update user stats(weight, height)
        if username not in user_database:
            return jsonify({"message": "User not found"}), 404
        data = request.get_json()
        weight = data.get('weight')
        height = data.get('height')
        user = user_database[username]
        user_stats = user.get_user_stats()
        # update weight and height if provided in the request
        if weight:
            user_stats.set_weight(weight)
        if height:
            user_stats.set_height(height)
        # save the updated stats
        user.set_user_stats(user_stats)
        return jsonify({"message": f"User {username} stats updated"}), 200

        
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
    