#main.py
# the import section
import webapp2
import os
import jinja2
import json
from models import Question

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
# class Profile(webapp2.RequestHandler):
#     def get(self):
#         template = JINJA_ENVIRONMENT.get_template('templates/home.html')
#         self.response.write("Welcome")

class Create(webapp2.RequestHandler):
    def get(self):
        create_template = JINJA_ENVIRONMENT.get_template('templates/create.html')
        self.response.write(create_template.render())

    def post(self):
        the_question = self.request.get('question')
        the_answer = self.request.get('answer')

        card = Question(question=the_question, answer= the_answer, level="easy")
        card_two = Question(question=the_question, answer= the_answer, level="medium")
        card_three = Question(question=the_question, answer= the_answer, level="hard")
        # card_data_answers = Hard(multiple_answers = the_answer)
        card.put()
        self.redirect('/')






# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/signup', SignUp),
    # ('/profile', Profile)
    ('/create', Create),

], debug=True)
