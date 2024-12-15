class User:
    def __init__(self, data):
        self.set_user(data)
        self.stats = None

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def set_user(self, data):
        self.username = data['username']
        self.password = data['password']

    def set_user_stats(self, stats):
        self.stats = stats

    def get_user_stats(self):
        return self.stats.get_stats()

class UserStats:
    def __init__(self, data):
        self.set_stats(data)

    def get_stats(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "gender": self.gender,
        }
    
    def set_stats(self, data):
        self.fname = data['fname']
        self.lname = data['lname']
        self.height = data['height']
        self.weight = data['weight']
        self.age = data['age']
        self.gender = data['gender']

