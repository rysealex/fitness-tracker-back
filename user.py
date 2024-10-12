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
            "birthday": self.birthday
        }
    
    def set_stats(self, data):
        self.fname = data['fname']
        self.lname = data['lname']
        self.height = data['height']
        self.weight = data['weight']
        self.age = data['age']
        self.gender = data['gender']
        self.birthday = data['birthday']

