#-*- coding: utf-8 -*-
from flask import Flask
from random import choice

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#decoding='unicode_escape'

about_me = {
   "name": "Никита",
   "surname": "Меренков",
   "email": "Sizen321@specialist.ru"
}

quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },
]

len_quotes = {'Count' : len(quotes)}


@app.route("/")
def hello_world():
   return "Hello, World!"

@app.route("/about")
def about():
   return about_me

@app.route("/quotes")
def get_all_quotes():
   return quotes

@app.route('/quotes/<int:post_id>')
def get_quote(post_id):
   for i in range(len(quotes)):
      if quotes[i].get('id') == post_id:
         return quotes[i]
      else:
         return f"Quote with id={post_id} not found", 404

@app.route('/quotes/count')
def count_quote():
   return len_quotes

@app.route('/quotes/random')
def random_quote():
   return choice(quotes)

if __name__ == "__main__":
   app.run(debug=True)
