from google.appengine.ext import ndb


class Easy(ndb.Model):
    content = ndb.StringProperty(required=True)
class Medium(ndb.Model):
    content = ndb.StringProperty(required=True)
class Hard(ndb.Model):
    content = ndb.StringProperty(required=True)
