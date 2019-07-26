from google.appengine.ext import ndb

# class Easy(ndb.Model):
#     content = ndb.StringProperty(required=True)
#     user = ndb.KeyProperty(Profile)
#
# class Medium(ndb.Model):
#     content = ndb.StringProperty(required=True)
#     user = ndb.KeyProperty(Profile)
#
# class Hard(ndb.Model):
#     content = ndb.StringProperty(required=True)
#     user = ndb.KeyProperty(Profile)

class Profile(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    user_id = ndb.StringProperty()

# class Flashcard_set(ndb.Model):
#     easy_cards = ndb.KeyProperty(Easy)
#     medium_cards = ndb.KeyProperty(Medium)
#     hard_cards = ndb.KeyProperty(Hard)
#     owner = ndb.KeyProperty(User)
