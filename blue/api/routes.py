from flask import Blueprint
from blue import db
from blue.models import User, Post
from flask import jsonify

mod = Blueprint('api', __name__)


@mod.route('/getCategories')
def get_categories():
    post = User(username='Tesfa', email='alphatesfa789@gmail.com', password_hash='1234')
    db.session.add(post)
    db.session.commit
    users = User.query.all()
    print(users[0])
    return 'ss'


@mod.route('/addPost')
def add_post():
    u = User.query.get(0)
    p = Post(body='my first post!', author=u)
    db.session.add(p)
    db.session.commit()
    posts = Post.query.all()
    print(posts)
    return 'post'
