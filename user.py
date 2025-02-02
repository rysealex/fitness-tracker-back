from datetime import datetime

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
        self.birthday = data.get('birthday')
        self.gender = data.get('gender')
        self.profile_pic = data.get('profile_pic')

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height

    def calculate_age(self):
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def get_stats(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "height": self.height,
            "weight": self.weight,
            "age": self.calculate_age(),
            "birthday": self.birthday,
            "gender": self.gender,
            "profilepic": self.profile_pic 
        }