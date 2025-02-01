import mongoengine as me

class User(me.Document):
    name = me.StringField(required=True)
    email = me.EmailField(required=True, unique=True)
    age = me.IntField(min_value=18)
    
    def __str__(self):
        return self.name
