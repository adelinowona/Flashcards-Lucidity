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
    # user = ndb.KeyProperty(required=True)

# class Flashcard_set(ndb.Model):
#     easy_cards = ndb.KeyProperty(Easy)
#     medium_cards = ndb.KeyProperty(Medium)
#     hard_cards = ndb.KeyProperty(Hard)
#     owner = ndb.KeyProperty(User)
