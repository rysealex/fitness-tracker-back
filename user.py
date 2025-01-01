class User:
    def __init__(self, data):
        self.username = data.get('username')
        self.password = data.get('password')
        self.user_stats = None

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def set_user_stats(self, user_stats):
        self.user_stats = user_stats

    def get_user_stats(self):
        return self.user_stats

class UserStats:
    def __init__(self, data):
        self.fname = data.get('fname')
        self.lname = data.get('lname')
        self.height = data.get('height')
        self.weight = data.get('weight')
        self.age = data.get('age')
        self.gender = data.get('gender')

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height
        
    def get_stats(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "gender": self.gender
        }