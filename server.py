from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'posts')


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/posts/create', methods=['POST'])
def create():
    query = "INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
    data = {
        'description': request.form['posts']
    }
    mysql.query_db(query, data)
    return_query = "SELECT * FROM posts"
    all_posts = mysql.query_db(return_query)
    return render_template('posts.html', all_posts = all_posts)

@app.route('/posts/index_json')
def index_json():
    query = "SELECT * FROM posts"
    all_posts = mysql.query_db(query)
    return jsonify(all_posts = all_posts)

@app.route('/posts/index_html')
def index_partial():
    query = "SELECT * FROM posts"
    all_posts = mysql.query_db(query)
    return render_template('posts.html', all_posts = all_posts)

@app.route('/posts')
def posts():
    all_posts = mysql.query_db("SELECT * FROM posts")

    return render_template('posts.html', all_posts = all_posts)


app.run(debug=True)
