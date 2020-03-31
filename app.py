import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'i_brary'
app.config['MONGO_URI'] = 'mongodb://sw1ckham:1hamcvcw123@myfirstcluster-shard-00-00-iff8d.mongodb.net:27017,myfirstcluster-shard-00-01-iff8d.mongodb.net:27017,myfirstcluster-shard-00-02-iff8d.mongodb.net:27017/i_brary?ssl=true&replicaSet=myFirstCluster-shard-0&authSource=admin&retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_books')
def show_books():
    return render_template('books.html', books=mongo.db.books.find())


@app.route('/add_book')
def add_book():
    return render_template('addbook.html')


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('show_books'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)