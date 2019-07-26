from google.appengine.ext import ndb

class Card(ndb.Model):
    level = ndb.IntegerProperty(required=True)
    question = ndb.StringProperty(required=True)
    answer = ndb.StringProperty(required=True)
    # user = ndb.KeyProperty(required=True)
