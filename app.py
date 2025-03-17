from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name = name, movies = movies)

name = 'Marukami'

movies = [
    {'title': '《青鸟·暗战》', 'year': '1989'},
    {'title': '《孤城·破晓》', 'year': '2010'},
    {'title': '《山海·暗战》', 'year': '2022'},
    {'title': '《星辰之密码》', 'year': '2006'},
    {'title': '《青鸟之秘史》', 'year': '2023'},
    {'title': '《星辰·追凶》', 'year': '1990'},
    {'title': '《锦衣·密码》', 'year': '2009'},
    {'title': '《山海·未央》', 'year': '2014'},
    {'title': '《星辰之未央》', 'year': '1984'},
    {'title': '《青鸟之追凶》', 'year': '2006'},
]