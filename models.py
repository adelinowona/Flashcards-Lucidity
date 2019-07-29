from google.appengine.ext import ndb

class Profile(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    user_id = ndb.StringProperty()

class Card(ndb.Model):
    level = ndb.IntegerProperty(required=True)
    question = ndb.StringProperty(required=True)
    answer = ndb.StringProperty(required=True)
    owner = ndb.StringProperty()

# class Flashcard_set(ndb.Model):
#     cards = ndb.StringProperty(repeated=True)
#     topic = ndb.StringProperty()
#     owner = ndb.KeyProperty(Profile)
