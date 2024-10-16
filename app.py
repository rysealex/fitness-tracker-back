from flask import Flask, request, jsonify
from user import UserStats
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
    "birthday": '06/04/2004'
})
"""

user_data = {}

@app.route('/user/<username>', methods = ['POST', 'GET'])
def profile(username):
    if request.method == 'POST':
        data = request.get_json()

        # create user data
        user = UserStats(data)
        user_data[username] = user

        return jsonify({"message": f"user {username} created"}), 200
    elif request.method == 'GET':
        # return user data
        if username in user_data:
            user = user_data[username]
            return jsonify(user.get_stats()), 200
        else:
            return jsonify({"message": "user not found"}), 404
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)  # Change 3000 to your desired port 
    