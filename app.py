import os
from flask import Flask, request, jsonify
from user import UserStats, User
from flask_cors import CORS
from flask import send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/user/*": {"origins": "http://localhost:3000"}})

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

# folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# check if upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

user_database = {}

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/user/<username>/profile-pic', methods=['PUT'])
def upload_profile_picture(username):
    if request.method == 'OPTIONS':
        return '', 200
    
    if username not in user_database:
        return jsonify({"message": "User not found"}), 404
    
    user = user_database[username]

    # Check if 'file' is in request.files
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    # Handle the file upload
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        file.save(filepath)  # Save the file to the uploads folder
    except Exception as e:
        return jsonify({"message": f"Error saving file: {str(e)}"}), 500

    # Update user's profile with the file path
    user_stats = user.get_user_stats()
    user_stats.profile_pic = filepath  # Save the path of the profile picture
    user.set_user_stats(user_stats)

    return jsonify({
        "message": "Profile picture updated successfully",
        "profile_pic": f"/uploads/{filename}"  # Return the image URL
    }), 200

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
    