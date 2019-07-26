# main.py
# the import section
import webapp2
import os
import jinja2
import json
from models import Card
import random

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write("Welcome")

# class SignUp(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/home.html')
#         self.response.write("Welcome")
#
class Profile(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write("Hey there!")

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






# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/signup', SignUp),
    ('/profile', Profile),
    ('/create', Create),
    ('/sort', Sort)

], debug=True)
