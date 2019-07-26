from google.appengine.ext import ndb

class Question(ndb.Model):
    level = ndb.StringProperty(required=True)
    question = ndb.StringProperty(required=True)
    answer = ndb.StringProperty(required=True)
    # user = ndb.KeyProperty(required=True)

# class Medium(ndb.Model):
#     content = ndb.StringProperty(required=True)
#     user = ndb.KeyProperty(User)
#
# class Hard(ndb.Model):
#     content = ndb.StringProperty(required=True)
#     user = ndb.KeyProperty(User)
#
# class User(ndb.Model):
#     user_name = ndb.StringProperty(required=True)
#     user_id = ndb.StringProperty()
#
# class Flashcard_set(ndb.Model):
#     easy_cards = ndb.KeyProperty(Easy)
#     medium_cards = ndb.KeyProperty(Medium)
#     hard_cards = ndb.KeyProperty(Hard)
#     owner = ndb.KeyProperty(User)
