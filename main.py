#main.py
# the import section
import webapp2
import os
import jinja2
import json
from models import Profile, Card
from google.appengine.api import users
from google.appengine.api import urlfetch
import random

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # If the user is logged in...
        if user:
          email_address = user.nickname()
          current_user = Profile.query().filter(Profile.email == email_address).get()
          # If the user is registered...
          if current_user:
            # Greet them with their personal information
            self.redirect("/profile0")
          # If the user isn't registered...
          else:
            # Offer a registration form for a first-time visitor:
            self.redirect('/profile')

        else:
          # If the user isn't logged in...
          login_url = users.create_login_url('/')
          template = JINJA_ENVIRONMENT.get_template('templates/Googlelogin.html')
          dict_variable = {
            "login_url": login_url
          }
          self.response.write(template.render(dict_variable))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("You are signed out")



class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/profile.html')
        self.response.write(template.render())




    def post(self):
        user_name = self.request.get('username')
        name = self.request.get('name')
        email = self.request.get('email')
        current_user = Profile(user_name=user_name, name=name, email=email,)
        current_user.put()
        dict_variable = {
            "username": user_name
        }
        template = JINJA_ENVIRONMENT.get_template('templates/profile0.html')
        self.response.write(template.render(dict_variable))

class Profile0Handler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        email_address = user.nickname()
        signout_link_html = users.create_logout_url('/login')
        current_user = Profile.query().filter(Profile.email == email_address).get()
        if current_user:
            dict_variable = {
                "username": current_user.user_name,
                "login_url": signout_link_html
            }
            template = JINJA_ENVIRONMENT.get_template('templates/profile0.html')
            self.response.write(template.render(dict_variable))
            
class Create(webapp2.RequestHandler):
    def get(self):
        create_template = JINJA_ENVIRONMENT.get_template('templates/create.html')
        self.response.write(create_template.render())

    def post(self):
        the_question = self.request.get('question')
        the_answer = self.request.get('answer')
        difficulty = int(self.request.get('difficulty_selection'))

        card = Card(question=the_question, answer= the_answer, level=difficulty)

        # card_data_answers = Hard(multiple_answers = the_answer)
        card.put()
        self.redirect('/create')


class Sort(webapp2.RequestHandler):
    def get(self):
        # some_levels = Card.query().order(Card.level).fetch()
        # sort_template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        # self.response.write(sort_template.render({"level_info": some_levels}))
        template = JINJA_ENVIRONMENT.get_template('templates/flashcard.html')
        card = Card.query().filter(Card.level == random.randint(1,3)).get()
        dict_for_template = {
            "my_answer": card.answer,
            "my_question": card.question,
        }
        self.response.write(template.render(dict_for_template))



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginHandler),
    ('/profile', ProfileHandler),
    ('/profile0', Profile0Handler),
    ('/create', Create),
    ('/sort', Sort),

], debug=True)
